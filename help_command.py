import asyncio
from bot_init import bot
import discord


@bot.command(pass_context=True)
async def sos(ctx):  # команда для отправки сообщения с командами
    await ctx.message.delete()
    print("Send help message")
    text_1 = "Это БЕСПЛАТНЫЙ бот-переводчик. Он умеет переводить ваши сообщения. " \
             "Дабы никого не бесить восклицательными знаками и слешами, их тут просто нет"
    emb = discord.Embed(title=text_1, color=discord.Color.gold())
    text_2 = "__**Команды: (можно несколько через пробел)**__\n"
    text = "ан *(да, прямо по русски) - перевод на английский*\n" \
           "ис *- перевод на испанский*\n" \
           "нм *- перевод на немецкий*\n" \
           "фр *- перевод на французский*\n" \
           "яп *- перевод на японский*\n" \
           "Чтобы удалить переводимое сообщение, допишите букву 'у' к первому языку, например: 'ису ан Привет мир!'\n" \
           "Чтобы озвучить переводимое сообщение, допишите букву 'г' к первому языку, например: 'фрг ис Привет мир!'\n"
    text_1 = "**Перевод по ответу: ответьте на сообщение сообщением " \
             "c буквой 'п'. Сообщение будет переведено на русский, или ответте сообщением " \
             "'п ан', 'п фр' и т. д., будет отправлен перевод на соответствующий язык**\n" \
             "Команды нечувствительны к регистру\n"
    emb.add_field(name=text_2, value=text + text_1, inline=False)
    text_2 = "__**Commands: (multiple spaces are possible)**__\n"
    text = "ru *- translate to Russian*\n" \
           "en *- translate to English*\n" \
           "fr *- translate to French*\n" \
           "de *- translate to Deutsch*\n" \
           "es *- translate to Spanish*\n" \
           "ja *- translate to Japanese*\n" \
           "To delete a translatable message, add a letter 'd' to the first language, for " \
           "example: 'rud fr Hello world!'\n" \
           "To voice the message you are translating, add the letter 'v' to the first language, for example: " \
           "'ruv es Hello world!'\n"
    text_1 = "**Translation by answer: reply to a message with a message " \
             "with the letter 't'. The message will be translated into English, or reply with a message " \
             "'t en', 't fr', etc., a translation into the appropriate language will be sent**\n" \
             "Commands are case insensitive\n"
    emb.add_field(name=text_2, value=text + text_1, inline=False)
    text = "Example:\n" \
           "es Hello\n" \
           "-> こんにちは"
    emb.add_field(name=text, value="Current version: 0.5.0", inline=False)
    view = discord.ui.View()
    btn = discord.ui.Button(style=discord.ButtonStyle.danger, label='Delete this message', disabled=False)
    view.add_item(btn)
    g = await ctx.send(embed=emb, view=view)
    try:
        await bot.wait_for('button_click', check=lambda message: message.author == ctx.author, timeout=300.0)
    except asyncio.TimeoutError:
        emb.add_field(name=text, value="Current version: 0.5.0", inline=False)
        view = discord.ui.View()
        btn = discord.ui.Button(style=discord.ButtonStyle.danger, label='Delete this message', disabled=True)
        view.add_item(btn)
        await g.edit(view=view)
    else:
        await g.delete()
    return True
