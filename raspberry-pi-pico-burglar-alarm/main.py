import machine
import utime


pir_pin = machine.Pin(28, machine.Pin.IN)
led_pin = machine.Pin(15, machine.Pin.OUT)
buzzer_pin = machine.Pin(14,machine.Pin.OUT)            # Pin tanımları
trigger = machine.Pin(18, machine.Pin.OUT) 
echo = machine.Pin(21, machine.Pin.IN) 

def echoTime():                    
            
    trigger.off()
    utime.sleep_us(2)            #  HC-SR04 sensörün doğru bir şekilde çalışması için 
    trigger.on()                 #  trigger pinini yüksek seviyede bir süre beklettik
    utime.sleep_us(10)
    trigger.off()

    echo_time = machine.time_pulse_us(echo, 1, 1000000)     # echo pininden nesne ile olan yankı süresini ölçtük (1 mikrosaniye = 1/1000000 saniye)
    distance_cm = (echo_time * 0.0343) / 2                  # yankı süresini ses hızı ile çarpıp 2'ye böldük 
    return distance_cm                                      # çünkü sadece gidiş veya geliş süresi ile aradaki mesafeyi ölçebiliriz



led_pin.off()
buzzer_pwm = machine.PWM(buzzer_pin)       # Wokwi'de buzzer üzerinde sadece ses notası gösterilir, ses çıkması için 
buzzer_pwm.freq(440)                       # PWM sinyali ile buzzer'ın ses üretmesini sağladık



while True:

    if pir_pin.value() == 1:             # PIR sensörü hareket algıladığında

        distance = echoTime()            # nesne ile aradaki mesafeyi ölçtük

        if 0< distance < 100 :           # mesafe 0-100 cm arasındaysa

            print("Hareket Algılandı")
            led_pin.on()                     # LED'i yaktık
            buzzer_pwm.duty_u16(32768)       # Buzzer'ı yarı parlaklıkta çalıştırdık
            utime.sleep(2)                   # 2 saniye beklettik

        
        led_pin.off()                       # LED'i ve Buzzer'ı kapattık
        buzzer_pwm.duty_u16(0)          