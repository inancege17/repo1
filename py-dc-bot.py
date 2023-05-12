import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

a = ["doğayı koruyalım"]

@bot.command()
async def doga(ctx):
    await ctx.send("a")

bot.run("GİZLİ TOKEN BURAYA")

# Bu kod parçacığı bir metin dosyasının tamamını okumamızı sağlar
f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()
# Ve işte bir metin dosyasının tamamını nasıl yeniden yazabileceğimiz:
f = open('metinbelgesi.txt', 'w', encoding='utf-8')
text = 'Yeni Yazı'
f.write(text)
f.close()