import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!witaj'):
        msg = 'Wiiiiiiiiitajcie tutaj Dooooknesss! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!komendy'):
        msg = ':black_small_square: !rangi - informacje o rangach VIP/SVIP/MVIP.
:black_small_square: !administracja - spis ekipy i administracji serwerka  discord.
:black_small_square: !mcserwer - ip KOZACKIEGO serwerka mc
:black_small_square: !serwer - informacje o serwerze 
:black_small_square: !8ball Pytanie? - odpowiedz bota
:black_small_square: !reklama - link do reklamy naszego discorda
:black_small_square: !regulamin - wyświetla regulamin serwera discord.
:black_small_square: !levels - pokazuje status lvl.
:black_small_square: !yt - informacje na temat reklamowania i rangi YouTuber
:black_small_square: !rank - pokazuje wykres lvl
:black_small_square: !porn - aaaa.....
:black_small_square: !humorek - żarciki 
:black_small_square: !kapselek - kapsle z tymbarka
:black_small_square: !emoji - emotki serwerowe
:black_small_square: !rekrutacja - informacje na temat rekrutacji {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Zalogowano jako')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDU1MzgzNzExODM2NDA1NzYw.Df7N7Q.DTVxzeYaNITacZvmKwC_gL43Nbo')
