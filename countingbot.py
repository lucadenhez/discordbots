import discord, re

botToken = ""
countingChannelID = # Integer
client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.id == countingChannelID:
        if message.author != client.user:
            if "@" not in message.content: # Workaround for bot detecting @ mentions as integers
                try:
                    currentNumber = int(message.content)
                    await message.channel.send(str(currentNumber + 1))
                except Exception as ex:
                    numbers = re.findall(r'\d+', message.content)
                    if not numbers:
                        pass
                    else:
                        numbers = str(''.join(numbers))
                        try:
                            currentNumber = int(numbers)
                            await message.channel.send(str(currentNumber + 1))
                        except Exception as ex:
                            pass

@client.event
async def on_ready():
    print("Bot online!\n")
    
client.run(botToken)
