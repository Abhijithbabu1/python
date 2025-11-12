# Arduino LED Blink - Python Control

A simple Python project to control an Arduino board and blink an LED.

## 📋 Description

This project demonstrates how to use Python to communicate with an Arduino board via serial communication to blink an LED on and off. It's a great starting point for learning Arduino-Python integration.

## 🔧 Hardware Requirements

- Arduino board (Uno, Nano, Mega, etc.)
- LED (any color)
- 220Ω resistor
- Breadboard
- Jumper wires
- USB cable for Arduino connection

## 💻 Software Requirements

- Python 3.x
- PySerial library
- Arduino IDE

## 📦 Installation

1. **Install Python dependencies:**
```bash
pip install pyserial
```

2. **Clone this repository:**
```bash
git clone <your-repository-url>
cd arduino-led-blink
```

## 🔌 Circuit Setup

1. Connect the LED anode (longer leg) to Arduino pin 13 through a 220Ω resistor
2. Connect the LED cathode (shorter leg) to GND
3. Connect Arduino to your computer via USB

```
Arduino Pin 13 → 220Ω Resistor → LED (+) → LED (-) → GND
```

## 🚀 Usage

1. **Upload Arduino sketch** (if using Arduino-side code)
2. **Find your Arduino port:**
   - Windows: `COM3`, `COM4`, etc.
   - Linux/Mac: `/dev/ttyUSB0`, `/dev/ttyACM0`, etc.

3. **Run the Python script:**
```bash
python blink_led.py
```

## 📝 Code Example

### Python Code (blink_led.py)

```python
import serial
import time

# Configure serial connection
arduino = serial.Serial('COM3', 9600)  # Change COM3 to your port
time.sleep(2)  # Wait for connection to establish

try:
    while True:
        arduino.write(b'1')  # Turn LED ON
        print("LED ON")
        time.sleep(1)
        
        arduino.write(b'0')  # Turn LED OFF
        print("LED OFF")
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nStopping...")
    arduino.close()
```

### Arduino Code (blink_led.ino)

```cpp
int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == '1') {
      digitalWrite(ledPin, HIGH);
    }
    else if (command == '0') {
      digitalWrite(ledPin, LOW);
    }
  }
}
```

## 🐛 Troubleshooting

- **Port not found:** Check Arduino is connected and note the correct port in Device Manager (Windows) or `ls /dev/tty*` (Linux/Mac)
- **Permission denied (Linux):** Add user to dialout group: `sudo usermod -a -G dialout $USER`
- **LED not blinking:** Check connections and resistor value
- **Serial communication error:** Ensure baud rate matches in both Python and Arduino code (9600)

## 📚 How It Works

1. Python opens a serial connection to the Arduino
2. Python sends '1' or '0' characters through serial
3. Arduino reads these characters
4. Arduino turns LED ON (HIGH) or OFF (LOW) based on received command

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

MIT License - feel free to use this project for learning and development.

## 👤 Author

Abhijith Babu - [Python]

## 🔗 Resources

- [PySerial Documentation](https://pyserial.readthedocs.io/)
- [Arduino Serial Communication](https://www.arduino.cc/reference/en/language/functions/communication/serial/)
