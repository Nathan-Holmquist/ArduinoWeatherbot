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



