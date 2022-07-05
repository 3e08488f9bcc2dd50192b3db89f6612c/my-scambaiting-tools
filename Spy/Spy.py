import discord
import os
import ctypes
import datetime
import sys
from discord.ext import commands
from discord.utils import get
from tkinter import *

async def sendCommands():
    window = Tk()

    input_user = StringVar()
    input_field = Entry(window, text=input_user)
    input_field.pack(side=BOTTOM, fill=X)

    async def enter_pressed(event):
        input_get = input_field.get()
        if input_get == "!help":
            label = Label(frame, text="Available commands:\n!help - show all commands.\n!find [user] - check if user is in the server.\n!sendmessage [channel] [message] - send message in specific channel.\n!info [user] - get information about user.\n!clearlog - delete SpyLog.txt\n!stop - stop the bot.", anchor='w').pack(fill='both')
            input_user.set('')
        elif input_get == "!clearlog":
            if os.path.exists("Spy-Log.log"):
                os.remove("Spy-Log.log")
                label = Label(frame, text="[+] Successfull.", anchor='w').pack(fill='both')
            else:
                label = Label(frame, text="[+] Failed.", anchor='w').pack(fill='both')
            input_user.set('')
        elif input_get == "!stop":
            await bot.close()
            label = Label(frame, text="[+] Successfull.", anchor='w').pack(fill='both')
            input_user.set('')
        else:
            label = Label(frame, text="Invalid Command, try write !help for see all commands", anchor='w').pack(fill='both')
            input_user.set('')

    frame = Frame(window, width=500, height=300)
    frame.pack_propagate(False)
    r1 = enter_pressed
    input_field.bind("<Return>", await r1)
    frame.pack()
    window.mainloop()
        

#bot = commands.Bot(command_prefix='!')
bot = discord.AutoShardedClient(fetch_offline_members=False)
#TOKEN = input('Discord Token: ')
TOKEN = 'JawySjii4y2c1AAf65-qvkpfmgqfa0CEgxOKa6BlhJ1Mh8NDn3w1377JxWO-lXsok0Lv'

# System
@bot.event
async def on_ready():
    os.system('cls')
    print('[+] \x1b[6;30;42m' + 'Successfull Connected!' + '\x1b[0m')
    ctypes.windll.kernel32.SetConsoleTitleW("| Program Version: 1.51 | Name: "+bot.user.name+" | ID: "+str(int(bot.user.id))+" | Activity: "+str(bot.activity)+" | TOKEN: "+str(TOKEN)+"  | Total Servers: "+str(len(bot.guilds))+" | Total Bots: "+str(len(bot.users))+" :|") #
    await sendCommands()
    
# Spying (Member Events)
@bot.event
async def on_member_join(member):
    WHITE = '\33[37m'
    YELLOW = '\33[33m'
    RED = '\33[31m'
    BOLT = '\33[1m'
    print(BOLT+'\33[92m' + '['+str(member.joined_at)+'] '+WHITE+' '+'The member: '+YELLOW+' '+''+str(member.name)+' '+WHITE+' '+'is invited to '+RED+''+''+str(member.guild)+' '+''+WHITE+'.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(member.joined_at)+'] The member '+str(member.name)+' is invited to '+str(member.guild)+'.\n')
        file.close()

@bot.event
async def on_member_remove(member):
    WHITE = '\33[37m'
    YELLOW = '\33[33m'
    RED = '\33[31m'
    BOLT = '\33[1m'
    time = datetime.datetime.now()
    print(BOLT+'\33[92m' + '['+str(time)+'] '+WHITE+' '+'The member: '+YELLOW+' '+''+member.name+' '+WHITE+' '+'has leaved from '+RED+''+''+str(member.guild)+' '+''+WHITE+'.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] The member '+member.name+' has leaved from '+str(member.guild)+'.\n')
        file.close()

@bot.event
async def on_member_ban(member):
    WHITE = '\33[37m'
    YELLOW = '\33[33m'
    RED = '\33[31m'
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    print(BOLT+'\33[92m' + '['+str(time)+'] '+WHITE+' '+'The member: '+YELLOW+' '+''+member.name+' '+WHITE+' '+'has been banned from '+RED+' '+''+str(member.guild))
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] The member '+member.name+' has been banned from '+str(member.guild)+'.\n')
        file.close()
  
@bot.event
async def on_member_unban(member):
    await member.guild.unban(member)
    WHITE = '\33[37m'
    YELLOW = '\33[33m'
    RED = '\33[31m'
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    print(BOLT+'\33[92m' + '['+str(time)+'] '+WHITE+' '+'The member: '+YELLOW+' '+''+member.name+' '+WHITE+' '+'has been unbanned from '+RED+' '+''+str(member.guild))
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] The member '+member.name+' has been unbanned from '+str(member.guild)+'.\n')
        file.close()
    
@bot.event
async def on_user_update(before,after):
    pass
    
    
# Spying (Message Events)
@bot.event
async def on_message(message):
    WHITE = '\33[37m'
    YELLOW = '\33[33m'
    RED = '\33[31m'
    VIOLET = '\33[35m'
    WWW = '\33[31m'
    channel_id = message.channel.id
    channel = bot.get_channel(channel_id)
    author = message.author
    content = message.content
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+''+' '+str(author)+' ('+str(message.author.id)+')'+WHITE+' '+'has send message'+VIOLET+''+' '+str(content)+' / (ID: '+str(message.id)+') '+WHITE+' '+'in (#'+str(channel)+' / '+str(channel_id)+'). Discord Server:  '+WWW+' ['+str(message.guild)+' / '+str(message.guild.id)+']'+WHITE+'.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] '+str(author)+' ('+str(message.author.id)+') has send message / '+str(content)+' (ID: '+str(message.id)+') in ('+str(channel)+' / '+str(channel_id)+') Discord Server: ['+str(message.guild)+'].\n')     
        file.close()
     
@bot.event
async def on_message_delete(message):
    WHITE = '\33[37m'
    YELLOW = '\33[33m'
    RED = '\33[31m'
    VIOLET = '\33[35m'
    BLUE = '\33[34m'
    WWW = '\33[31m'
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+' '+''+str(message.author)+' ('+str(message.author.id)+')'+WHITE+' '+'has deleted message / (ID: '+str(message.id)+') '+VIOLET+' '+''+str(message.content)+''+WHITE+' '+' in '+BLUE+' '+'(#'+str(message.channel)+' / '+str(message.channel.id)+')'+WHITE+'. Discord Server: '+WWW+' ['+str(message.guild)+' / '+str(message.guild.id)+'] '+WHITE+'.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] '+str(message.author)+' ('+str(message.author.id)+') has deleted message / '+str(message.content)+' (ID: '+str(message.id)+') in ('+str(message.channel)+' / '+str(message.channel.id)+') Discord Server: ['+str(message.guild)+' / '+str(message.guild.id)+'].\n')
        file.close()
        
@bot.event
async def on_raw_message_delete(payload):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+str(payload)+' (Deleted)')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+']'+str(payload)+' (Deleted)\n') 
        file.close()

@bot.event
async def on_raw_message_edit(payload):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+str(payload)+' (Edited)')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+']'+str(payload)+' (Edited)\n') 
        file.close()
        
@bot.event
async def on_message_edit(before,after):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+str(before)+BLUE+str(after))
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] The message before: '+str(before)+'" has been edited to: ['+str(after)+'].\n') 
        file.close()

#Spying (Reactions Events)
@bot.event
async def on_reaction_add(reaction,user):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+' '+str(user)+'"s reaction: ['+str(reaction)+'] was added.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] '+str(user)+'"s reaction: ['+str(reaction)+'] was added.\n') 
        file.close()

@bot.event
async def on_reaction_remove(reaction,user):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+' '+str(user)+'"s reaction: ['+str(reaction)+'] was removed.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] '+str(user)+'"s reaction: ['+str(reaction)+'] was removed.\n') 
        file.close()

#Spying (Guild Events)
@bot.event
async def on_guild_channel_create(channel):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+' Channel with name: #'+str(channel)+' was created.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] Channel with name: #'+str(channel)+' was created.\n') 
        file.close()

@bot.event
async def on_guild_channel_delete(channel):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+' Channel with name: #'+str(channel)+' was deleted.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] Channel with name: #'+str(channel)+' was deleted.\n') 
        file.close()

@bot.event
async def on_guild_role_create(role):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+' Role with name: '+str(role)+' was created.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] Role with name: '+str(role)+' was created.\n') 
        file.close()

@bot.event
async def on_guild_role_delete(role):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+' Role with name: '+str(role)+' was deleted.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] Role with name: '+str(role)+' was deleted.\n') 
        file.close()

@bot.event
async def on_invite_create(invite):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+' Invite: '+str(invite)+' was created.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] Invite '+str(invite)+' was created.\n') 
        file.close()

@bot.event
async def on_invite_delete(invite):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    print(BOLT+'\33[92m' + '['+str(time)+']'+YELLOW+' Invite: '+str(invite)+' was deleted.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] Invite '+str(invite)+' was deleted.\n') 
        file.close()

@bot.event
async def on_socket_raw_send(payload):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    YELLOW = '\33[33m'
    #print(BOLT+'\33[92m' + '['+str(time)+'] '+YELLOW+str(payload)+' (WebSocket)')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] '+str(payload)+' (WebSocket)\n') 
        file.close()

@bot.event
async def on_private_channel_delete(channel):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    print(BOLT+'\33[92m'+ '['+str(time)+']'+str(channel)+' was deleted (private).')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] '+str(channel)+' was deleted (private).') 
        file.close()
        
@bot.event
async def on_private_channel_create(channel):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    print(BOLT+'\33[92m'+ '['+str(time)+']'+str(channel)+' was created (private).')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] '+str(channel)+' was created (private).') 
        file.close()

@bot.event
async def on_private_channel_update(before,after):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    print(BOLT+'\33[92m'+ '['+str(time)+'] The channel before: '+str(before)+' now to '+str(after)+' (private).')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] The channel before: '+str(before)+' now to '+str(after)+' (private).') 
        file.close()

# Spying (Typing)
@bot.event
async def on_typing(channel, user, when):
    time = datetime.datetime.now()
    BOLT = '\33[1m'
    print(BOLT+'\33[92m'+ '['+str(time)+']'+str(user)+' start typing text in:'+str(channel)+' at '+str(when)+'.')
    with open('Spy-Log.log', 'a', encoding='utf-8') as file:
        file.write('['+str(time)+'] '+str(when)+' ( '+str(user)+') start typing text in: '+str(channel)+'.') 
        file.close()
        
try:
    bot.run(TOKEN, bot=False)
except:
    BOLT = '\33[1m'
    RED = '\33[31m'
    WHITE = '\33[37m'
    print(BOLT+'['+RED+'-'+WHITE+'] The token is invalid ('+TOKEN+')')
    os.system('pause')