import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
from machine import Pin, PWM
wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'iPhone de Davy'
password = 'kingjames'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://hp-api.lainocs.fr/characters/"


pin_red = 17
pin_green = 18
pin_blue = 19

pwm_red = PWM(Pin(pin_red, mode=Pin.OUT))
pwm_green = PWM(Pin(pin_green, mode=Pin.OUT))
pwm_blue = PWM(Pin(pin_blue, mode=Pin.OUT))

pwm_red.freq(1_000)
pwm_green.freq(1_000)
pwm_blue.freq(1_000)

def set_rgb_color(red, green, blue):
    pwm_red.duty_u16(int(red * 65535 / 255))
    pwm_green.duty_u16(int(green * 65535 / 255))
    pwm_blue.duty_u16(int(blue * 65535 / 255))
    
    

def get_house_color(house):
    if house == "Gryffindor":
        return (255, 0, 0) 
    elif house == "Slytherin":
        return (0, 255, 0)  
    elif house == "Ravenclaw":
        return (0, 0, 255) 
    elif house == "Hufflepuff":
        return (255, 255, 0)  
    else:
        return (255, 255, 255) 



while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url) 
        characters = r.json() 
        r.close()
        
        character = characters[15]
        house = character.get("house", "pas connue")
        print(f"Character: {character['name']}, House: {house}")
        
        color = get_house_color(house)
        set_rgb_color(*color)
        
       
    
        utime.sleep(3)
        
        
    except Exception as e:
        print(e)
        
        utime.sleep(3)
        
