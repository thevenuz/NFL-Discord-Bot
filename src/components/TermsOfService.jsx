import React from 'react';
import { Link} from "react-router-dom";

const TermsOfService = () => {
  return (
    <div className="p-2 flex-1 flex flex-col">
      <div className="flex mx-auto px-2">
        <p className="text-2xl font-bold underline underline-offset-2">
          TERMS OF SERVICE
        </p>
      </div>

      <div className="flex-1 px-6 shadow-md py-2 my-4 space-y-2 justify-around">
        <p className="font-bold text-xl">
          Terms of Service for using NFL Livescore Bot:
        </p>
        <div>
          <p className="font-semibold text-lg my-4 underline">Conditions:</p>
          <p className="p-2">
            General conditions regarding NFL Livescore Discord Bot are under
            this topic.
          </p>
          <ol className="list-decimal p-2">
            <li className=" ml-8 py-2">
              Our terms and conditions apply to each and every user using NFL
              Livescore Bot.
            </li>
            <li className=" ml-8 py-2">
              By adding NFL Livescore Bot in your server, you agree to these
              terms of service and the future terms which we may add after a
              notice.
            </li>
          </ol>
        </div>

        <div>
          <p className="font-semibold text-lg my-4 underline">Terms of Use:</p>
          <ol className="list-decimal p-2">
            <li className=" ml-8 py-2">
              Intentional command spam or attempts to crash the bot should not
              be made.
            </li>
            <li className=" ml-8 py-2">
              NFL Livescore Bot Team reserves the rights to prohibit any server
              or user from using the Bot.
            </li>
            <li className=" ml-8 py-2">
              The client is responsible for any violation caused by them.
            </li>
            <li className=" ml-8 py-2">
              We have the rights to update terms of service anytime with a
              notice in the support server.
            </li>
          </ol>
        </div>
        <div>
          <Link to="/privacy-policy">
            <p className="underline underline-offset-4 text-blue-200">
              Check Privacy Policy
            </p>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default TermsOfService;
