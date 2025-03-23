import discord
from discord.ext import commands
import jishaku

intents = discord.Intents.all()

# Set your bot's prefix (e.g., "!")
bot = commands.Bot(command_prefix="!", intents = intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Be back soon..."))
    await bot.load_extension("jishaku")

# Command: !hello
@bot.command()
async def ping(ctx):
  return await ctx.reply(f"latency: {round(bot.latency * 1000)}")
  
# Run the bot using your token
bot.run('MTM1MzQ3NzM2MzAzOTczMTg2Mw.G_j77X.EMpop7Z9IbxEZjqAFpyjPPuN7AdJblaOUlFRks')
