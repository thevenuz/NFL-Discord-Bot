import aiohttp
import json
from copy import deepcopy
from datetime import datetime, timedelta, time
from typing import Dict, List
from nflbot.logger.baselogger import BaseLogger
from nflbot.models.score import Score, Game, GameStatus
from nflbot.utils.configutil import ConfigUtil

class ScoreImpl:
    def __init__(self) -> None:
        self.filePrefix="nflbot.pluginsimpl.commands.scoreimpl"
        self.logger=BaseLogger().loggger_init()


    async def get_live_score(self) -> List[Game]:
        try:
            self.logger.info("%s.get_live_score method invoked", self.filePrefix)

            today = datetime.today()
            startDate = today - timedelta(days=4)
            endDate = today + timedelta(days=1)

            startDate = startDate.strftime("%Y%m%d")
            endDate = endDate.strftime("%Y%m%d")

            settings = await ConfigUtil().load_settings()

            apiUrl = settings.ApiEndpoint

            req = f"{apiUrl}{startDate}-{endDate}"

            async with aiohttp.ClientSession() as session:
                async with session.get(req) as response:
                    result = json.loads(await response.text())

            games = await self.__parse_game_data(result)
            
            filteredGames = list(filter(lambda x: x["home"].Status == GameStatus.Ongoing, games))

            if filteredGames:
                return filteredGames

            return games

        except Exception as e:
            self.logger.fatal("Exception occured in %s.get_live_score method", exc_info=1)
            raise e
        
    async def __parse_game_data(self, result: Dict) -> List[Game]:
        try:
            self.logger.info("%s.__parse_game_data method invoked", self.filePrefix)

            game: Game ={}
            games: List[Game] = []

            homeTeam = Score()
            awayTeam = Score()

            events= result["events"]

            today = (datetime.combine(datetime.today(), time.min))
            nextDay = (datetime.combine(datetime.today(), time.max) + timedelta(hours=3))

            latestEvents = sorted(filter(lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%MZ")  >= today and datetime.strptime(x["date"], "%Y-%m-%dT%H:%MZ") < nextDay, events),
                                  key=lambda x: x["date"])

            latestEventsCopy= deepcopy(latestEvents)

            if latestEvents:
                events = latestEvents
            else:
                events.sort(key=lambda item:item['date'], reverse=True)

            for event in events:
                if event:
                    for competition in event["competitions"]:
                        if competition:
                            homeTeam = await self.__fill_game_details(competition["competitors"][0], event["date"])
                            game["home"] = deepcopy(homeTeam)

                            awayTeam = await self.__fill_game_details(competition["competitors"][1], event["date"])
                            game["away"] = deepcopy(awayTeam)
                            
                            games.append(deepcopy(game))

                            if not latestEventsCopy and len(games) >= 3:
                                return games

            return games
        
        except Exception as e:
            self.logger.fatal("Exception occured in %s.__parse_game_data method", self.filePrefix, exc_info=1)
            raise e
        

    async def __fill_game_details(self, gameData: Dict, gameDate:str) -> Score:
        try:
            self.logger.info("%s.__fill_game_details method invoked", self.filePrefix)

            thresholdTime= datetime.utcnow()

            score = Score()

            score.Score = gameData["score"]
            score.Team.Name = gameData["team"]["name"]
            score.Team.DisplayName = gameData["team"]["displayName"]
            score.Team.Color= gameData["team"]["color"]

            if "winner" in gameData:
                score.Winner = gameData["winner"]
                score.Status = GameStatus.Completed

            else:
                if (thresholdTime >= datetime.strptime(gameDate, "%Y-%m-%dT%H:%MZ")):
                    score.Status = GameStatus.Ongoing
                else:
                    score.Status = GameStatus.YetToStart

            return score
        
        except Exception as e:
            self.logger.fatal("Exception occured in %s.__fill_game_details method", self.filePrefix, exc_info=1)
            raise e
        