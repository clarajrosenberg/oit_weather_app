import requests
from pprint import pprint
from keys import location_API_key, weather_API_key


def get_lat_long(location):
    """
    Get latitude and longitude for a location the user inputs.
    Args: location - user input
    Returns: lat, long - latitude & longitude from API
    """
    location_base_url = "http://api.positionstack.com/v1/forward?access_key="\
                        + location_API_key + "&query=" + location
    location_data = requests.get(location_base_url).json()
    lat = str(location_data["data"][0]["latitude"])
    long = str(location_data["data"][0]["longitude"])

    return lat, long


def kelv_to_fahr(temp_kelv):
    """
    Helper function to change API temp output in Kelvin to Fahrenheit.
    Arg: temp_kelv - temperature in Kelvin
    Returns: temp_fahr - temperature in Fahrenheit
    """
    temp_fahr = round(1.8*(temp_kelv-273) + 32)

    return temp_fahr


def get_weather(lat, long):
    """
    Get and print basic weather forecast for a given lat & long.
    Args: lat, long - latitude & longitude from get_lat_long()
    """
    weather_base_url = "http://api.openweathermap.org/data/2.5/weather?appid="\
                        + weather_API_key + "&lat=" + lat + "&lon=" + long
    weather_data = requests.get(weather_base_url).json()

    forecast = weather_data["weather"][0]["description"]
    feels_like = kelv_to_fahr(weather_data["main"]["feels_like"])
    temp_max = kelv_to_fahr(weather_data["main"]["temp_max"])
    temp_min = kelv_to_fahr(weather_data["main"]["temp_min"])
    output_list = ["Today's forecast is ", forecast, ". It currently feels like ",
                   str(feels_like), " with a high of ", str(temp_max),
                   " and a low of ", str(temp_min), "."]
    print("".join(output_list))


def main():
    location = input("Enter a location: ")
    lat, long = get_lat_long(location)
    get_weather(lat, long)
    print("Seem wrong? Try being more specific (e.g. 'Springfield MA' instead of 'Springfield').")


if __name__ == "__main__":
    main()