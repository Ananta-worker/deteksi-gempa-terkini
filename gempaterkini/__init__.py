"""
__init__.py adalah modul python yang dibaca pertama kali saat package pertama kali di import
"""
import requests
from bs4 import BeautifulSoup



def ekstraksi_data():
    """
    Tanggal: 07 Mei 2025
    Waktu: 07:16:22 WIB
    Pusat gempa: Pusat gempa berada di laut 101 km baratdaya Kab. Blitar
    Magnitudo: 4,5
    Kedalaman: 84 Km
    Lokasi: LS: 9,00 BT:111,92
    :return:
    """
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

        # magnitudo = soup.find('span',{'class':'text-base lg:text-lg font-bold text-black-primary'})
        # kedalaman = soup.find('p',{'class':'Kedalaman:'})



        hasil = dict()  # fungsi mengembalikan dictionary sama dengan {}
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        # hasil['magnitudo'] = magnitudo.text  #4.5
        # hasil['kedalaman'] = kedalaman.text  #'84 Km'
        hasil['lokasi'] = {'ls':9.00,'bt':111.92}
        hasil['pusat_gempa'] = 'Pusat gempa berada di laut 101 km barat daya Kab. Blitar'
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return

    print('\nGempa terakhir berdasarkan BMKG')
    print('---------------------------------')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Pusat Gempa: {result['pusat_gempa']}")
    # print(f"Magnitudo: {result['magnitudo']}")
    # print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: {result['lokasi']['ls']} LS, {result['lokasi']['bt']} BT")


if __name__ == '__main__':
    print('Ini adalah package gempaterkini')
    print('hai')