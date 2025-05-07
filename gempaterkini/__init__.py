"""
__init__.py adalah modul python yang dibaca pertama kali saat package pertama kali di import
"""

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
    hasil = dict()  # fungsi mengembalikan dictionary sama dengan {}
    hasil['tanggal'] = '07 Mei 2025'
    hasil['waktu'] = '07:16:22 WIB'
    hasil['pusat_gempa'] = 'Pusat gempa berada di laut 101 km barat daya Kab. Blitar'
    hasil['magnitudo'] = 4.5
    hasil['kedalaman'] = '84 Km'
    hasil['lokasi'] = {'ls':9.00,'bt':111.92}
    return hasil


def tampilkan_data(result):
    print('\nGempa terakhir berdasarkan BMKG')
    print('---------------------------------')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Pusat Gempa: {result['pusat_gempa']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: {result['lokasi']['ls']} LS, {result['lokasi']['bt']} BT")


# if __name__ == '__main__':
#     print('Ini adalah package gempaterkini')
