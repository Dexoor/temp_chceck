# import the module
import python_weather
import asyncio
import os
import pandas as pd


async def getweather(CityName):

  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    # fetch a weather forecast from a city

        weather = await client.get(CityName)
    
    # returns the current day's forecast temperature (int)
        print(cities, '-->', weather.current.temperature,'°C')   

if __name__ == '__main__':
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

cities = pd.read_csv('data/cities.csv')
for cities in cities['city']:
  asyncio.run(getweather(cities))