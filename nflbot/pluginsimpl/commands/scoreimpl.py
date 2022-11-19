import aiohttp
import json
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

            apiUrl="https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?limit=1000&dates="

            req=f"{apiUrl}{startDate}-{endDate}"

            async with aiohttp.ClientSession() as session:
                async with session.get(req) as response:
                    result = json.loads(await response.text())

            games = await self.__parse_game_data(result)
            
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
            #events.sort(key=lambda item:item['date'], reverse=True)

            today = (datetime.combine(datetime.today(), time.min))
            nextDay = (datetime.combine(datetime.today(), time.max) + timedelta(hours=3))

            latestEvents = sorted(filter(lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%MZ")  >= today and datetime.strptime(x["date"], "%Y-%m-%dT%H:%MZ") < nextDay, events),
                                  key=lambda x: x["date"], reverse=True)

            if latestEvents:
                events = latestEvents
            else:
                events.sort(key=lambda item:item['date'], reverse=True)

            for event in events:
                if event:
                    print(type(event["date"]))
                    for competition in event["competitions"]:
                        if competition:
                            homeTeam = await self.__fill_game_details(competition["competitors"][0], event["date"])
                            awayTeam = await self.__fill_game_details(competition["competitors"][1], event["date"])

                            game["home"] = homeTeam
                            game["away"] = awayTeam
                            games.append(game)


                            if not latestEvents and games.count >= 3:
                                break

            return games
        
        except Exception as e:
            self.logger.fatal("Exception occured in %s.__parse_game_data method", self.filePrefix, exc_info=1)
            raise e
        

    async def __fill_game_details(self, gameData: Dict, gameDate:str) -> Score:
        try:
            self.logger.info("%s.__fill_game_details method invoked", self.filePrefix)

            game = Score()

            game.Score = gameData["score"]

            thresholdTime= datetime.utcnow()

            if "winner" in gameData:
                game.Winner = gameData["winner"]
                game.Status = GameStatus.Completed

            else:
                if (thresholdTime >= datetime.strptime(gameDate, "%Y-%m-%dT%H:%MZ")):
                    game.Status = GameStatus.Ongoing
                else:
                    game.Status = GameStatus.YetToStart


            game.Team.Name = gameData["team"]["name"]
            game.Team.DisplayName = gameData["team"]["displayName"]
            game.Team.Color= gameData["team"]["color"]

            return game
        
        except Exception as e:
            self.logger.fatal("Exception occured in %s.__fill_game_details method", self.filePrefix, exc_info=1)
            raise e
        