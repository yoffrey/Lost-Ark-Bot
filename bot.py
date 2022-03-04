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
        d[name] = dec
        if dec <= 0:
            d.pop(name)

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

    elif message.content.startswith('/add t2 boss'):
        ticket = 'T2 Boss Rush'
        add(bosst2, name)
        count = bosst2[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(bosst2) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in bosst2:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add t3 boss'):
        ticket = 'T3 Boss Rush'
        add(bosst3, name)
        count = bosst3[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(bosst3) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in bosst3:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add t1 cube'):
        ticket = 'T1 Cube'
        add(cubet1, name)
        count = cubet1[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(cubet1) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in cubet1:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add t2 cube'):
        ticket = 'T2 Cube'
        add(cubet2, name)
        count = cubet2[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(cubet2) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in cubet2:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add t3 cube'):
        ticket = 'T3 Cube'
        add(cubet3, name)
        count = cubet3[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(cubet3) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in cubet3:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add t1 map'):
        ticket = 'T1 Map'
        add(mapt1, name)
        count = mapt1[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(mapt1) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in mapt1:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add t2 map'):
        ticket = 'T2 Map'
        add(mapt2, name)
        count = mapt2[name]
        await message.channel.send(name + ' now has ' + str(count) +' tickets')
        if len(mapt2) >= 4:
            await message.channel.send('The following users have tickets for ' + ticket)
            for key in mapt2:
                await message.channel.send(key)
        return

    elif message.content.startswith('/add t3 map'):
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
        if name in plat:
            count = plat[name]
            await message.channel.send(name + ' has ' + str(count) + ' ' + ticket + ' tickets!' )
        else:
            await message.channel.send(name + ' has 0 tickets!')
    
    elif message.content.startswith('/rmv t2 boss'):
        ticket = 'T2 Boss Rush'
        if name not in bosst2:
            await message.channel.send(name + ' did not have any ' + ticket + ' tickets.')
            return
        sub(bosst2, name)
        if name in bosst2:
            count = bosst2[name]
            await message.channel.send(name + ' has ' + str(count) + ' ' + ticket + ' tickets!' )
        else:
            await message.channel.send(name + ' has 0 tickets!')
    
    elif message.content.startswith('/rmv t3 boss'):
        ticket = 'T3 Boss Rush'
        if name not in bosst3:
            await message.channel.send(name + ' did not have any ' + ticket + ' tickets.')
            return
        sub(bosst3, name)
        if name in bosst3:
            count = bosst3[name]
            await message.channel.send(name + ' has ' + str(count) + ' ' + ticket + ' tickets!' )
        else:
            await message.channel.send(name + ' has 0 tickets!')

    elif message.content.startswith('/rmv t1 cube'):
        ticket = 'T1 Cube'
        if name not in cubet1:
            await message.channel.send(name + ' did not have any ' + ticket + ' tickets.')
            return
        sub(cubet1, name)
        if name in cubet1:
            count = cubet1[name]
            await message.channel.send(name + ' has ' + str(count) + ' ' + ticket + ' tickets!' )
        else:
            await message.channel.send(name + ' has 0 tickets!')

    elif message.content.startswith('/rmv t2 cube'):
        ticket = 'T2 Cube'
        if name not in cubet2:
            await message.channel.send(name + ' did not have any ' + ticket + ' tickets.')
            return
        sub(cubet2, name)
        if name in cubet2:
            count = cubet2[name]
            await message.channel.send(name + ' has ' + str(count) + ' ' + ticket + ' tickets!' )
        else:
            await message.channel.send(name + ' has 0 tickets!')

    elif message.content.startswith('/rmv t3 cube'):
        ticket = 'T3 Cube'
        if name not in cubet3:
            await message.channel.send(name + ' did not have any ' + ticket + ' tickets.')
            return
        sub(cubet3, name)
        if name in cubet3:
            count = cubet3[name]
            await message.channel.send(name + ' has ' + str(count) + ' ' + ticket + ' tickets!' )
        else:
            await message.channel.send(name + ' has 0 tickets!')

    elif message.content.startswith('/rmv t1 map'):
        ticket = 'T1 Map'
        if name not in mapt1:
            await message.channel.send(name + ' did not have any ' + ticket + ' tickets.')
            return
        sub(mapt1, name)
        if name in mapt1:
            count = mapt1[name]
            await message.channel.send(name + ' has ' + str(count) + ' ' + ticket + ' tickets!' )
        else:
            await message.channel.send(name + ' has 0 tickets!')

    elif message.content.startswith('/rmv t2 map'):
        ticket = 'T2 Map'
        if name not in mapt2:
            await message.channel.send(name + ' did not have any ' + ticket + ' tickets.')
            return
        sub(mapt2, name)
        if name in mapt2:
            count = mapt2[name]
            await message.channel.send(name + ' has ' + str(count) + ' ' + ticket + ' tickets!' )
        else:
            await message.channel.send(name + ' has 0 tickets!')

    elif message.content.startswith('/rmv t3 map'):
        ticket = 'T3 Map'
        if name not in mapt3:
            await message.channel.send(name + ' did not have any ' + ticket + ' tickets.')
            return
        sub(mapt3, name)
        if name in mapt3:
            count = mapt3[name]
            await message.channel.send(name + ' has ' + str(count) + ' ' + ticket + ' tickets!' )
        else:
            await message.channel.send(name + ' has 0 tickets!')

client.run(TOKEN)