<p align="center"><img src="https://github.com/ArthThapa/TNB-Ecosystem-Bot/blob/main/readme/TNB%20Ecosystem.png" width="300px"></p>
<h1 align="center">  TNB-Ecosystem-Bot  </h1>
<p align="center">A discord bot for TNB Community projects and services</p>

<p> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white" /> <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white" /></p>

<h4> About TNB Ecosystem Bot</h4>

TNB Ecosystem bot is a utility discord bot for auto moderation of discord links and serves as a projects API wrapper for discord.

#### Contributing
Clone the repo.

Install all the requirements using `pip install -r requirements.txt`

Set the required environment variables.
```shell
TNB_DISCORD_TOKEN = "Discord Bot Token" (string type)
SUPERUSERS = Discord IDs of SUPERUSERS in a list , ids should be (integer) type, ex:- [Id of SUPERUSER1, Id of SUPERUSER2, etc.]
BOT_MANAGER_ID = Discord ID of the Bot manager/developer, Bot manager has access to /kill command (integer) type.
```

#### Commands

`/whitelist add`: Add a server to the whitelist.  (SUPERUSER ONLY) <br />
`/whitelist remove`: Remove a server from the whitelist.    (SUPERUSER ONLY) <br />
`/whitelist all`: Show all the servers in the whitelist.    <br />

`/project all`: List of all TNB Projects  <br />
`/project show <project name>`: Know more about a specific project (PROJECT NAME SHOULD PRECISELY ACCURATE AS SHOWN IN THE LIST) <br />



