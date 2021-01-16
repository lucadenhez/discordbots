import discord, random, re

client = discord.Client()
prefix = "!bingus"
discordToken = ""
bingusImages = ["https://media.tenor.com/images/8e49bb7796692a102487cdb996323982/tenor.gif",
              "https://kittentoob.com/wp-content/uploads/2017/12/Hairless-Cats-3.jpg",
              "https://static.boredpanda.com/blog/wp-content/uploads/2020/03/89436950_1090410697992892_8878057772038512233_n-5e811f85444a3__700.jpg",
              "https://media.tenor.com/images/bd64a9f309f70c283d8757cc0f102923/tenor.gif","https://media.tenor.com/images/fbae3e4a28aa1be0f2ae4b1ee309d1ba/tenor.gif"]

@client.event
async def on_ready():
    print("BingusBot is online!\n")

@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        quantity = re.findall(r'\d+', message.content)
        if not quantity:
            print("Sender: " + str(message.author) + " | Response: Sorry, quantity is not a number.")
        else:
            quantity = int(quantity[0])
            if quantity > 10:
                try:
                    print("Sender: " + str(message.author) + " requested more than 10 images. Requested quantity: " + str(quantity))
                    await message.channel.send("Sorry, won't send more than 10 images at a time. (You can spam it though!)")
                except:
                    print("Sorry, couldn't send the message explaining image quantity. Maybe check your internet connection or firewall rules?")
            else:
                print("Sender: " + str(message.author) + "| Number of images requested: " + str(quantity))
                for i in range(quantity):
                    try:
                        image = bingusImages[random.randint(0, len(bingusImages))]
                        await message.channel.send(image)
                    except:
                        print("Sorry, couldn't send one image. Either image url is dead and or Discord is rate-limiting the bot.")
    else:
        pass

client.run(discordToken)
