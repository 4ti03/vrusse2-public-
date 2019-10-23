import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import logging
import logging.handlers
import random
import json

# Bot créé par ramle seam#4665 et Redd#8194

TOKEN = "TOKEN"

my_logger = logging.getLogger('Discordbot launcher')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = '/dev/log')
my_logger.addHandler(handler)
my_logger.debug('Discordbot : Start of script')


bot = commands.Bot(command_prefix='/')



# ce qu'il se passe en se connectant
@bot.event
async def on_ready():
    print('Connecté en tant que')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# commandes du bot

# commande d'aide
bot.remove_command('help')
@bot.command()
async def help(ctx):
    try:
         
        await ctx.send("Coucou\nJe suis le gentil chien du grand prophète:\n")
		#await ctx.send("NON")
        embed=discord.Embed(title="Aide", color=0xff0080)
        embed.add_field(name="/help", value="Affiche cette aide.", inline=False)
        embed.add_field(name="/ok", value="Affiche un GIF de ok aléatoire.", inline=False)
        embed.add_field(name="/gif", value=" Affiche un GIF aléatoire parmis tout ceux en réserve.", inline=False)
        embed.add_field(name="/cat", value="Affiche un GIF de chat aléatoire.", inline=False)
        embed.add_field(name="/dog", value="Affiche un GIF de chien.", inline=False)
        embed.add_field(name="/what", value="Affiche un GIF 'WHAT' aléatoire.", inline=False)
        embed.add_field(name="/think", value="Affiche un GIF de réflexion aléatoire.", inline=False)
        embed.add_field(name="/yes", value="Affiche un GIF d'acquiessement aléatoire.", inline=False)
        embed.add_field(name="/no", value="Affiche un GIF de négation aléatoire.", inline=False)
        embed.add_field(name="/hurss", value="L'hymne de l'URSS en vocal, mais quelle bonheur !", inline=False)
        embed.add_field(name="/slt", value= "GIF de salutation.", inline =False)
        embed.add_field(name="/hacker", value="Affiche un GIF de h@ck3r aléatoire.", inline=False)
        embed.add_field(name="/gg", value="GIF de félicitation.", inline=False)
        embed.add_field(name="/dab", value="GIF de personne qui dab.", inline=False)
        embed.add_field(name="/ouaf -- VOCAL", value="Aboie dans le channel vocal.", inline=False)
        embed.add_field(name="/ouaf_angry -- VOCAL", value="OCTOGONE DE CHIENS !", inline=False)
        embed.add_field(name="/maisoui -- VOCAL", value="Réflexion nucléaire des rollers.", inline=False)
        embed.add_field(name="/nani -- VOCAL", value="You are already dead.", inline=False)
        embed.add_field(name="/multi nbr1 nbr2" , value="Multiplie 2 nombres.", inline=False)
        embed.add_field(name="/salt", value="Un peu de sel ça fait pas de mal ;).", inline=False)       
        embed.add_field(name="/lol", value="un petit gif de lol.", inline=False)
        embed.add_field(name="/russe", value="La russie est supérieure à tout sauf la Belgique sache le, vive Poutine !", inline=False)
        embed.add_field(name="/urss", value="L'URSS fut une grande chose, URA comrade !", inline=False)
        embed.add_field(name="/slav", value="Les slaves sont de bonnes personnes, fous mais sont un bon exemple de la beauté du monde.", inline=False)
        embed.add_field(name="/excusetoi", value="Excuse toi !", inline=False)
        embed.add_field(name="/add nbr1 nbr2", value="Additionne 2 nombres", inline=False)
        embed.add_field(name="/sou nbr1 nbr2", value="Soustrait 2 nombres", inline=False)
        embed.add_field(name="/div nbr1 nbr2", value="Divise 2 nombres", inline=False)
        embed.add_field(name="/calc", value="Envoie le lien vers une calculatrice", inline=False)
        
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))

# commande pour faire passer l'hymne de l'urss en vocal
@bot.command()
async def hurss(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("/root/bot/urss.mp3"), after=lambda e: print ('done', e))
        await asyncio.sleep(250)
        await vc.disconnect()
    except Exception as e:
        print(str(e))

# commande pour montrer des gif de la Russie
@bot.command()
async def russe(ctx):
	russe=["https://media.tenor.com/images/d0b633cb01b917601ed0f4030e032f5c/tenor.gif","https://media.tenor.com/images/afc2bede03a149dd6d082acd3eb25740/tenor.gif","https://media.tenor.com/images/c3b9522dbfe8be78ff4dc305c999013e/tenor.gif","https://media.tenor.com/images/77b5b573689cd8bebb95b19be686c303/tenor.gif",""]
	thisone = random.choice(russe)
	await ctx.send(thisone)
	
# commande pour montrer des gif de l'URSS
@bot.command()
async def urss(ctx):
	urss=["https://media.tenor.com/images/a31f7702838f0620981617d4dd067e48/tenor.gif","https://media.tenor.com/images/b278b992ab3c919559061859a5aa72ff/tenor.gif","https://media.tenor.com/images/87074b2a51c9c328f32180843737c77d/tenor.gif","https://media.tenor.com/images/c47c9b4baddc4479e26fa26cf7761d66/tenor.gif",""]
	thisone = random.choice(russe)
	await ctx.send(thisone)
	
# commande pour montrer des gif slaves
@bot.command()
async def slav(ctx):
	slav=[""]
	thisone = random.choice(russe)
	await ctx.send(thisone)

# commande pour montrer des gif de lol
@bot.command()
async def lol(ctx):
	lol=["https://media.giphy.com/media/65ODCwM00NVmEyLsX3/giphy.gif","https://media.giphy.com/media/3o6ozvv0zsJskzOCbu/giphy.gif","https://media.giphy.com/media/u36Ow6jBvWCFW/giphy.gif","https://media.giphy.com/media/3NtY188QaxDdC/giphy.gif","https://media.giphy.com/media/KiaU2EUyxjQB2/giphy.gif","https://media.giphy.com/media/3oFzlW4yxJIGR4SrSg/giphy.gif","https://media.giphy.com/media/wofyg8nxsWEmtR7eOK/giphy.gif","https://media.giphy.com/media/5zs7PKZVNu4toH0jC4/giphy.gif","https://media.giphy.com/media/11caEgnSDg0avS/giphy.gif","https://media.giphy.com/media/3oEjHSxRXpXTlzC15C/giphy.gif","https://media.giphy.com/media/Nn2wW3g0hwDEA/giphy.gif","https://media.giphy.com/media/3ov9k7qgHvACHJNOV2/giphy.gif"]
	thisone = random.choice(lol)
	await ctx.send(thisone)

# commande pour montrer un gif de... abaok
@bot.command()
async def ok(ctx):
	ok=["https://media.giphy.com/media/tIeCLkB8geYtW/giphy.gif","https://media.giphy.com/media/l0IyccEqUTO7xy9Ec/giphy.gif","https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif","https://media.giphy.com/media/iOMSfTen1pZUPTx2QF/giphy.gif","https://media.giphy.com/media/3o7abGQa0aRJUurpII/giphy.gif","https://media.giphy.com/media/3o6Zt8qDiPE2d3kayI/giphy.gif","https://media.giphy.com/media/QYdvAXCxn6TSVsa3ez/giphy.gif","https://media.giphy.com/media/3oKGz6x35nOiMJ3pqo/giphy.gif","https://media.giphy.com/media/lrPirPA0Bqmwgzdib6/giphy.gif"]
	thisone = random.choice(ok)
	await ctx.send(thisone)
	
# commande pour montrer un gif de dabeur
@bot.command()
async def dab(ctx):
    dab=["https://media.giphy.com/media/ifexwFOgPiWAn0p9AK/giphy.gif","https://tenor.com/Txfb.gif","https://media.giphy.com/media/A4R8sdUG7G9TG/giphy.gif","https://media.giphy.com/media/bXvwCQglnTGKs/giphy.gif","https://media.giphy.com/media/lae7QSMFxEkkE/giphy.gif","https://media.giphy.com/media/xUOwGmG2pRfFZUmdVe/giphy.gif","https://media.giphy.com/media/JEo5Y2ywdWRDW/giphy.gif","https://media.giphy.com/media/SoshjAcfNsOsw/giphy.gif","https://media.giphy.com/media/WxIBO7AsS6OJP02KRN/giphy.gif","https://media.giphy.com/media/cOqfwLtoTsYNL7SqSH/giphy.gif"]
    thisone = random.choice(dab)
    await ctx.send(thisone)

# commande pour... Mais gg comrade ! 
@bot.command()
async def gg(ctx):
    gg=["https://media.giphy.com/media/bXvwCQglnTGKs/giphy.gif","https://media.giphy.com/media/ytTYwIlbD1FBu/giphy.gif","https://media.giphy.com/media/12xWfDQcGkbU1W/giphy.gif","https://media.giphy.com/media/4HnRlpEINn9q3pRYMR/giphy.gif","https://media.giphy.com/media/TgFibAJdezKXUYsddv/giphy.gif","https://media.giphy.com/media/G22vVm4jcPeco/giphy.gif","https://media.giphy.com/media/3ohc0Qyv7kWHBYzSqk/giphy.gif","https://media.giphy.com/media/10C8dIIpCux0ru/giphy.gif"]
    thisone = random.choice(gg)
    await ctx.send(thisone)

# commande pour montrer un gif random parmis tout ceux en stock
@bot.command()
async def gif(ctx):
    gif=["https://media.giphy.com/media/4iqMzLtBO9KSY/giphy.gif","https://media.giphy.com/media/A4R8sdUG7G9TG/giphy.gif","https://media.giphy.com/media/bXvwCQglnTGKs/giphy.gif","https://media.giphy.com/media/lae7QSMFxEkkE/giphy.gif","https://media.giphy.com/media/xUOwGmG2pRfFZUmdVe/giphy.gif","https://media.giphy.com/media/XmgbcmQvLEThS/giphy.gif","https://media.giphy.com/media/WxIBO7AsS6OJP02KRN/giphy.gif","https://media.,giphy.com/media/SoshjAcfNsOsw/giphy.gif","https://media.giphy.com/media/3h1L0Zhu4oMxhyRLAT/giphy.gif","https://media.giphy.com/media/3oKIPf1BaBDILVxbYA/giphy.gif","https://media.giphy.com/media/3o6Zt3AC93PIPAdQ9a/giphy.gif","https://media.giphy.com/media/10C8dIIpCux0ru/giphy.gif","https://media.giphy.com/media/12xWfDQcGkbU1W/giphy.gif","https://media.giphy.com/media/ytTYwIlbD1FBu/giphy.gif","https://cdn.discordapp.com/attachments/620021478569672704/620022300405792798/inconnu.gif","https://cdn.discordapp.com/attachments/620021478569672704/620022426243432470/inconnu.gif","https://cdn.discordapp.com/attachments/620021478569672704/620022300405792798/inconnu.gif","https://media.giphy.com/media/YQitE4YNQNahy/giphy.gif","https://media.giphy.com/media/UqxVRm1IaaIGk/giphy.gif","https://media.giphy.com/media/TOWeGr70V2R1K/giphy.gif","https://media.giphy.com/media/ZvLUtG6BZkBi0/giphy.gif","https://media.giphy.com/media/QNFhOolVeCzPQ2Mx85/giphy.gif","https://media.giphy.com/media/VbAFrrDVGAvZu/giphy.gif","https://media.giphy.com/media/Wsju5zAb5kcOfxJV9i/giphy.gif","http://giphygifs.s3.amazonaws.com/media/rMS1sUPhv95f2/giphy.gif","https://media.giphy.com/media/3oriNLx3dUqFgVi86I/giphy.gif","https://media.giphy.com/media/9kSM4y028LvvW/giphy.gif","http://giphygifs.s3.amazonaws.com/media/eCqFYAVjjDksg/giphy.gif","https://media.giphy.com/media/eDmCKa8Wd3MUU/giphy.gif","https://media.giphy.com/media/13UZisxBxkjPwI/giphy.gif","https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif,http://giphygifs.s3.amazonaws.com/media/12XMGIWtrHBl5e/giphy.gif","https://media.giphy.com/media/eKrgVyZ7zLvJrgZNZn/giphy.gif","https://media.giphy.com/media/wYyTHMm50f4Dm/giphy.gif","https://media.giphy.com/media/pLcgO003rbeo0/giphy.gif","http://giphygifs.s3.amazonaws.com/media/g69ZPJfLy7hD2/giphy.gif","https://media.giphy.com/media/26tPlltsuA89RwYww/giphy.gif","https://media.giphy.com/media/kE8bAdv1AKdSqJf2Rw/giphy.gif","http://giphygifs.s3.amazonaws.com/media/8NQ7T1ExRuMz6/giphy.gif","https://media.giphy.com/media/23BST5FQOc8k8/giphy.gif,https://media.giphy.com/media/BmmfETghGOPrW/giphy.gif", "https://media.giphy.com/media/26xBI73gWquCBBCDe/giphy.gif", "https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", "https://media.giphy.com/media/21I1WOUDnct4EmSNa6/giphy.gif", "https://media.giphy.com/media/Caey86HvbOPuPwHrsx/giphy.gif", "https://media.giphy.com/media/dJ4vNQ7r72pb4nDhN5/giphy.gif,https://media.giphy.com/media/puOukoEvH4uAw/giphy.gif", "https://media.giphy.com/media/oOTTyHRHj0HYY/giphy.gif", "https://media.giphy.com/media/CiYImHHBivpAs/giphy.gif", "https://media.giphy.com/media/g9SURfIJouBck/giphy.gif", "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif", "https://media.giphy.com/media/xL7PDV9frcudO/giphy.gif,https://media.giphy.com/media/Qakc4UBUd4jjnaDeBv/giphy.gif","https://media.giphy.com/media/xT9Igkrr14eIS3lWKI/giphy.gif","https://media.giphy.com/media/8wRy9PtdcCSXK/giphy.gif","https://media.giphy.com/media/lRiyNSnmPkP522QDjw/giphy.gif","https://cdn.discordapp.com/attachments/432469352311291906/619642564328292392/inconnu.gif ,https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif","http://giphygifs.s3.amazonaws.com/media/13CoXDiaCcCoyk/giphy.gif","https://media.giphy.com/media/Q94xQWspTUkShljj8P/giphy.gif","https://media.giphy.com/media/WXB88TeARFVvi/giphy.gif","https://media.giphy.com/media/5i7umUqAOYYEw/giphy.gif","https://media.giphy.com/media/GFHJXPCoVQEec/giphy.gif","https://media.giphy.com/media/3oEdvbAVPeVsPDQL5u/giphy.gif","https://media.giphy.com/media/Nm8ZPAGOwZUQM/giphy.gif","https://media.giphy.com/media/QyJ0We4GHpjBa7PvKL/giphy.gif","https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif","https://media.giphy.com/media/NjevnbNiUmeLm/giphy.gif","https://media.giphy.com/media/cuPm4p4pClZVC/giphy.gif","http://giphygifs.s3.amazonaws.com/media/nR4L10XlJcSeQ/giphy.gif","https://media.giphy.com/media/jRlP4zbERYW5HoCLvX/giphy.gif, https://cdn.discordapp.com/attachments/432469352311291906/619909184195919883/image0.gif", "https://cdn.discordapp.com/attachments/432469352311291906/619909522827378704/image0.gif"]
    thisone = random.choice(gif)
    await ctx.send(str(thisone))

# commande pour... Hey salut mec !
@bot.command()
async def slt(ctx):
    slt=["https://media.giphy.com/media/WsLQQA9IQC9nqkCfrE/giphy.gif","https://media.giphy.com/media/1rRRLznkmlP3WdutGJ/giphy.gif","https://media.giphy.com/media/XbD6gChlrd8S8500Ef/giphy.gif","https://media.giphy.com/media/kW8mnYSNkUYKc/giphy.gif","https://media.giphy.com/media/IThjAlJnD9WNO/giphy.gif","https://media.giphy.com/media/11Wf3llSqbkgko/giphy.gif","https://media.giphy.com/media/3oKIPsx2VAYAgEHC12/giphy.gif","https://media.giphy.com/media/LiOS57ojyxAGc/giphy.gif","https://media.giphy.com/media/3o6Ztl7oraKm4ZJ9mw/giphy.gif"]
    thisone = random.choice(slt)
    await ctx.send(thisone)

# commande pour montrer un gif salé
@bot.command()
async def salt(ctx):
    salt=["https://media.giphy.com/media/eP1Ru8yP9lDTa/giphy.gif","https://media.giphy.com/media/zSJsBKGkoQBHy/giphy.gif","https://media.giphy.com/media/dRgcwKJaGgWgo/giphy.gif","https://media.giphy.com/media/13EjnL7RwHmA2Q/giphy.gif","https://media.giphy.com/media/2vmho5c3fKQ2I8yc7v/giphy.gif","https://media.giphy.com/media/3oKIPf1BaBDILVxbYA/giphy.gif","https://media.giphy.com/media/9JcMdbuGdV32fkswuR/giphy.gif","https://media.giphy.com/media/3o7P4F86TAI9Kz7XYk/giphy.gif","https://cdn.discordapp.com/attachments/432469352311291906/619909184195919883/image0.gif", "https://cdn.discordapp.com/attachments/432469352311291906/619909522827378704/image0.gif"]
    thisone = random.choice(salt)
    await ctx.send(str(thisone))
    
# commande... Mais ta geule !
@bot.command()
async def tg(ctx):
    try: 
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("/root/bot/tg.mp3"), after=lambda e: print ('done', e))
        await asyncio.sleep(10)
        await vc.disconnect()
    except Exception as e:
        print(str(e))

# commande de chien pas content
@bot.command()
async def ouaf_angry(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("/root/bot/ouaf_angry.mp3"), after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await vc.disconnect()
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))
        
# commande... Nani !?
@bot.command()
async def nani(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("/root/bot/nani.mp3"), after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await vc.disconnect()
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))
        
# commande... Mais oui c'est clair !
@bot.command()
async def maisoui(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("/root/bot/maisoui.mp3"), after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await vc.disconnect()
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))

# commande d'aboiement
@bot.command()
async def ouaf(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("/root/bot/chien.mp3"), after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await vc.disconnect()
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))
        
# commande de chat pas content
@bot.command()
async def miaou_angry(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("/root/bot/miaou_angry.mp3"), after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await vc.disconnect()
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))


# simple commande ping
@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping =  round(ping_ * 1000)
    await ctx.send("pong (envoyé avec "+str(ping)+"ms en temps de réponse)")

# commande pour montrer des gif de chat
@bot.command()
async def cat(ctx):
    chats=["https://media.giphy.com/media/4iqMzLtBO9KSY/giphy.gif","https://media.giphy.com/media/U7JM6ChJMrFnXfFHvE/giphy.gif","https://media.giphy.com/media/Zx1ZEctOOvxK5VCwwE/giphy.gif","https://media.giphy.com/media/2A75RyXVzzSI2bx4Gj/giphy.gif","https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif","http://giphygifs.s3.amazonaws.com/media/13CoXDiaCcCoyk/giphy.gif","https://media.giphy.com/media/Q94xQWspTUkShljj8P/giphy.gif","https://media.giphy.com/media/WXB88TeARFVvi/giphy.gif","https://media.giphy.com/media/5i7umUqAOYYEw/giphy.gif","https://media.giphy.com/media/GFHJXPCoVQEec/giphy.gif","https://media.giphy.com/media/3oEdvbAVPeVsPDQL5u/giphy.gif","https://media.giphy.com/media/Nm8ZPAGOwZUQM/giphy.gif","https://media.giphy.com/media/QyJ0We4GHpjBa7PvKL/giphy.gif","https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif","https://media.giphy.com/media/NjevnbNiUmeLm/giphy.gif","https://media.giphy.com/media/cuPm4p4pClZVC/giphy.gif","http://giphygifs.s3.amazonaws.com/media/nR4L10XlJcSeQ/giphy.gif","https://media.giphy.com/media/jRlP4zbERYW5HoCLvX/giphy.gif"]
    thisone = random.choice(chats)
    await ctx.send(str(thisone))
    
# commande pour montrer des gif de chien
@bot.command()
async def dog(ctx):
	chiens=["https://media.giphy.com/media/yRUn8Y8yAYRW0/giphy.gif","https://media.giphy.com/media/npSf214982ig8/giphy.gif","https://media.giphy.com/media/Qakc4UBUd4jjnaDeBv/giphy.gif","https://media.giphy.com/media/xT9Igkrr14eIS3lWKI/giphy.gif","https://media.giphy.com/media/8wRy9PtdcCSXK/giphy.gif","https://media.giphy.com/media/lRiyNSnmPkP522QDjw/giphy.gif","https://cdn.discordapp.com/attachments/432469352311291906/619642564328292392/inconnu.gif"]
	thisone = random.choice(chiens)
	await ctx.send(str(thisone))
	
# commande pour montrer de gif de What ?
@bot.command()
async def what(ctx):
    whats =["https://media.giphy.com/media/puOukoEvH4uAw/giphy.gif", "https://media.giphy.com/media/oOTTyHRHj0HYY/giphy.gif", "https://media.giphy.com/media/CiYImHHBivpAs/giphy.gif", "https://media.giphy.com/media/g9SURfIJouBck/giphy.gif", "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif", "https://media.giphy.com/media/xL7PDV9frcudO/giphy.gif"]
    thisone = random.choice(whats)
    await ctx.send(str(thisone))
    
# commande pour montrer des gif de réfléxion
@bot.command()
async def think(ctx):
    thinks =["https://media.giphy.com/media/hJcpKgX96n7Q4/giphy.gif","https://media.giphy.com/media/XfoxinPB1fAWI/giphy.gif","https://media.giphy.com/media/777Aby0ZetYE8/giphy.gif","https://media.giphy.com/media/2H67VmB5UEBmU/giphy.gif","https://media.giphy.com/media/BmmfETghGOPrW/giphy.gif", "https://media.giphy.com/media/26xBI73gWquCBBCDe/giphy.gif", "https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", "https://media.giphy.com/media/21I1WOUDnct4EmSNa6/giphy.gif", "https://media.giphy.com/media/Caey86HvbOPuPwHrsx/giphy.gif", "https://media.giphy.com/media/dJ4vNQ7r72pb4nDhN5/giphy.gif"]
    thisone = random.choice(thinks)
    await ctx.send(str(thisone))
    
#commande pour montrer des gif de yes
@bot.command()
async def yes(ctx):
    yes = ["https://cdn.discordapp.com/attachments/620021478569672704/620022300405792798/inconnu.gif","https://media.giphy.com/media/yFs12GkGa4Cpq/giphy.gif","http://giphygifs.s3.amazonaws.com/media/nFjDu1LjEADh6/giphy.gif","https://media.giphy.com/media/WQr2txk5iEYUS6Kv3d/giphy.gif","http://giphygifs.s3.amazonaws.com/media/NEvPzZ8bd1V4Y/giphy.gif","https://media.giphy.com/media/10Jpr9KSaXLchW/giphy.gif","https://media.giphy.com/media/oGO1MPNUVbbk4/giphy.gif"]
    thisone = random.choice(yes)
    await ctx.send(str(thisone))
    
# commande pour montrer des gif de no
@bot.command()
async def no(ctx):
    nos = ["http://giphygifs.s3.amazonaws.com/media/12XMGIWtrHBl5e/giphy.gif","https://media.giphy.com/media/eKrgVyZ7zLvJrgZNZn/giphy.gif","https://media.giphy.com/media/wYyTHMm50f4Dm/giphy.gif","https://media.giphy.com/media/pLcgO003rbeo0/giphy.gif","http://giphygifs.s3.amazonaws.com/media/g69ZPJfLy7hD2/giphy.gif","https://media.giphy.com/media/26tPlltsuA89RwYww/giphy.gif","https://media.giphy.com/media/kE8bAdv1AKdSqJf2Rw/giphy.gif","http://giphygifs.s3.amazonaws.com/media/8NQ7T1ExRuMz6/giphy.gif","https://media.giphy.com/media/23BST5FQOc8k8/giphy.gif"]
    thisone = random.choice(nos)
    await ctx.send(str(thisone))
    
# commande pour montrer des gif de hacker
@bot.command()
async def hacker(ctx):
    hackers = ["https://cdn.discordapp.com/attachments/620021478569672704/620022426243432470/inconnu.gif,https://cdn.discordapp.com/attachments/620021478569672704/620022494413324288/inconnu.gif,https://media.giphy.com/media/YQitE4YNQNahy/giphy.gif","https://media.giphy.com/media/UqxVRm1IaaIGk/giphy.gif","https://media.giphy.com/media/TOWeGr70V2R1K/giphy.gif","https://media.giphy.com/media/ZvLUtG6BZkBi0/giphy.gif","https://media.giphy.com/media/QNFhOolVeCzPQ2Mx85/giphy.gif","https://media.giphy.com/media/VbAFrrDVGAvZu/giphy.gif","https://media.giphy.com/media/Wsju5zAb5kcOfxJV9i/giphy.gif","http://giphygifs.s3.amazonaws.com/media/rMS1sUPhv95f2/giphy.gif","https://media.giphy.com/media/3oriNLx3dUqFgVi86I/giphy.gif","https://media.giphy.com/media/9kSM4y028LvvW/giphy.gif","http://giphygifs.s3.amazonaws.com/media/eCqFYAVjjDksg/giphy.gif","https://media.giphy.com/media/eDmCKa8Wd3MUU/giphy.gif","https://media.giphy.com/media/13UZisxBxkjPwI/giphy.gif","https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif"]
    thisone = random.choice(hackers)
    await ctx.send(str(thisone))

# commande qui fait s'excuser le bot
@bot.command()
async def excusetoi(ctx):
    await ctx.send("Pardon :(")
    
# commande déclinant l'identité du bot
@bot.command()
async def tki(ctx):
	await ctx.send('Je suis ton père.')
	
# commande qui envoie le lien vers une calculatrice
@bot.command()
async def calc(ctx):
    await ctx.send("https://fr.calcuworld.com/calculs-mathematiques/calculatrice-scientifique/")
	
# commande de multiplication entre 2 nombres
@bot.command()
async def multi(ctx, a:int,b:int):
    await ctx.send(a*b)
    
# commande d'addition entre 2 nombres
@bot.command()
async def add(ctx, a:int,b:int):
    await ctx.send(a+b)

# commande d'addition entre 2 nombres
@bot.command()
async def sou(ctx, a:int,b:int):
    await ctx.send(a-b)
    
# commande d'addition entre 2 nombres
@bot.command()
async def div(ctx, a:int,b:int):
    await ctx.send(a/b)

# commande de sortie - previent du depart d'un utilisateur
@bot.event
async def on_member_remove(member):
    try:
        print(str(member)+"has quit")
        my_logger.debug('Discorbot : '+str(member)+"has quit")
        channel = member.guild.text_channels[1]
        await channel.send(str(member)+" a quitté le serveur.")
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))

#commandnde de modération

try:
    bot.run('TOKEN')
except KeyboardInterrupt:
        print("\n\n************************************\n\n")
