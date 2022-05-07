import discord
from discord.ext import commands
from discord.commands import Option
import config
from bs4 import BeautifulSoup
import requests
import html5lib
#from scraper import CovidCases

#import scraper


# Bot Variables
bot = commands.Bot(command_prefix = '!', case_insensitive=True)

# Bot Online Confirmation
def scrape():
    URL = "https://www.worldometers.info/coronavirus/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    covidCases = soup.find('div', class_="maincounter-number")
    counter = covidCases.text.strip()
    print(counter)

'''
URL = "https://www.worldometers.info/coronavirus/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())
covidCases = soup.find('div', class_="maincounter-number")
counter = covidCases.text.strip()
print(counter)
'''

@bot.event
async def on_ready():
    print(f'{bot.user} is online.')

# Bot command for returning Covid cases

@bot.slash_command(guild_ids=[879461344322138173], description="To see if bot is responding to commands.")
async def checkworking(ctx):
    await ctx.respond("I am here.")
    
@bot.slash_command(guild_ids=[879461344322138173], description="Worldwide COVID cases")
async def covidcounter(ctx):
    await ctx.respond("There are currently %s COVID-19 cases worldwide." % scrape())
    
@bot.slash_command(guild_ids=[879461344322138173], description="Information on COVID-19 Pandemic")
async def covidinfo(ctx):
    await ctx.respond("For more information on COVID-19 visit: https://www.cdc.gov/coronavirus/2019-ncov/index.html")
    
    
bot.run = bot.run(config.BOT_TOKEN)