import requests
import time
import serial

API_KEY = ""  # PUT YOUR API KEY THAT YOU GET FROM OPENWEATHERMAP INBETWEEN THE QUOTES

def get_forecast(city_name, api_key, units="imperical"):

    url = "https://api.openweathermap.org/data/2.5/forecast/daily"
    

    params = {
        "q": city_name,  
        "appid": api_key,  
        "cnt": 1,  # The amount of days you want to get the forcast for. | ex. 3  will give you the weather for today and the next 2 days
        "units": units,
    }
    
    try:
   
        response = requests.get(url, params=params)
        response.raise_for_status()  

        # Parse JSON
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
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1) # ASSUMING THAT YOU ARE USING COM3
    time.sleep(2) #setup time, don't touch this

    # Fetch the forecast and send to Arduino
    lcd_output = get_forecast("<YOUR CITY HERE>", API_KEY) # WRITE WHATEVER CITY YOU WANT TO GET THE FORECAST FOR
    if lcd_output:
        send_to_arduino(lcd_output)

    arduino.close()  # Close the serial connection
except serial.SerialException as e:
    print(f"Could not connect to Arduino: {e}")