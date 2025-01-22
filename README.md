### ArduinoWeatherAPI


## Summery
I wired together an LCD screen to my Arduino Uno and I am making some code to ask OpenWeatherMap.org what the weather is in my area and display it to the LCD screen.


## Aurduino
I watched a youtube video on how to setup a LCD screen with the arduino and a breadboard so this repo assumes you already have it setup. 
I am using a Arduino Uno Starter Kit and the supplies I use are:
1. Arduino Uno
2. 16x2 LCD screen
3. Breadboard
4. Potentiometer (optional)
5. USB 2.0 Cable Type A/B

# How to get around using a potentiometer
A potentiometer is a twistable knob that increases and decreases resistance through a wire. In this case, it is used to increase and decrease the contrast of the LCD screen.
I didn't have a potentiometer for my build so I instead used a PWM (Pulse Width Modulation) port to simulate resistance. So the V0 LCD port connects directly to a PWM port that I specify in my Arduino code.

# OpenWeathermap
OenWeatherMap has free weather API that is simple to use and gives you Weekly, Daily, or hourly weather data about a location you specify. The arduino I used for this does not have a wifi chip. In theory, if you have a wifi chip and a battery to power the arduino, you can use this LCD to display the current weather completely remote/wirelessly.



# How to Get Everything Working

### Now for what you probably want to know. How do you set this thing up?

1. Setup the LCD on the Arduino

  

This was probably the hardest part for me just because I have never done this before so I didn't know how to do anything. Watch a youtube turorial, follow the directions, and you should be fine.

For this build, I have the LCD data connections set to (12, 11, 5, 4, 3, 2). I believe that these are the data ports on the arduino. If you wire your arduino differently, you should change these values. They are at the top of the "ArduinoCode" file.

2. Download the Arduino IDE

I don't know if there is a easier way than the native Arduino software to upload code to the board but it was the method that I chose to use. Copy paste my code or write some code of your own but make sure to upload your code to the Arduino.  Check that your Arduino is using COM1 as the serial communication port (I think it is default?) or if you are using something different, make sure to change the port that it listens on in the code.

3. Run the python code on your PC

Download the Python code. After you have it open in an IDE go to the lines where there are comments in all caps. These are the lines of code that you might want to change. They consist of the API key, the port to send data to Arduino (in this case COM3), and the location that you want to get the weather of (city name).

This is the main section where I can improve . Right now, you need to run the python API code to get the data, parse it, take what you need, and then give it to the Arduino over the COM3 port. I want to eventually be able to do this all wirelessly. I want to get a Wi-Fi chip and have it refresh every hour to get the hourly forecast, and setup to a battery that is solar powered so it can run forever. 
