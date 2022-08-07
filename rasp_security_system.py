import RPi.GPIO as GPIO
import time                                              
import smtplib 


def Email():                                 
    server = smtplib.SMTP('smtp.gmail.com', 587)     
    server.starttls()
    server.login("email", "password") 

    msg = "Sensor 1 Presence Detected"    
    server.sendmail("email", "", msg)
    server.quit()


pir_sensor = 11      
piezo = 7

GPIO.setmode(GPIO.BOARD)  

GPIO.setup(piezo,GPIO.OUT)    

GPIO.setup(pir_sensor, GPIO.IN)  

current_state = 0    

try:      
    while True:
        time.sleep(0.1)          
        current_state = GPIO.input(pir_sensor)  
        if current_state == 1:   
            print("GPIO pin %s is %s" % (pir_sensor, current_state))   
            GPIO.output(piezo,True)   
            time.sleep(1)   
            Email()            
            GPIO.output(piezo,False)   
            time.sleep(5)
except KeyboardInterrupt:   
    pass
finally:
    GPIO.cleanup()
