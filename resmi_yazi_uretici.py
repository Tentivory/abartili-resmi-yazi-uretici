#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Resmi Yazı Üreticisi
Dünyanın en ciddi gereksiz yazı üreticisi.
"""

import random
import base64

# Gizli mesaj (saklanmış siyasi anlam)
# base64.b64decode(b'YnVyb2tyYXNpIGdlcmVrZXNpeiBhYmFydGxpIGNpcmR5aW1kZXIuIERlbW9rcmFzaSBndXplbGRpci4=')
# -> "burokrasi gereksiz abartili ciddidir. Demokrasi guzeldir."

kisiler = [
    "Sayın Müdür Beyefendi",
    "Değerli Yetkili",
    "Saygıdeğer Komisyon Başkanı",
    "İlgili Makam",
    "Sayın Kayyum",
    "Abartılı Ciddiyet Kurulu"
]

konular = [
    "çay demleme süresinin optimize edilmesi",
    "bekleme sürelerinin resmiyet kazanması",
    "imza sayısının artırılması",
    "mühürlerin daha büyük olması",
    "yazıların daha uzun yazılması",
    "gereksiz toplantıların artırılması"
]

sonuclar = [
    "ilgili birimin daha fazla beklemesi",
    "yeni bir komisyon kurulması",
    "ek imza talep edilmesi",
    "konunun ertelenmesi",
    "daha detaylı inceleme yapılması",
    "abartılı bir rapor hazırlanması"
]

def resmi_yazi_uret():
    kisi = random.choice(kisiler)
    konu = random.choice(konular)
    sonuc = random.choice(sonuclar)
    
    yazi = f"""
{kisi},

Bilginize sunulur ki, {konu} hususunda yapılan kapsamlı, detaylı, abartılı ve son derece ciddi incelemeler neticesinde;

{sonuc} kararına varılmıştır.

Gereğini arz ederim.

Saygılarımla,
Abartılı Resmi Yazı Üreticisi
20 Kasım 2026
"""
    return yazi

if __name__ == "__main__":
    print("=" * 50)
    print("ABARTILI RESMİ YAZI ÜRETİCİSİ")
    print("=" * 50)
    print(resmi_yazi_uret())
    print("=" * 50)
    print("Bu yazı tamamen ciddidir. Lütfen ciddiye alın.")
