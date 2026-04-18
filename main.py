import argparse
import serial
from serial.tools.list_ports import comports
import pygame
import time

# Initialize the pygame mixer
pygame.mixer.init()


def main(command: str):
    if command != 'aiDone' and command != 'aiQuestion':
        print("Invalid command. Please use 'aiDone' or 'aiQuestion'.")
        return

    ports = comports()

    for port in ports:
        if port.description.startswith('Arduino Micro'):

            ser = serial.Serial(
                port=port.device,
                baudrate=9600,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=1
            )

            try:
                data = command.encode()
                ser.write(data)
                ser.flush()
                print(f"Sent: {data.decode()}")

                sound = pygame.mixer.Sound(f'E:/Projects/ProgProject/__CLAUDE__/macropad_notifier/{command}_2.wav')

                sound.play()
                time.sleep(sound.get_length())

            except Exception as e:
                print(f"Error: {e}")
            finally:
                ser.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str)
    args = parser.parse_args()
    main(args.command)
