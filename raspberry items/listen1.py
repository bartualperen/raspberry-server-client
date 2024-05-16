from pymavlink import mavutil
import time

# Seri bağlantı portu ve baudrate'i
seri_port = '/dev/ttyS0'  # Raspberry Pi üzerinde genellikle ttyS0 kullanılır
baudrate = 57600  # Pixhawk'un baudrate'ine uygun olarak ayarlayın (genellikle 57600)

try:
    # Seri bağlantıyı aç
    mav_serial = mavutil.mavlink_connection(seri_port, baud=baudrate)
    print(f"Seri bağlantı açıldı: {seri_port}")

    while True:
        try:
            # MAVLink mesajını al
            msg = mav_serial.recv_match(blocking=True)
            if msg is not None:
                # Alınan mesajı kontrol et (yükseklik verisi için VFR_HUD veya GLOBAL_POSITION_INT mesajları)
                if msg.get_type() == 'GLOBAL_POSITION_INT':
                    # VFR_HUD mesajından yükseklik verisini al
                    altitude = msg.relative_alt / 1000.0
                    longitude = msg.lon / 1.0e7
                    latitude = msg.lat / 1.0e7
                    print(f"Altitıde (VFR_HUD): {altitude} meter")
                    print(f"Longtitude (VFR_HUD): {longitude} meter")
                    print(f"Latitude (VFR_HUD): {latitude} meter")

               # elif msg.get_type() == 'GLOBAL_POSITION_INT':
                    # GLOBAL_POSITION_INT mesajından yükseklik verisini al
                #    altitude = msg.relative_alt / 1000.0  # 1/1000 faktörünü kullanarak mm'den metreye çevir
                 #   print(f"Yükseklik (GLOBAL_POSITION_INT): {altitude} meter")
                  #  print(f"Yükseklik (GLOBAL_POSITION_INT): {longitude} meter")
                   # print(f"Yükseklik (GLOBAL_POSITION_INT): {latitude} meter")



        except KeyboardInterrupt:
            # Ctrl+C ile programı sonlandır
            break
        except Exception as e:
            # Hata durumlarını yakala
            print("Hata:", e)

except mavutil.MavlinkError as e:
    print(f"Seri bağlantı hatası: {e}")

finally:
    # Seri bağlantıyı kapat
    if mav_serial is not None and mav_serial.is_open():
        mav_serial.close()
        print("Seri bağlantı kapatıldı.")
