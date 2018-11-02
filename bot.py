import random
import asyncio
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("sprinkle ")
TOKEN = "NDQxMzQ0MzYxNjUzODYyNDEw.Dcu5lA.QlYl8bxUnqnF4AkkYtCcjyZi9kM"


client = Bot(command_prefix=BOT_PREFIX)

@client.command(name="8ball",
                description="Answers a yes/no question.",
                breif="Answers from the beyond.",
                aliases=["eight_ball","eightball","8-ball"],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        "That is a resounding no",
        "It is not looking likely",
        "Too hard to tell",
        "It is quite possible",
        "Definitely",
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

    @client.event
    async def on_ready():
        await client.change_presence(game=Game(name="with humans"))
        print("Logged in as " + client.user.name)

        async def on_message(message):
            if message.author == client.user:
                return

        if message.content/startswith("!!help"):
            msg = "{0.author.mention}\nThe current prefix is:"+BOT_PREFIX+"\n\nCommands:\n"+BOT_PREFIX+"8ball - Responds to yes/no questions.".format(message)
            await client.send_message(message.channel, msg)

        if message.content/startswith("afk"):
            msg = "i dont care if ur afk {0.author.mention}."
            await client.send_message(message.channel, msg)

        @client.command()
        async def bitcoin():
            url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
            async with aiohttp.ClientSession() as session:
                raw_response = await session.get(url)
                response = await raw_response.json(content_type="application/javascript")
                await client.say("Bitcoin price is: $" + response["bpi"]["USD"]["rate"])

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)
