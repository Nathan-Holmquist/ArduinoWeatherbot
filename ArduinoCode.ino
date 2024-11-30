#include <LiquidCrystal.h>

// Initialize the LCD (12, 11, 5, 4, 3, 2) for what im doin rn
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  pinMode(9, OUTPUT); // Use pin 9 for PWM
  analogWrite(9, 70); // Adjust value (0-255) to control contrast

  // Set up the LCD's number of columns and rows
  lcd.begin(16, 2);

  // Start serial communication
  Serial.begin(9600);

  // Display a welcome message
  lcd.setCursor(0, 0);
  lcd.print("Waiting for data");
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming data as a string
    String data = Serial.readStringUntil('\n'); // Read until newline character
    
    // Debug print statement
    Serial.println("Received: " + data);

    // Clear the LCD and process the data only if it's valid
    if (data.length() > 0) {
      int separatorIndex = data.indexOf(';'); // Find the semicolon separator
      lcd.clear(); // Clear the LCD before displaying new data
      
      if (separatorIndex != -1) {
        // Extract top and bottom rows from the received data
        String topRow = data.substring(0, separatorIndex);
        String bottomRow = data.substring(separatorIndex + 1);
        Serial.println(data);
        // Display the data on the LCD
        lcd.setCursor(0, 0); // Top row
        lcd.print(topRow);
        lcd.setCursor(0, 1); // Bottom row
        lcd.print(bottomRow);
        Serial.println(data);
      } else {
        // If no semicolon, display the entire message on one row
        lcd.setCursor(0, 0);
        lcd.print(data);
      }
    }
    Serial.flush();
  }
}

