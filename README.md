# LinkBot
Hello! This is my discord bot, LinkBot. He is made in Python, using [Discord.py](https://github.com/Rapptz/discord.py). You can find the documentation [here](https://discordpy.readthedocs.io/en/latest/index.html).
## Features
- A per-server Admin system that restricts Admin level commands from being used by non-admins.
- A per-server Quote database in which Admins can immortalize their friends' most disappointing, out-of-context statements.
- A per-server Birthday tracking system. Have an Admin set birthdays for everyone (who is important) and have LinkBot with them Happy Birthday when it comes!
- Youtube video and Google image first-result search embedding.
- Plus more, and more to come in the future!
## Getting Started
To get LinkBot to run, you'll need a Sensitive.py file. This file contains a few variables that are considered sensitive information. They are all strings:
- DISCORD_API_KEY: Your Discord API key. You can get one by going [here](https://discordapp.com/developers/applications/me/) and creating a new Discord application.
- RIOT_API_KEY: Your Riot Games API key. You can get one by going [here](https://developer.riotgames.com/) and signing up as a developer.
- GOOGLE_API_KEY: Your Google API key. You can get one by following the instructions [here](https://support.google.com/googleapi/answer/6158862?hl=en).

These two are optional, as they are part of an automatic role-assignment operation that I implemented for myself:
- MY_SERVER_ID: ID of the server in which you would like to set new members' role to a default role.
- ENTRY_LEVEL_ROLE_ID: ID of the default role for that server.

Once all of those have been defined, you will need a config file. The config file is generated automatically upon running the bot for the first time. It will be located at data/config.cfg by default. In the config file, you can specify who the owner of the bot is, and what the prefix for all commands will be. It is essential to set up the owner ID! You won't be able to access any of the commands that alter the databases without an owner to be the initial Admin. You also won't be able to log the bot out without killing the process.

Now that you have a Sensitive.py and a config file, the bot should be all ready. You can go ahead and add him to one of your servers and start him up.

# Commands
*This list of commands is not necessarily up-to-date.*
```
- admin list  |  admin add <@user|@role>...  |  admin remove <@user|@role>...
- birthday list  |  birthday set <name> <mm/dd>  |  birthday remove <name>
- help [here] [command]
- image <query>  |  img <query>
- logout  |  logoff
- lolgame <player> [,region]
- migrate <ch>, <ch>
- nsfw <on|off>
- play
- quote <#id>  |  quote list [author]  |  quote random [author]  
    |  quote add <quote -author>  |  quote remove <#id>
- suggest <feature>
- youtube <query>  |  yt <query>
```
