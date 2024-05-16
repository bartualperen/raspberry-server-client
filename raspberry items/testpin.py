import RPi.GPIO as GPIO
import time

# Kullanılan GPIO pinleri
TX_PIN = 14
RX_PIN = 15

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TX_PIN, GPIO.OUT)
    GPIO.setup(RX_PIN, GPIO.IN)

def send_data():
    print("TX Pin'e veri gönderiliyor...")
    GPIO.output(TX_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(TX_PIN, GPIO.LOW)

def receive_data():
    print("RX Pin'den veri okunuyor...")
    data = GPIO.input(RX_PIN)
    print(f"Alınan veri: {data}")

def main():
    setup_gpio()

    try:
        while True:
            send_data()
            receive_data()
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nProgram kapatılıyor...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
