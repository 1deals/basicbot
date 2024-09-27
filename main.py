import discord
from discord.ext import commands

# Set your bot's prefix (e.g., "!")
bot = commands.Bot(command_prefix="!")

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

# Command: !hello
@bot.command()
async def ping(ctx):
  return await ctx.reply(f"latency: {round(bot.latency * 1000)}")
  
# Run the bot using your token
bot.run('MTI4OTE4ODc5MjA2NTk4MjQ2NA.GacT1d.3PrsiMWUOXtIwgr0WndUnaAFltJx7O1NcNuJWw')
