import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)
bot.remove_command("help")
