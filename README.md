# oit_weather_app

A program that takes input of a location and outputs the day's weather forecast. It does this by first making an API call to determine the latitude & longitude of the place that most closely matches the input given, and then making a second API call to get the daily weather forecast for those coordinates.

In order to run this successfully, you will need to create two API keys and store them in a file named keys.py:
- [OpenWeather](https://openweathermap.org/api)
- [PositionStack](https://positionstack.com/product)

This is an expansion of CodeWithTomi/FreeCodeCamp's tutorial [Getting Weather Information](https://www.youtube.com/watch?v=SqvVm3QiQVk&t=1494s).

I coded this as one of multiple mini-projects during [Out in Tech](https://outintech.com/)'s fall 2022 mentorship program. I chose this project to gain practice making basic API calls as part of a larger pipeline.