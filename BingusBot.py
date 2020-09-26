import discord, re, random

client = discord.Client()
keywords = ["!bingus"]
TOKEN = ''
bingus_list = ["https://media.tenor.com/images/8e49bb7796692a102487cdb996323982/tenor.gif",
              "https://kittentoob.com/wp-content/uploads/2017/12/Hairless-Cats-3.jpg",
              "https://static.boredpanda.com/blog/wp-content/uploads/2020/03/89436950_1090410697992892_8878057772038512233_n-5e811f85444a3__700.jpg",
              "https://media.tenor.com/images/bd64a9f309f70c283d8757cc0f102923/tenor.gif","https://www.thesun.co.uk/wp-content/uploads/2020/03/NINTCHDBPICT000569488664.jpg?strip=all&w=960"]

@client.event
async def on_message(message):
    if (message.content.find("!bingus") >= 0):
        number_of_images_data = int(re.search(r'\d+', message.content).group())
        if number_of_images_data > 5:
            await message.channel.send("Sorry, won't send more than 5 images at a time.")
        else:
            print("Requested amount of images: " + str(number_of_images_data))
            for j in range (number_of_images_data):
                bingus_image = random.choice(bingus_list)
                await message.channel.send(bingus_image)
    else:
        print("")
print("BingusBot is online!")
client.run(TOKEN)
