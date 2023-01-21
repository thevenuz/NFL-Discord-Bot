import React from 'react';
import { Link} from "react-router-dom";

const PrivacyPolicy = () => {
  return (
    <div className="p-2 flex-1 flex flex-col">
      <div className="flex mx-auto px-2">
        <p className="text-2xl font-bold underline underline-offset-2">
          PRIVACY POLICY
        </p>
      </div>
      <div className="flex-1 px-6 shadow-md py-2 mt-4 flex-col space-y-8 justify-around">
        <div>
          <p className="text-2xl font-semibold">
            What information do we collect?
          </p>
          <ul className=" list-disc">
            <li className="ml-8">
              NFL livescore bot does not collect or store any data at all from
              the users. The only data the bot ever receive from the client is the server Id and server name whenever
              the bot joins a server. Other than this the bot does not
              collect or store any other form of data.
            </li>
          </ul>
        </div>
        <div>
          <p className="text-2xl font-semibold">How do we use information?</p>
          <ul className=" list-disc">
            <li className="ml-8">
              The only data the bot collects is server name and server Id and
              this data is only used to notify the bot developers whenver the
              bot joins a server or leaves a server. Othar than this, the
              collected data is not used in any other manner.
            </li>
          </ul>
        </div>
        <div>
          <p className="text-2xl font-semibold">
            What information do we share?
          </p>
          <ul className=" list-disc">
            <li className="ml-8">
              We don't collect any information from the users and we don't share
              information of the users to any third party.
            </li>
          </ul>
        </div>
        <div>
          <p className="text-2xl font-semibold">
            How to make sure your data gets deleted?
          </p>
          <ul className=" list-disc">
            <li className="ml-8">
              We don't collect any infromation from the users in the first
              place. The only data we collect is of server name and server Id
              and if you want to make sure that even this data gets deleted, you
              can always request it in our{" "}
              <a
                className="underline underline-offset-4 text-blue-300"
                href="https://discord.gg/S3hhw9kSKV" target='_blank'
              >
                support server
              </a>
              .
            </li>
          </ul>
        </div>
        <div>
          <Link to="/terms-of-service">
            <p className='underline underline-offset-4 text-blue-200'>Check Terms of Service</p>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default PrivacyPolicy;
