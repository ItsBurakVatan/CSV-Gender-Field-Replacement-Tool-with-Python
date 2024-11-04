import os
import re


klasor_yolu = 'C:\\Users\\brkeq\\OneDrive\\Masaüstü\\Yeni klasör (2)\\valid'


dosya_listesi = os.listdir(klasor_yolu)


xml_dosyalari = [dosya for dosya in dosya_listesi if dosya.endswith('.xml')]


for dosya_adi in xml_dosyalari:
    dosya_yolu = os.path.join(klasor_yolu, dosya_adi)

    with open(dosya_yolu, 'r') as dosya:
        xml_icerik = dosya.read()


    yeni_xml_icerik = re.sub(r'females', 'head', xml_icerik)


    with open(dosya_yolu, 'w') as dosya:
        dosya.write(yeni_xml_icerik)


