# bot.py
import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

plat = {}
bosst2 = {}
bosst3  = {}
cubet1 = {}
cubet2 = {}
cubet3 = {}
mapt1 = {}
mapt2 = {}
mapt3  = {}

def add(d, name):
    if name not in d:
        d[name] = 1 
    else:
        inc = d.get(name)
        inc += 1
        d[name] = inc

def sub(d, name):
    if name not in d:
        return
    else:
        dec = d.get(name)
        dec -= 1
        if dec <= 0:
            return
        d[name] = dec


@client.event
async def on_ready():
    print ('Lost Ark bot is now running!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    name = message.author.name
    if message.content.startswith('/add plat'):
        ticket = 'Platinum Fields'
        add(plat, name)
        count = plat[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(plat) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in plat:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add boss t2'):
        ticket = 'T2 Boss Rush'
        add(bosst2, name)
        count = bosst2[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(bosst2) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in bosst2:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add boss t3'):
        ticket = 'T3 Boss Rush'
        add(bosst3, name)
        count = bosst3[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(bosst3) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in bosst3:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add cube t1'):
        ticket = 'T1 Cube'
        add(cubet1, name)
        count = cubet1[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(cubet1) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in cubet1:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add cube t2'):
        ticket = 'T2 Cube'
        add(cubet2, name)
        count = cubet2[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(cubet2) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in cubet2:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add cube t3'):
        ticket = 'T3 Cube'
        add(cubet3, name)
        count = cubet3[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(cubet3) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in cubet3:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add map t1'):
        ticket = 'T1 Map'
        add(mapt1, name)
        count = mapt1[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(mapt1) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in mapt1:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add map t2'):
        ticket = 'T2 Map'
        add(mapt2, name)
        count = mapt2[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(mapt2) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in mapt2:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add map t3'):
        ticket = 'T3 Map'
        add(mapt3, name)
        count = mapt3[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(mapt3) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in mapt3:
                await message.channel.send(key)
        return

    elif message.content.startswith('/rmv plat'):
        ticket = 'Platinum Fields'
        if name not in plat:
            await message.channel.send(name + ' did not have any ' + ticket + ' tickets.')
            return
        sub(plat, name)
        count = plat[name]
        await message.channel.send(name + ' has ' + str(count) + ticket + ' tickets!' )

client.run(TOKEN)