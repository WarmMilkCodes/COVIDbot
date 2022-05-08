from time import sleep
from urllib import response
import discord
from discord.ext import commands
from discord.commands import Option
from numpy import real
import config
from bs4 import BeautifulSoup
import requests
from uszipcode import SearchEngine
import html5lib
import addfips
import urllib.request, json

# Bot Variables
bot = commands.Bot(case_insensitive=True)


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
    soup = BeautifulSoup(r.content, 'html5lib')
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
    

@bot.slash_command(guild_ids=[879461344322138173], description="Check for vaccine locations near you")
async def covidvaccine(ctx, 
    zipcode:Option(int, max=5),
    age:Option(int, min=5)
    ):
    search = SearchEngine()
    zipcodeSearch = search.by_zipcode(zipcode)
    zipList = zipcodeSearch.values()
    majorCity = zipList[3]
    if age >= 5 and age <= 11:
        await ctx.respond("I'm looking for vaccines suitable for age of %s near %s now." % (age, majorCity))
        sleep(3)
        await ctx.respond("https://www.vaccines.gov/results/?zipcode=%s&medicationGuids=25f1389c-5597-47cc-9a9d-3925d60d9c21&medicationKeys=pfizer_covid_19_vaccine_pediatric_range_1&appointments=true" % zipcode)
    elif age >= 12 and age < 18:
        await ctx.respond("I'm looking for vaccines suitable for age of %s near %s now." % (age, majorCity))
        sleep(3)
        await ctx.respond("https://www.vaccines.gov/results/?zipcode=%s&medicationGuids=a84fb9ed-deb4-461c-b785-e17c782ef88b&medicationKeys=pfizer_covid_19_vaccine&appointments=true" % zipcode)
    elif age >= 18:
        await ctx.respond("I'm looking for vaccines suitable for age of %s near %s now." % (age, majorCity))
        sleep(3)
        await ctx.respond("https://www.vaccines.gov/results/?zipcode=%s&medicationGuids=779bfe52-0dd8-4023-a183-457eb100fccc,784db609-dc1f-45a5-bad6-8db02e79d44f,a84fb9ed-deb4-461c-b785-e17c782ef88b&medicationKeys=moderna_covid_19_vaccine,j%%26j_janssen_covid_19_vaccine,pfizer_covid_19_vaccine&appointments=true" % zipcode)
    else:
        await ctx.respond("I was unable to find anything. Please ensure your search options for age and zipcode are correctly entered and try again. You entered age: %s --- your city is: %s" % (age, majorCity))
        
        
@bot.slash_command(guild_ids=[879461344322138173], description="Check your local community's COVID status")
async def covidlocal(ctx,
                    county:Option(str),
                    state:Option(str,"State abbreviation",max=2) 
                    ):
     
    
    af = addfips.AddFIPS()
    
    countyCode = af.get_county_fips(county, state=state)
    
    await ctx.respond("Checking COVID-19 Community Level in %s County, %s" % (county.capitalize(),state.upper()))
    sleep(3)
    jsonURL = "https://api.covidactnow.org/v2/county/%s.json?apiKey=%s" % (countyCode, config.CDC_API)
    print(jsonURL)
    response = urllib.request.urlopen(jsonURL)
    data = json.loads(response.read())
    cases = data['actuals']['cases']
    deaths = data['actuals']['deaths']
    await ctx.respond("Results for %s County, %s. Total cases: %s. Total deaths: %s" % (county.capitalize(), state.upper(), cases, deaths))
    
 


    
bot.run = bot.run(config.BOT_TOKEN)

