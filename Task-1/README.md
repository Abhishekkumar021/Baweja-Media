# Task-1: Weather Data API Utility

This module provides functions to fetch weather and air quality data for a given city using [weatherapi.com](https://www.weatherapi.com/).

---

## 1. **Requirements**

- Python 3.7+
- `requests` library

Install dependencies (if not already installed):

```sh
pip install requests
```

---

## 2. **File Structure**

```
Task-1/
│
├── __init__.py
└── Python_And_API_Data.py
```

---

## 3. **How to Use**

### **A. As a Standalone Script**

You can run the script directly to test weather data fetching:

```sh
cd Task-1"
Python_And_API_Data.py
```

This will print weather and AQI data for the city `"Delhi"` (default in the script).

---

### **B. As an Importable Module**

You can import and use the `get_weather_data` function in your own Python code:

```python
from Python_And_API_Data import get_weather_data

city = "Delhi"
data = get_weather_data(city)
print(data)
```

---

## 4. **Function Reference**

### `get_weather_data(city_name: str) -> dict`

Fetches weather and AQI data for the specified city.

- **Parameters:**  
  `city_name` (str): Name of the city.

- **Returns:**  
  `dict` with weather and AQI details, or error message.

---

## 5. **Environment Variables**

No environment variables are required for Task-1.  
The API key is hardcoded in `Python_And_API_Data.py` as `weather_api_key`.

---

## 6. **Notes**

- Ensure you have a valid API key for [weatherapi.com](https://www.weatherapi.com/).
- If you want to use your own API key, replace the value of `weather_api_key` in [`Python_And_API_Data.py`](Task-1/Python_And_API_Data.py).

---

## 7. **Example Output**

```json
{
  "City Name and Region": "Delhi, Delhi, India",
  "Latitude and Longitude": "28.67, 77.22",
  "Local Time": "2025-05-18 14:00",
  "Local Time Zone": "Asia/Kolkata",
  "Weather Condition": "Partly cloudy",
  "Last Updated": "2025-05-18 13:45",
  "Temperature": "35.0 °C",
  "Temperature in Fahrenheit": "95.0 °F",
  "Humidity": "30%",
  "AQI": 110,
  "Category": "Moderate"
}
```

---