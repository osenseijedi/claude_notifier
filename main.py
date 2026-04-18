import argparse
import serial
from serial.tools.list_ports import comports
import time
import os
import threading

# Remove pygame startup message. To do before importing pygame.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


def playSound(wav_file):
    sound = pygame.mixer.Sound(wav_file)

    sound.play()
    time.sleep(sound.get_length())


def main(command: str):
    if command not in ['aiDone', 'aiQuestion']:
        print("Invalid command. Please use 'aiDone' or 'aiQuestion'.")
        return

    # Initialize the pygame mixer
    pygame.mixer.init()

    ports = comports()

    script_path = os.path.abspath(os.path.dirname(__file__))
    t = threading.Thread(target=playSound, args=(f'{script_path}/{command}_2.wav',))

    t.start()

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

            except Exception as e:
                print(f"Error: {e}")
            finally:
                ser.close()
    t.join()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str)
    args = parser.parse_args()
    main(args.command)
