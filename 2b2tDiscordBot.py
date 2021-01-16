import discord, socket

logpath = "" # Insert Minecraft directory here with \logs\latest.log extension (Ex. 'C:\Users\lucad\AppData\Roaming\.minecraft\logs\latest.log')
botToken = "" # Insert bot token here

client = discord.Client()

@client.event
async def on_ready():
    currentHost = discord.Game("Current host: " + socket.gethostname())
    await client.change_presence(activity=currentHost)
    print("\nBot is online!\n")

@client.event
async def on_message(message):
    if message.content == ".q":
        print("User " + str(message.author) + " requested queue position.")
        queuePosition = getQueuePosition(logpath)
        if queuePosition is None:
            print("No queue position detected for " + str(message.author))
            await message.channel.send("Sorry, no queue position detected for you. Either:\n1. You're not in the 2b2t queue.\n2. Log path directory is incorrect.\n3. Log path directory is root or protected\n4. 2b2t's queue system has changed internally resulting in false negatives.")
        else:
            await sendEmbed(message, queuePosition)
    else:
        pass

def getQueuePosition(logpath):
    try:
        log = open(logpath, 'r')
        lines = log.readlines()
        for line in reversed(lines):
            line = line.strip()
            if line.find("Position in queue") != -1:
                try:
                    queuePosition = int(line[50:])
                    return queuePosition
                except:
                    print("Sorry, detected queue position is not a number. Maybe Mojang or 2b2t has changed their queue system?")
                break
            else:
                pass
    except:
        print("Sorry, couldn't open log file. Make sure the file isn't protected or in a root directory.")
    
async def sendEmbed(message, queuePosition):
    embed = discord.Embed(title="2b2t Queue for " + socket.gethostname() + ":", color=13184526)
    embed.add_field(name="Current queue position:", value=str(queuePosition))
    embed.add_field(name="Estimated time left:", value=str(queuePosition / 100) + " hours", inline=False)
    embed.set_author(name="Made by Luca Denhez on 01/06/2021")
    try:
        await message.channel.send(embed=embed)
    except:
        print("Sorry, couldn't send the embed. Maybe check your internet connection?")

client.run(botToken)
