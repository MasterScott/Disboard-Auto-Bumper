**app.json:** 
[![asd](https://camo.githubusercontent.com/bcffcd4a539d4b3c4bde97e0cea7503b9ac8d751ff8e4b5c5ad007a0eb59f518/68747470733a2f2f7777772e6865726f6b7563646e2e636f6d2f6465706c6f792f627574746f6e2e706e67)](https://www.heroku.com/deploy/?template=https://github.com/vaido-world/Disboard-Auto-Bumper)

# Auto Disboard Bumper

# User Token 
To get a user token: F12 -> Network -> Tick the Hide data URLS -> Type into the filter /api -> Look for file named "science" -> Press on a "headers" tab -> Look for Title "Request headers" -> find the "authorisation" in it

## What is disboard?
Disboard is a service were you can post your discord server to grow it. Click the [link](https://disboard.org/) to go to their website.

## What's the purpose?
The purpose of this Auto Bumper is to auto type the command `!d bump` every 2 hours (The cooldown time between bumping your server to the top page again). With this you will not have to type the command yourself, you can simply run this on heroku or a server and have a second discord account do it for you.

## Setup:
Setup is really easy, first install python3. Once installed simply run the command `pip install discord.py` this will install the discord libary for python. Allowing the bot to run correctly. 

After everything is setup open the python file and edit the lines with you token. As you can see with the image below it says for you to edit and uncomment the correct one. If you do not know what an environment variable is simply uncomment line 8 and replace "TOKEN" with your discord token. [Link](https://www.youtube.com/watch?v=tI1lzqzLQCs) - Click the link if you don't know what/how to get your discord token.
![pic](https://user-images.githubusercontent.com/21064622/120111142-70a50a80-c179-11eb-9380-6433c2e5f8cc.png)


## Starting the bot:
Once you have completed all the above simply run the code. `python3 bumper.py` depending on how many servers you are in this can take some time for it to boot up. (If its a fresh account in one server its instant.) Once booted go into the channel you want the bot to post in and type `--bla` and you are done, you should see your account type `!d bump` if this worked correct (Some reasons for it not working correctly is you have two python versions installed and it installed discord.py for another version, to fix this use `pip3 install discord.py` instead of the command above) just keep the script running. Every 2 hours it will automatically type `!d bump` in that same channel again.

## Why not use a bot?
Disboard automatically ignores `!d bump` commands from any bot token, this is why we need to use a real discord account.
