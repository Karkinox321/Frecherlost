import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Bot Started")


serverstatus = "online"


@client.event
async def on_ready():
    print("Bot Started")
    if serverstatus == "Offline":
        await client.change_presence(activity=discord.Game("Wartungsarbeiten [> Unknown "), status=discord.Status.idle)
    else:
        await client.change_presence(activity=discord.Game("payen for Support"), status=discord.Status.online)


@client.event
async def on_message(message):
    global tog2, tog3, tog1, warn
    if message.author.bot:
        return

    if serverstatus == "Offline":
        return


@client.event
async def on_message(message):
    if "%test" in message.content:
            await  message.delete()
            embed = discord.Embed(title="**Info Admin **",
                                  description="hey, das sind die infos zu den Admins\n\r"
                                              f" @===🦋Admin🦋==== = Das ist Karkinox(der chef vom server)\n"
                                              f" @===🔥Die cooolen🔥=== = Das sind die coolen die Karkinox sehr mag\n"
                                              f" @=====😺my Friend😺===== = das sind die freunde (DC) von Karkinox",
                                  colour=discord.Colour.blue())
            await message.channel.send(embed=embed)

    if "%help" in message.content:
        if message.author == "Karkinox#5126":
            await  message.delete()
            embed = discord.Embed(title="**Hilfe**")


    if "%bannoff" in message.content:
        if message.author == "Nigolou#9363" or "Karkinox#5126":
            await  message.delete()
            embed = discord.Embed(title="**Verwarnung !**",
                                  description= "hey, sie haben eine Warnung\n\r"
                                                  f"Wegen eines Regelbruches haben sie nun eine Warnung bekommen !\n"
                                                  f"Sie haben nun noch 1 Verwarnung(en)**. \n\r"
                                                  f"Bei 3 oder mehr Verwarnungen wird der Serverowner benachrichtigt !",
                                      colour=discord.Colour.red())
            await message.channel.send(embed=embed)


    if "%commands" in message.content:
        if message.author == "Nigolou#9363" or "Karkinox#5126":
            await message.delete()                                      #Das alle commands mir angezeigt werden
            embed = discord.Embed(title="**```Commands```**",
                                  description=" ``%info`` = Information zum bot.\n\r"
                                              "``%funbann ``= einfach aus lange weile ein spaß bann machen.\n\r"
                                              " ``%bannoff ``= wenn jemmand misst baut oder beleidigt.\n\r"
                                              "**Von @Karkinox programmiert**",
                                  color=discord.Colour.blue())
            await message.author.send(embed=embed)

    if "%info" in message.content:
        await message.delete()
        embed = discord.Embed(title="**```Informationen```**",
                              description="Dieser Discord Bot ist für die Moderation und Adminstration gedacht."
                                          "Der Bot kann verschiedene Beleidigungen, mit einem Kontext erkennen und Löschen [**BETA**]\n\r"
                                          "Dies solltet ihr ernst nehmen,denn es kann dadurch führen,dass wenn ihr die Regeln verstöst,dass ihr gebannt werdet! \n\r "
                                          "**Von @Karkinox programmiert**")
        await message.channel.send(embed=embed)
    if "%funbann" in message.content:
        if message.author == "Betalif#1237" or "Karkinox#5126":
            await message.delete()
            embed = discord.Embed(title="**```Verwarnung```**",
                              description="Sie wurden gewarnt wegen eines Verbotenes ``Bustaben``.")
        await message.channel.send(embed=embed)


    if message.content.startswith("%clear"):
        if message.author.id == "Karkinox#5126":
             args = message.content.split(" ")
             if len(args) == 2:
                 if args[1].isdigit():
                     count = int(args[1]) + 1
                     deleted = await message.channel.purge(limit=count)
                     await message.channl.send("{} Naricht wurde gelöscht.".format(len(deleted) - 1))





client.run("OTIzODUyNjQ1NjUzOTcwOTU0.YcWC0w.3PEY0kO5w83KJcXPzJ0LnbjQCrQ")
