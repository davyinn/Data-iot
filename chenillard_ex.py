from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pin1 = 17 # declaration d'une variable pinNumber à 17
pin2 = 18
pin3 = 27


led1 = Pin(pin1, mode=Pin.OUT)
led2 = Pin(pin2, mode=Pin.OUT)
led3 = Pin(pin3, mode=Pin.OUT)
while True:  # Boucle infinie
 
    led1.on()
    led2.off()
    led3.off()
    utime.sleep(1)  

   
    led1.off()
    led2.on()
    led3.off()
    utime.sleep(1)  ;

   
    led1.off()
    led2.off()
    led3.on()
    utime.sleep(1) 