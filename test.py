import os
import time
import json
from slackclient import SlackClient
count = 0
scores = dict()

RTM_READ_DELAY = 1 # 1 second delay between reading from RTM


# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]

        while True:
            rm = slack_client.rtm_read()
            if len(rm) > 0:
                dc = rm[0]
                if dc['type'] == 'message':
                    usr = dc['user']

                    if dc['text'] == 'gane':
                        if usr not in scores:
                            scores [usr] = 1
                        else:
                            scores[usr] = scores[usr] + 1

                        print (scores)
                    else: continue


            '''cómo mierda le resto? pareciera no funcionar esto

                    if dc['text'] == 'perdi':
                         if usr not in scores:
                             scores [usr] = 0
                         else:
                             scores[usr] = scores[usr] - 1

                         print (scores)
                     else: continue
                else: continue
            '''

            # if rd['text'] == 'gane':
            #     scoreboard = scoreboard + 1
            #     print (scoreboard)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
