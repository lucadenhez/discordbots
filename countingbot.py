import discord, re

botToken = "ODAxODcyNTc3OTU3ODU1MjYz.YAnACA.N_hXOg-a9j5GmC_LUK7Iry-cnuA"
countingChannelID = 783541471990906881
client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.id == countingChannelID:
        if message.author != client.user:
            if "@" not in message.content: 
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
