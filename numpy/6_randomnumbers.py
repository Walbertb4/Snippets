# ==========================================
# NUMPY RANDOM (RASTGELE SAYI ÜRETİMİ) ÖZETİ
# ==========================================
# Nedir?: Belirli aralıklarda, farklı istatistiksel dağılımlara sahip 
# veya mevcut bir diziden rastgele sayılar/diziler (array) üretmeyi sağlar.
#
# EN SIK KULLANILAN FONKSİYONLAR:
#
# 1. TAM SAYI ÜRETME (randint):
# np.random.randint(alt_sinir, ust_sinir, size=(shape))
# ust_sinir dahil DEĞİLDİR.
# Örnek: 0-100 arası (100 hariç) rastgele sayılardan oluşan 3x3 matris:
# matris = np.random.randint(0, 100, size=(3, 3))
#
# 2. 0 İLE 1 ARASINDA ONDALIKLI SAYI (rand):
# np.random.rand(d0, d1, ...) -> Boyutları doğrudan paranteze yazarsın.
# Örnek: 0 ile 1 arasında 5 tane rastgele sayı:
# sayilar = np.random.rand(5) 
#
# 3. NORMAL (GAUSS) DAĞILIMLI SAYILAR (randn):
# np.random.randn(d0, d1, ...) 
# Ortalaması 0, standart sapması 1 olan (eksi değerler de alabilen) sayılar üretir.
# Örnek: İstatistiksel bir test için 2x2'lik normal dağılım:
# norm_matris = np.random.randn(2, 2)
#
# 4. MEVCUT BİR LİSTEDEN SEÇİM YAPMA (choice):
# np.random.choice(dizi, size=...)
# Örnek: Bir listeden rastgele 2 kişi seçme:
# kisiler = ['Ali', 'Ayşe', 'Veli', 'Fatma']
# secilenler = np.random.choice(kisiler, size=2)
#
# ------------------------------------------
# ÇOK ÖNEMLİ İPUCU: SEED (Tohum) KULLANIMI
# np.random.seed(42) 
# Kodun başına bunu yazarsan, "rastgele" üretilen sayılar sabitlenir.
# Kodu yarın da çalıştırsan, başka bilgisayarda da çalıştırsan 
# hep aynı rastgele sayıları elde edersin (Test ve debug için şarttır!).
# ==========================================

import numpy as np

#hep aynı rastgele sayıları üretir debuging için
np.random.seed(1)

#daha güncel metot
rng= np.random.default_rng()
print(rng.integers(1,100, size=(3,3)))

#daha eski metot
print(np.random.randint(1,100, size=(3,3)))
'''[[89 39 48]
 [13  6 18]
 [44  6 53]]'''

#array karıştırma
array= np.array([1,2,3,4,5])
rng= np.random.default_rng()
rng.shuffle(array)
print(array)

#array içinden rastgele eleman seçer
array= np.array([1,2,3,4,5])
rng= np.random.default_rng()
print(rng.choice(array))
print(rng.choice(array, size=3)) # 3 rastgele seçim yapar