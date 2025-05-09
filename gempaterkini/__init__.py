"""
__init__.py adalah modul python yang dibaca pertama kali saat package pertama kali di import
"""
import requests
from bs4 import BeautifulSoup


def ekstraksi_data():

    try:
        content = requests.get('https://bmkg.go.id/')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        # print(soup.prettify())  # cetak kode htmlnya
        title = soup.find('title')
        print(title.string) # diambil stringnya saja
        result = soup.find('p',{'class':'mt-2 text-sm leading-[22px] font-medium text-gray-primary'})
        result = result.text.split(', ')
        waktu = result[1]
        tanggal = result[0]

        result = soup.find('div',{'class':'mt-5 flex flex-wrap lg:flex-nowrap gap-3'})

        i = 0
        magnitudo = None
        kedalaman = None
        lokasi = None

        for res in result:
            # print(i, res.text)
            if i == 0:
                res = res.text.split(':')
                magnitudo = res[1]
            elif i == 1:
                res = res.text.split(':')
                kedalaman = res[1]
            elif i == 2:
                res = res.text.split(': ')
                lokasi = res[1]
            i += 1

        result = soup.find('p',{'class':'mt-4 text-xl lg:text-2xl font-bold text-black-primary'})
        pusat = result.text
        result = soup.find('p',{'class':'text-sm font-medium text-black-primary'})
        saran = result.text

        hasil = dict()  # fungsi mengembalikan dictionary sama dengan {}
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['lokasi'] = lokasi
        hasil['pusat_gempa'] = pusat
        hasil['saran'] = saran
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return

    print('\nGempa Bumi Terkini berdasarkan BMKG')
    print('---------------------------------')
    print(f"Titik Gempa: {result['pusat_gempa']}")
    print(f"\nTanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: {result['lokasi']}")
    print(f"\n{result['saran']}")


if __name__ == '__main__':
    print('Ini adalah package gempaterkini')
    print('hai')