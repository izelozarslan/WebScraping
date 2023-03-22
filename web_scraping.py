import requests #http istekleri gönderebilmek için
from bs4 import BeautifulSoup #request içeriğini parse etmek için
import pandas as pd #veri işleme ve analiz
import csv

yorum, kullanici_bilgisi, tarih, degerlendirme = [],[],[],[]

url = "https://www.hepsiburada.com/hp-15-dw3017nt-intel-core-i3-1115g4-4gb-256-gb-ssd-freedos-15-6-fhd-tasinabilir-bilgisayar-2n2r4ea-p-HBCV000007PQ8B-yorumlari?sayfa="
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
for page in range(1,16):
    response = requests.get(url + str(page) , headers = headers)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi, "html.parser")


    YORUM = soup.find_all("span",{"itemprop":"description"})
    KULLANİCİ_BİLGİSİ = soup.find_all("div",{"class":"hermes-ReviewCard-module-p2lw9pDiloK0sQ9iHHQy"})
    TARİH = soup.find_all("span",{"class":"hermes-ReviewCard-module-WROMVGVqxBDYV9UkBWTS"})
    DEGERLENDIRME = soup.find_all("div",{"class":"hermes-ReviewCard-module-aE344K36tDrcq8cwNt7g"})


    for i,j,l,k in zip(YORUM,KULLANİCİ_BİLGİSİ,TARİH,DEGERLENDIRME):
        yorum.append(i.text)
        kullanici_bilgisi.append(j.text)
        tarih.append(l.text)
        degerlendirme.append(k.text)
    
        

df = pd.DataFrame({ #satır ve sütunlardan oluşan tablo hazırlar
    'yorum' : yorum,    
    'kullanici_bilgisi' : kullanici_bilgisi,
    'tarih' : tarih,
    'degerlendirme' : degerlendirme
})
df.to_csv('Output.csv', encoding='utf-8', index=False,date_format=str)
print(df)
