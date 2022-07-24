import asyncio
import discord
from bot_init import bot
from constants import VERSIONS_DICT


@bot.command()
async def versions(ctx):  # отправка сообщения о версиях
    emb = discord.Embed(title="Exceptional Bot Versions", color=discord.Color.blue())
    for q in VERSIONS_DICT.items():
        emb.add_field(name=q[0], value=q[-1], inline=False)

    text = "While there are no ideas"
    emb.add_field(name="**(in developing)**\n", value=text, inline=False)
    emb.add_field(name="ᅠ ᅠ ", value="__*This message will be deleted in 2 minutes*__", inline=False)

    message = await ctx.send(embed=emb)
    print("Send versions info message")
    await asyncio.sleep(120)
    await message.delete()
    await ctx.message.delete()
    print("Versions info message deleted")
    return True
