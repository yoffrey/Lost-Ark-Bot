# bot.py
import os
import discord

from dotenv import load_dotenv

load_dotenv()
bot = os.getenv('TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

verify = False
commandList = ['/add', '/del', '/check', '/p']
ticketList = ['plat', 'cube', 'map', 'boss']
tierList = ['t1', 't2', 't3']
userID = {}

ticketsDict = {
	'plat' : {},
	'cube' : {'t1':{}, 't2':{}, 't3':{}},
	'map' : {'t1':{}, 't2':{}, 't3':{}},
	'boss' : {'t2':{}, 't3':{}}
}

def pingUser(ticketName, tier):
	ticket = ticketsDict[ticketName]
	if tier:
		msg = 'Awakened Arkers with {} {} tickets\n'.format(tier, ticketName)
		for user in ticket[tier]:
			msg += '- <@{}> : {}\n'.format(userID[user], str(ticket[tier][user]))
	else:
		msg = 'Awakened Arkers with {} tickets\n'.format(ticketName)
		for user in ticket:
			msg += '- <@{}> : {}\n'.format(userID[user], str(ticket[user]))
	return msg

def checkCount(ticketName, tier):
	ticket = ticketsDict[ticketName]
	if tier:
		msg = 'Awakened Arkers with {} {} tickets\n'.format(tier, ticketName)
		for user in ticket[tier]:
				msg += '- {} : {}\n'.format(user, str(ticket[tier][user]))            
	else:
		msg = 'Awakened Arkers with {} tickets\n'.format(ticketName)
		for user in ticket:
			msg += '- {} : {}\n'.format(user, str(ticket[user]))
	return msg

def addTicket(ticketName, name, ticketAmount, tier=''):
	ticket = ticketsDict[ticketName]
	if tier:
		if tier not in tierList:
			return
		#add case not plat
		if name not in ticket[tier]:
			ticket[tier][name] = ticketAmount
		else:
			ticket[tier][name] += ticketAmount
	else:
		#add case plat
		if name not in ticket:
			ticket[name] = ticketAmount
		else:
			ticket[name] += ticketAmount
	return checkCount(ticketName, tier)

def delTicket(ticketName, name, ticketAmount, tier=''):
	ticket = ticketsDict[ticketName]
	if tier:
		if tier not in tierList:
			return
		#add case not plat
		if name in ticket[tier]:
			ticket[tier][name] -= ticketAmount
		if ticket[tier][name] == 0:
			del ticket[tier][name]
	else:
		#add case plat
		if name in ticket:
			ticket[name] -= ticketAmount
		if ticket[name] == 0:
			del ticket[name]

@client.event
async def on_ready():
	print ('Lost Ark bot is now running!\n')
    
	#Get user data for all Lost Ark role/admin
	#for member with lostark role or admin
	#populate the userID dict
	for guild in client.guilds:
		for member in guild.members: 
			userID[member.name] = member.id

	file = open('users.txt', 'w')
	file.write(str(userID))
	file.close

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	#Split message, get and store name in a dictionary with userID
	contentTokens= message.content.split()
	name = message.author.name
	userID[name] = message.author.id
	if contentTokens[-1].isdigit():
		ticketAmount = int(contentTokens[-1])
		del contentTokens[-1]
	else:
		ticketAmount = 1
	#assign variables    
	if contentTokens[0] not in commandList:
		return
	command = contentTokens[0]
	if contentTokens[-1].lower() in str(userID.keys()).lower():
		userIDList = list(userID)
		userIDListLower = [x.lower() for x in userID.keys()]
		#if lowercase matches, name = the one stored in userID for case
		name = userIDList[userIDListLower.index(contentTokens[-1].lower())]
		if contentTokens[-2] in ticketList:
			ticketName = contentTokens[-2]
			if contentTokens[-3] in tierList:
				tier = contentTokens[-3]
			else:
				tier = ''
		else:
			return
	elif contentTokens[-1] in ticketList:
		ticketName = contentTokens[-1]
		if contentTokens[-2] in tierList:
			tier = contentTokens[-2]
		else:
			tier = ''
	else:
		return
	#if ticket is plat and has a tier then return
	if (ticketName == 'plat') and tier:
		return

    #Process the command
	msg = ''
	if ticketName == 'plat':
		tier = None 
	if command == '/add':
		msg = addTicket(ticketName, name, ticketAmount, tier)
	if command == '/del':
		delTicket(ticketName, name, ticketAmount, tier)
	if command == '/check':
		msg = checkCount(ticketName, tier)
	if command == '/p':
		msg = pingUser(ticketName, tier)
        
    #Verify the message was processed by reacting to it    
	verify = True
	if verify:
		emoji = '\U0001F3AB'
		await message.add_reaction(emoji)
		verify = False

	if msg:
		await message.channel.send(msg)

    #save dict to a text file
	file = open('log.txt', 'w')
	file.write(str(ticketsDict))
	file.close

client.run(bot)
