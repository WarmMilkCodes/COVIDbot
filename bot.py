import discord
from discord.ext import commands
from discord.commands import Option
from numpy import real
import config
from bs4 import BeautifulSoup
import requests
from uszipcode import SearchEngine

# Bot Variables
bot = commands.Bot(command_prefix = '!', case_insensitive=True)


@bot.event
async def on_ready():
    print(f'{bot.user} is online.')


# Bot commands

@bot.slash_command(guild_ids=[879461344322138173], description="To see if bot is responding to commands.")
async def checkworking(ctx):
    await ctx.respond("I am here.")
    
    
@bot.slash_command(guild_ids=[879461344322138173], description="Worldwide COVID cases")
async def covidcounter(ctx):
    URL = "https://www.worldometers.info/coronavirus/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'htmlparser')
    covidCases = soup.find('div', class_="maincounter-number")
    counter = covidCases.text.strip()
    print(counter)
    await ctx.respond('The current number of COVID-19 cases to date is %s.' % counter)
    
    
@bot.slash_command(guild_ids=[879461344322138173], description="Information on COVID-19 Pandemic")
async def covidinfo(ctx):
    await ctx.respond("For more information on COVID-19 visit: https://www.cdc.gov/coronavirus/2019-ncov/index.html")
    

@bot.slash_command(guild_ids=[879461344322138173], description="Request free at-home COVID tests")
async def covidtest(ctx):
    await ctx.respond("Request your free at-home COVID tests from the USPS: https://special.usps.com/testkits")
    
'''    
@bot.slash_command(guild_ids=[879461344322138173], description="Check for vaccine locations near you")
async def covidvaccine(ctx, 
    zipcode:Option(int, max=5)
    ):
    search = SearchEngine()
    zipcodeSearch = search.by_zipcode(zipcode)
    zipList = zipcodeSearch.values()
    majorCity = zipList[3]
    await ctx.respond("I've got your city as %s" % majorCity)
    
'''


    
bot.run = bot.run(config.BOT_TOKEN)

