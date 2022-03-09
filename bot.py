# bot.py
import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

commandList = ['/add', '/del', '/check']
ticketList = ['plat', 'cube', 'map', 'boss']
tierList = ['t1', 't2', 't3']

userID = {}

ticketsDict= {
    'plat' : {},
    'cube' : {'t1':{}, 't2':{}, 't3':{}},
    'map' : {'t1':{}, 't2':{}, 't3':{}},
    'boss' : {'t2':{}, 't3':{}}
}

def checkCount(ticketName, tier, count=4):
    msg = ''
    ticket = ticketsDict[ticketName]
    if tier:
        if len(ticket[tier]) >= count:
            msg = 'Awakened Arkers with {} {} tickets\n'.format(tier, ticketName)
            for user in ticket[tier]:
                if len(ticket[tier]) < 4:
                    msg += '{}\n'.format(user)
                else:
                    msg += '<@{}>\n'.format(userID[user])
    else:
        if len(ticket) >= count:
            msg = 'Awakened Arkers with {} tickets\n'.format(ticketName)
            for user in ticket:
                if len(ticket) < 4:
                    msg += '{}\n'.format(user)
                else:
                    msg += '<@{}>\n'.format(userID[user])
    return msg

def addTicket(ticketName, name, tier=''):
    ticket = ticketsDict[ticketName]
    if tier:
        if tier not in tierList:
            return
        #add case not plat
        if name not in ticket[tier]:
            ticket[tier][name] = 1
        else:
            ticket[tier][name] += 1
    else:
        #add case plat
        if name not in ticket:
            ticket[name] = 1
        else:
            ticket[name] += 1
    return checkCount(ticketName, tier)

def delTicket(ticketName, name, tier=''):
    ticket = ticketsDict[ticketName]
    if tier:
        if tier not in tierList:
            return
        #add case not plat
        if name in ticket[tier]:
            ticket[tier][name] -= 1
        if ticket[tier][name] == 0:
            del ticket[tier][name]
    else:
        #add case plat
        if name in ticket:
            ticket[name] -= 1 
        if ticket[name] == 0:
            del ticket[name]
        
@client.event
async def on_ready():
    print ('Lost Ark bot is now running!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    contentTokens= message.content.split()
    name = message.author.name

    userID[name] = message.author.id
    
    if len(contentTokens) > 3:
        return

    command = contentTokens[0] 
    ticketName = contentTokens[1] 
    
    if not (command in commandList and ticketName in ticketList):
        return

    msg = ''
    tier = None if ticketName == 'plat' else contentTokens[2]
    if command == '/add':
        msg = addTicket(ticketName, name, tier)
    
    if command == '/del':
        delTicket(ticketName, name, tier)

    if command == '/check':
        print(tier)
        msg = checkCount(ticketName, tier, count=0)
    
    if msg:
        await message.channel.send(msg)

client.run(TOKEN)
