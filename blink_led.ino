/*
  Arduino LED Blink - Serial Control
  
  This sketch receives commands from Python via serial communication
  to control an LED connected to pin 13.
  
  Commands:
  - '1' or 'H': Turn LED ON
  - '0' or 'L': Turn LED OFF
  
  Circuit:
  - LED anode (+) connected to pin 13 through 220Ω resistor
  - LED cathode (-) connected to GND
*/

const int LED_PIN = 13;  // Built-in LED on most Arduino boards

void setup() {
  // Initialize LED pin as output
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);  // Start with LED off
  
  // Initialize serial communication
  Serial.begin(9600);
  
  // Wait for serial connection
  while (!Serial) {
    ; // Wait for serial port to connect (needed for native USB boards)
  }
  
  // Send ready message
  Serial.println("Arduino LED Controller Ready");
  
  // Flash LED twice to indicate ready
  for (int i = 0; i < 2; i++) {
    digitalWrite(LED_PIN, HIGH);
    delay(200);
    digitalWrite(LED_PIN, LOW);
    delay(200);
  }
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    // Read the incoming byte
    char command = Serial.read();
    
    // Process the command
    switch (command) {
      case '1':
      case 'H':
      case 'h':
        digitalWrite(LED_PIN, HIGH);  // Turn LED ON
        Serial.println("LED: ON");
        break;
        
      case '0':
      case 'L':
      case 'l':
        digitalWrite(LED_PIN, LOW);   // Turn LED OFF
        Serial.println("LED: OFF");
        break;
        
      default:
        // Unknown command
        Serial.print("Unknown command: ");
        Serial.println(command);
        break;
    }
  }
}
