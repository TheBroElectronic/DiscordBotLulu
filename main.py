########### CREATED BY LUCIANO B. #############
########### ALIAS TheBroJef       #############

##--------ESTE NO ES UN ESCRIPT SERIO-------###

# PARA USAR ESTE BOT, COLOCA UN TOKEN AL FINAL
# DEL CODIGO

# comandos: $inspirar, $creador,$Chat (Jef / Train / off), $l (message)

from chatterbot import ChatBot
import discord
import os
import requests
import json
import random

client = discord.Client()

# ============ variables ============
# = lista de fraces para contestar =#
fracesLlamada = ["hola", "dime", "holi", "zZzZzZz", "que pasa?", "no estoy"]

fracesContestar = ["si", "a mimir", "clave", "estoy durmiendo no molestes", "miau", "xd", "cacahuete",
                   "dame comida y punto", "dame comida", "no", "feo", "te quiero", "dame morfi y no hables",
                    "cayadito te ves mas bonito", "que onda","deja dormir", "tengo sueñito","miau",
                    "||capo el que lee||"]


# = lista de fraces que detecta =#
fracesConversacion = ["porque", "uh", "gracias", "como que", "por que", "y vos", "malo",
                      "que onda", "bue", "agresiva", "agresivo", "porque?", "mala", "buee"]

# = variables auxiliares =#
talk = False
com = ""
interaction = ""


# ============ functions ============#
def inspirar():
    response = requests.get("https://zenquotes.io/api/random")
    data = json.loads(response.text)
    insp = data[0]["q"]
    return insp


# = sistema de converzacion
print("Training")
chatbot = ChatBot('LuluBotChat', trainer="chatterbot.trainers.ChatterBotCorpusTrainer")
chatbot.train("chatterbot.corpus.spanish")


def MessageSistemJef(msg):
    global talk
    global interaction

    if interaction == """$m
       verga, nu puedo""":
        interaction = ""
        return "$m"

    elif (msg.startswith("lulu") and msg.endswith("lulu")) or (msg.startswith("lulu?") and msg.endswith("lulu?")):
        talk = True
        return random.choice(fracesLlamada)

    elif ("lulu" in msg) or (talk and any(word in msg for word in fracesConversacion)):
        contestar = random.choice(fracesContestar)
        if contestar == "estoy que tiro waifu":
            interaction = """$m
       verga, nu puedo"""
        return contestar

    else:
        talk = False
        return ""


def MessageSistemBot(msg):
    return chatbot.get_response(msg)


# ============ events ============#
@client.event
async def on_ready():
    print("logeado en {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # = Commands sistem =#
    if message.content.startswith("$help"):
        await message.channel.send("$inspirar, $creador,$Chat (Jef / Train / off), $l (message)")

    elif message.content.startswith("$Chat"):
        global com

        if len(message.content) > 6:
            com = message.content.split("$Chat ", 1)[1]

            if com == "off":
                com = "off"
                await message.channel.send("Response Sistem OFF")

            elif com == "Jef":
                com = "Jef"
                await message.channel.send("Response Sistem using lib 'Jef'")

            elif com == "Train":
                com = "Train"
                await message.channel.send("Response Sistem using lib 'Train'")
            else:
                com = ""
                await message.channel.send("$Chat (Jef / Train / off)")
        else:
            com = ""
            await message.channel.send("$Chat (Jef / Train / off)")


    elif message.content.startswith("$inspirar"):
        await message.channel.send(inspirar())


    elif message.content.startswith("$creador"):
        await message.channel.send("///creado por TheBroJef///")  # luciano B.


    # = Message sistem =#
    elif com == "Jef":
        msg = MessageSistemJef(message.content)
        if (msg != ""):
            await message.channel.send(msg)

    elif com == "Train":
        msg = MessageSistemBot(message.content)
        if (msg != ""):
            await message.channel.send(msg)

client.run(os.getenv('TOKEN')) ## INSERT TOKEN