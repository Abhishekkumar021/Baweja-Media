import requests
import json


# weather_api_key = "7d1c033a849e4eb0ba025183251203" # This is dumy API key
weather_api_key = "Your API Key"

forecast_base_url = f"http://api.weatherapi.com/v1/forecast.json"
current_temperature_base_url = f"http://api.weatherapi.com/v1/current.json"


def get_aqi(c_pm2):

    #   AQI = (I_hight- I_low)/(C_hight - C_low) * (C - C_low) + I_low

    CPCB_PM25_BREAKPOINTS = [
        {
            "pm25_range": (0, 30),
            "aqi_range": (0, 50),
            "category": "Good",
            "color": "Green",
        },
        {
            "pm25_range": (31, 60),
            "aqi_range": (51, 100),
            "category": "Satisfactory",
            "color": "Light Green",
        },
        {
            "pm25_range": (61, 90),
            "aqi_range": (101, 200),
            "category": "Moderate",
            "color": "Yellow",
        },
        {
            "pm25_range": (91, 120),
            "aqi_range": (201, 300),
            "category": "Poor",
            "color": "Orange",
        },
        {
            "pm25_range": (121, 250),
            "aqi_range": (301, 400),
            "category": "Very Poor",
            "color": "Red",
        },
        {
            "pm25_range": (251, 500),
            "aqi_range": (401, 500),
            "category": "Severe",
            "color": "Maroon",
        },
    ]

    for breakpoint in CPCB_PM25_BREAKPOINTS:
        if (
            c_pm2 >= breakpoint["pm25_range"][0]
            and c_pm2 <= breakpoint["pm25_range"][1]
        ):
            aqi = (breakpoint["aqi_range"][1] - breakpoint["aqi_range"][0]) / (
                breakpoint["pm25_range"][1] - breakpoint["pm25_range"][0]
            ) * (c_pm2 - breakpoint["pm25_range"][0]) + breakpoint["aqi_range"][0]

            aqi = round(aqi)
            return {
                "AQI": aqi,
                "Category": breakpoint["category"],
            }

    return {"AQI": "N/A", "Category": "N/A"}


def get_weather_data(city_name):
    params = {
        "key": weather_api_key,
        "q": city_name,
        "aqi": "yes",
    }
    try:
        response = requests.get(current_temperature_base_url, params=params)
        response.raise_for_status()
        data = response.json()
        aqi = get_aqi(data["current"]["air_quality"]["pm2_5"])
        # print(response.url)
        # print(json.dumps(data, indent=4))

        # print("\nResponse Data Printing...\n")
        # print(
        #     f"City Name and Region : {data['location']['name']}, {data['location']['region'].split(',')[0]}, {data['location']['country']}"
        # )
        # print(
        #     f"Latitude and Longitude : {data['location']['lat']}, {data['location']['lon']}"
        # )
        # print(f"Local Time : {data['location']['localtime']}")
        # print(f"Local Time Zone : {data['location']['tz_id']}")
        # print(f"Weather Condition : {data['current']['condition']['text']}")
        # print(f"Last Updated : {data['current']['last_updated']}")
        # print(f"Temperature : {data['current']['temp_c']} °C")
        # print(f"Temperature in Fahrenheit : {data['current']['temp_f']} °F")
        # print(f"Humidity : {data['current']['humidity']}%")
        # print(f"AQI : {aqi['AQI']} {(aqi['Category'])} \n")

        return {
            "City Name and Region": f"{data["location"]["name"]}, {data["location"]["region"].split(",")[0]}, {data["location"]["country"]}",
            "Latitude and Longitude": f"{data['location']['lat']}, {data['location']['lon']}",
            "Local Time": data["location"]["localtime"],
            "Local Time Zone": data["location"]["tz_id"],
            "Weather Condition": data["current"]["condition"]["text"],
            "Last Updated": data["current"]["last_updated"],
            "Temperature": f"{data["current"]["temp_c"]} °C",
            "Temperature in Fahrenheit": f"{data["current"]["temp_f"]} °F",
            "Humidity": f"{data["current"]["humidity"]}%",
            "AQI": aqi["AQI"],
            "Category": aqi["Category"],
        }
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return {"Error": "Unable to fetch data for the specified city."}
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return {"Error": "Unable to fetch data for the specified city."}


if __name__ == "__main__":

    data = get_weather_data("Delhi")
    print("\nResponse Data Streaming...\n")
    for key, value in data.items():
        print(f"{key}: {value}")

    print()

# print("\nResponse Data Printing...\n")
# print(
#     f"City Name and Region : {data['location']['name']}, {data['location']['region'].split(',')[0]}, {data['location']['country']}"
# )
# print(
#     f"Latitude and Longitude : {data['location']['lat']}, {data['location']['lon']}"
# )
# print(f"Local Time : {data['location']['localtime']}")
# print(f"Local Time Zone : {data['location']['tz_id']}")
# print(f"Weather Condition : {data['current']['condition']['text']}")
# print(f"Last Updated : {data['current']['last_updated']}")
# print(f"Temperature : {data['current']['temp_c']} °C")
# print(f"Temperature in Fahrenheit : {data['current']['temp_f']} °F")
# print(f"Humidity : {data['current']['humidity']}%")
# aqi = get_aqi(data["current"]["air_quality"]["pm2_5"])
# print(f"AQI : {aqi['AQI']} {(aqi['Category'])} \n")  # type: ignore
