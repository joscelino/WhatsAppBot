# Import libraries

""" https://www.youtube.com/watch?v=UenvIUxYo-0&ab_channel=DevAprender"""
import pywhatkit
import keyboard
import time
from datetime import datetime

contact = ['+5511-----', ]
message = open("mensagem.txt", "r")

while len(contact) >= 1:
    print(contact[0])
    pywhatkit.sendwhatmsg(contact[0], message.read(),
                          datetime.now().hour, datetime.now().minute + 1)
    del contact[0]
    time.sleep(15)
    keyboard.press_and_release('crt + w')
