import discord
from discord.ext import commands
from pathlib import Path
import json

def getConfig(element: str):
    with open(str(Path(__file__).parent.absolute()) + '/config.json') as json_file:
        config = json.load(json_file)
    return config[element]

client = commands.Bot(command_prefix='\\', description='Tiny quote bot. Be nice to him please :)')

@client.event
async def on_ready():
    print('Bot is ready!')
    print(f'Logged in as {client.user}')
    print('')
    print('Author: CrumblyLiquid (CrumblyLiquid#6668)')
    print('')
    print('If you find any bugs please report to:\n- https://github.com/CrumblyLiquid/Mics-Bots/tree/master/QuoteBot\n- crumblyliquid@gmail.com')

@client.command(aliases=['q', 'qu'])
async def quote(ctx, *, text):
        with open(str(Path(__file__).parent.absolute()) + '/quotes.txt', 'a') as file:
            file.write(text + '\n')
        await ctx.send(f'Quote saved!\nQuote: `{text}`')

@client.command(aliases=['ql', 'qli', 'quli', 'qul'])
async def quotelist(ctx):
    with open(str(Path(__file__).parent.absolute()) + '/quotes.txt', 'r') as file:
        content = file.readlines()

    msgtext='All quotes:\n'
    message = msgtext
    ctlen = len(content)

    for x in content:
        ctlen -= 1
        if len(message) + len(x) < 2000:
            if ctlen == 0:
                message += x
                await ctx.send(message)
            else:
                message += x
        else:
            await ctx.send(message)
            message = x

client.run(getConfig('token'), reconnect=True)