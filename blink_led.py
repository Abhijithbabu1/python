#!/usr/bin/env python3
"""
Arduino LED Blink Controller
Control an Arduino LED via serial communication
"""

import serial
import time
import sys

# Configuration
ARDUINO_PORT = 'COM3'  # Change this to your Arduino port
BAUD_RATE = 9600
BLINK_DELAY = 1  # seconds

def main():
    """Main function to control LED blinking"""
    try:
        # Establish serial connection
        print(f"Connecting to Arduino on {ARDUINO_PORT}...")
        arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for Arduino to reset and connection to establish
        print("Connected successfully!\n")
        
        print("LED Blink Started (Press Ctrl+C to stop)\n")
        
        # Blink loop
        while True:
            # Turn LED ON
            arduino.write(b'1')
            print("💡 LED ON")
            time.sleep(BLINK_DELAY)
            
            # Turn LED OFF
            arduino.write(b'0')
            print("⚫ LED OFF")
            time.sleep(BLINK_DELAY)
            
    except serial.SerialException as e:
        print(f"Error: Could not open serial port {ARDUINO_PORT}")
        print(f"Details: {e}")
        print("\nTroubleshooting:")
        print("1. Check if Arduino is connected")
        print("2. Verify the correct port (Windows: COMx, Linux/Mac: /dev/ttyUSBx)")
        print("3. Close Arduino IDE Serial Monitor if open")
        sys.exit(1)
        
    except KeyboardInterrupt:
        print("\n\nStopping LED blink...")
        arduino.write(b'0')  # Turn off LED before closing
        time.sleep(0.1)
        arduino.close()
        print("Connection closed. Goodbye!")
        sys.exit(0)
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        if 'arduino' in locals():
            arduino.close()
        sys.exit(1)

if __name__ == "__main__":
    main()
