import discord
from discord.ext import commands
from pathlib import Path
import json

def getConfig(element: str):
    with open(str(Path(__file__).parent.absolute()) + '/config.json') as json_file:
        config = json.load(json_file)
    return config[element]


client = commands.Bot(command_prefix = 'h!', help_command=None, description='Bot that handles history stuff.')

@client.event
async def on_ready():
    print('Bot is ready!')
    print(f'Logged in as {client.user}')
    print('')
    print('Author: CrumblyLiquid (CrumblyLiquid#6668)')
    print('')
    print('If you find any bugs please report to:\n- https://github.com/CrumblyLiquid/Mics-Bots/tree/master/HistoryBot\n- crumblyliquid@gmail.com')
    print('')


client.run(getConfig('token'), reconnect=True)