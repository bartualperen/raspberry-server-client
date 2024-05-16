import csv
import time

def csv_dosyasindan_oku(dosya_adi):
	veri_listesi = []
	with open(dosya_adi, 'r', newline='', encoding='utf-8') as dosya:
		csv_okuyucu = csv.reader(dosya)
		for satir in csv_okuyucu:
			veri_listesi.append(satir)
	return veri_listesi
	
dosya_adi = "testn.csv"
veriler = csv_dosyasindan_oku(dosya_adi)


for veri in veriler:
		print(veri)
		time.sleep(1)
	
