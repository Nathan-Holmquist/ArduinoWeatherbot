import requests
import time
import serial

API_KEY = "a7f45fbcfe01b22cf116a68889c8e31c"

def get_forecast(city_name, api_key, units="imperical"):

    url = "https://api.openweathermap.org/data/2.5/forecast/daily"
    

    params = {
        "q": city_name,  
        "appid": api_key,  
        "cnt": 1,  # Number of days for the forecast
        "units": units,
    }
    
    try:
   
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse JSON response
        data = response.json()

        city = data["city"]["name"]
        country = data["city"]["country"]
        forecast_list = data["list"]

        for day in forecast_list:
            temp = day["temp"]["day"]
            temp = round((temp - 273.15) * 9/5 + 32, 1) 
            weather_desc = day["weather"][0]["description"] 
            lcd_output = f"{temp}F;{weather_desc}"
            print(lcd_output)
            return lcd_output  

            

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError as e:
        print(f"Unexpected response structure: {e}")


# Connect to Arduino via serial
def send_to_arduino(data):
    try:
        arduino.write(f"{data}\n".encode()) # Send data as bytes
        print(f"Sent to Arduino: {data}")
    except Exception as e:
        print(f"Error: {e}")

try:
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
    time.sleep(2) #setup time DO NOT TOUCH THIS

    # Fetch the forecast and send to Arduino
    lcd_output = get_forecast("Reston", API_KEY)
    if lcd_output:
        send_to_arduino(lcd_output)

    arduino.close()  # Close the serial connection
except serial.SerialException as e:
    print(f"Could not connect to Arduino: {e}")