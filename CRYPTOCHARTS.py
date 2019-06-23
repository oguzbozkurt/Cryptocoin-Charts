import requests
from bs4 import BeautifulSoup
import time

url = "https://tr.investing.com/crypto/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content,"html.parser")
tablo=soup.find_all("table",{"class":"genTbl js-top-crypto-table mostActiveStockTbl crossRatesTbl allCryptoTlb wideTbl elpTbl elp15"})
veriler=(tablo[0].contents)[len(tablo[0].contents)-2] #tbody kısmını çeker para değerleri için
trveriler=veriler.find_all("tr")

coinler=["btc","eth","ripple","ltc","btcash","eos","bnccoin","svcoin","tether","stellar"]
paralar=[] #değerlerin atanacağı liste
artislar=[] #24 saatlik artışların aktarılacağı liste

for fiyat in trveriler:
    veri=fiyat.find_all("td",{"class":"price js-currency-price"}) #değerlerin oldugu bölüm
    veriismi=veri[0].text #değerleriin texte çevrilmesi
    paralar.append(veriismi) #değerlerin paralar listesine atanması

    artisveri=fiyat.find_all("td",{"class":"js-total-vol"}) #artışların okundugu bölüm
    artisveriismi=artisveri[0].text #artis değerlerinin texte çevrilmesi
    artislar.append(artisveriismi)

btc=paralar[0]
eth=paralar[1]
ripple=paralar[2]
ltc=paralar[3]
btcash=paralar[4]
eos=paralar[5]
bnccoin=paralar[6]
sv=paralar[7]
tether=paralar[8]
stellar=paralar[9]
btc1=artislar[0]
eth1=artislar[1]
ripple1=artislar[2]
ltc1=artislar[3]
btcash1=artislar[4]
eos1=artislar[5]
bnccoin1=artislar[6]
sv1=artislar[7]
tether1=artislar[8]
stellar1=artislar[9]


def xx():
    for i in range(0, 10):
        print("Coinler:", coinler[i], "   Değerleri:", paralar[i], "    Toplam hacimler:", artislar[i])
    print("-----------------------NEW CHARTS------------------------------------------")
for i in range(0,999):
    xx()
    time.sleep(5)



