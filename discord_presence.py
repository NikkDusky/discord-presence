from configparser import ConfigParser
from pypresence import Presence
from time import sleep
from PyQt5.QtCore import QThread
import time
import random
import os

parser = ConfigParser()
parser.read('presence_settings.ini')

#Settings parse
application_id = parser.get('settings', 'app_id')
icons = (parser.get('settings', 'images')).split()
sleep_time = float(parser.get('settings', 'sleep_time'))

text_btn = parser.get('settings', 'button_text')
link_btn = parser.get('settings', 'button_link')

color_list = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f")

btns = [
    {
        "label": f"{text_btn}",
        "url": f"{link_btn}"
    },
        ]

#Discord app connection
RPC = Presence(application_id)
RPC.connect()
os.system("title Discord Rich Presence")
start_time = time.time()

while True:
    os.system("cls")
    random_color = random.choice(color_list)
    os.system(f"color 0{random_color}")
    #Get random icon
    iconBig = random.choice(icons)
        
    #Get time
    date_now = time.strftime("%d %B %Y", time.localtime())
    time_now = time.strftime("%H-%M-%S", time.localtime())
    print(f"Time: {time_now}")
    print(f"Date: {date_now}")
    print(f"Picture now: {iconBig}")
    print(f"App id: {application_id}")
    print(f"Start time: {start_time}")
        
    #Discord app update
    RPC.update(
        state=f"{date_now}",
        details=f"{time_now}",
        buttons=btns,
        large_image=f"{iconBig}",
        start=start_time
        )
    sleep(sleep_time)