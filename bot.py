import os
import discord
import logging
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive


class BoT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logado como {self.bot.user} ({self.bot.user.id})')

    @commands.Cog.listener()
    async def on_resume(self):
        print('Bot se reconectou')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(error)


intents = discord.Intents.default()
intents.members = True
intents.presences = True

Bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('-'), description='Under development', intents=intents)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)


load_dotenv()
token = os.environ['TOKEN']

if __name__ == '__main__':

    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            Bot.load_extension(f'commands.{filename[: -3]}')
    Bot.add_cog(BoT(Bot))
    keep_alive()
    Bot.run(token, reconnect=True)


# Bot.add_cog(music_play(Bot))
# Bot.add_cog(Spotify(Bot))


# @Bot.command()
# async def echo(ctx, *args):
 #   m_args = " ".join(args)
  #  await ctx.send(m_args)

#token = ""

# with open(".env") as file:
 #   token = file.read()
# Bot.run(token)
