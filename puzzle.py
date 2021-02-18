#Daniel Bekai's Mini Escape Room!

from machine import Pin #gives ability to control pins
from time import sleep
import uhashlib
import ubinascii


led = Pin(25, Pin.OUT)

morse_code_pin = Pin(15,Pin.OUT)

n = 0

#functions for LED states

def led_stage1():
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.9)
    
def led_stage2():
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.8)
        
def led_stage3():
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.1)
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.7)
    
def state_solved():
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.1)
    
#Hard coded morse code functions

def morse1():
    for x in range(3):
        morse_code_pin.value(1)
        sleep(0.1)
        morse_code_pin.value(0)
        sleep(0.1)
        
    sleep(0.3)
    
    for x in range(3):
        morse_code_pin.value(1)
        sleep(0.2)
        morse_code_pin.value(0)
        sleep(0.1)
        
    sleep(0.3)
    
    for x in range(3):
        morse_code_pin.value(1)
        sleep(0.1)
        morse_code_pin.value(0)
        sleep(0.1)
        
def morse2():
    morse_code_pin.value(1)
    sleep(0.1)
    morse_code_pin.value(0)
    sleep(0.1)
    
    morse_code_pin.value(1)
    sleep(0.2)
    morse_code_pin.value(0)
    sleep(0.1)
    
    morse_code_pin.value(1)
    sleep(0.2)
    morse_code_pin.value(0)
    sleep(0.1)
    
    morse_code_pin.value(1)
    sleep(0.1)
    morse_code_pin.value(0)
    sleep(0.1)
    
    sleep(0.3)
    
    morse_code_pin.value(1)
    sleep(0.1)
    morse_code_pin.value(0)
    sleep(0.1)
    
    morse_code_pin.value(1)
    sleep(0.1)
    morse_code_pin.value(0)
    sleep(0.1)
    
def morse3():
    morse_code_pin.value(1)
    sleep(0.1)
    morse_code_pin.value(0)
    sleep(0.1)
    
    morse_code_pin.value(1)
    sleep(0.2)
    morse_code_pin.value(0)
    sleep(0.1)
    
    sleep(0.3)
    
    for x in range(4):
        morse_code_pin.value(1)
        sleep(0.1)
        morse_code_pin.value(0)
        sleep(0.1)
    
    
    
    
    
    
    
    
    

def sha_hasher(user_input):
    str = uhashlib.sha256(user_input)
    str_hex = ubinascii.hexlify(str.digest())
    ans = str_hex.decode("utf-8")
    return ans


print("Welcome to the escape room in a raspberry pi pico! Use the oscilloscope to decode the morse code message on GPIO 15!")

while True:
    led_stage1()
    guess1 = input("Press \"p\" to play the morse code on GPIO 15, or Enter the code. (lowercase no space): ")
    
    #Hash of the answer for the first stage (so you can't solve it by just looking at the code)
    hash1 = "c0946106b732f9f6ae889101ab987ed1bbcfe3eda2ad0a971be31575ad676851"
    if (sha_hasher(guess1) == hash1):
        print("Nice job! Now for round 2!")
        break
    elif guess1 == "p":
        morse1()
    else:
        print("Wrong! Try again")
        
while True:
    led_stage2()
    guess2 = input("Second round! Enter the code (lowercase no space): ")
    hash2 = "85b42e1702877c851eb7412fe958c8fb447c3207b4798fadab42ea8539046ce1"
    if (sha_hasher(guess2) == hash2):
        print("Nice job! Now for round 3!")
        break
    elif guess2 == "p":
        morse2()
    else:
        print("Wrong! Try again")

while True:
    led_stage3()
    guess3 = input("Second round! Enter the code (lowercase no space): ")
    hash3 = "70a0d5198ebb88f97a2cc83a236a8afcc28c7d9e6abf40c173dd54c9f45ad7f6"
    if (sha_hasher(guess3) == hash3):
        print("Nice! You've solved the puzzle. Here's the hash!")
        print("7297db81c2f7916e25b9593f8c8785e1aa1487fa9f3961c50b7cc5f1a541bc82")
        break
    elif guess3 == "p":
        morse3()
    else:
        print("Wrong! Try again")

while True:
    led.value(1)
    sleep(0.1)
    led.value(0)
    sleep(0.1)
           
        
        
        
    
