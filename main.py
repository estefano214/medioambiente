import discord, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Hemos iniciado sesión como", bot.user)

@bot.command()
async def clima(ctx):
    datos = [
        ("La basura mal gestionada aporta el 5% del calentamiento global", "basura.jpeg"),
        ("El transporte representa cerca del 14% del calentamiento global", "transporte.jpeg"),
        ("La producción de energía genera más del 25% del calentamiento global", "energia.jpg"),
        ("La deforestación aporta alrededor del 10%", "deforestacion.jpeg"),
        ("La industria contribuye con un 20% del calentamiento global", "industria.jpg")
    ]

    texto, imagen = random.choice(datos)

    try:
        await ctx.send(texto, file=discord.File(imagen))
    except:
        await ctx.send(texto + " (Imagen no encontrada)")

bot.run("token")
