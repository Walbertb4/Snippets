# ==========================================
# NUMPY FILTERING (FİLTRELEME / MASKELEME) ÖZETİ
# ==========================================
# Nedir?: Bir array içerisinden sadece senin belirlediğin şarta uyan 
# elemanları çekip alma işlemidir.
#
# Nasıl Çalışır?: Şartı yazdığında NumPy arka planda True ve 
# False değerlerinden oluşan bir "maske" oluşturur. Sonra 
# sadece True olan elemanları sana yeni bir array olarak döndürür.
#
# ÖRNEK SENARYO:
# fiyatlar = np.array([100, 250, 50, 400, 75, 300])
#
# 1. TEK KOŞULLU FİLTRELEME:
# # 150'den büyük olan fiyatları bul
# pahali_urunler = fiyatlar[fiyatlar > 150]
# # Sonuç: [250, 400, 300]
#
# 2. ÇOK KOŞULLU FİLTRELEME:
# # DİKKAT: Çoklu koşullarda 'and' yerine '&', 'or' yerine '|' kullanılır.
# # Her bir koşul parantez () içine alınmak ZORUNDADIR.
# # 100 ile 300 arasındaki (ikisi de dahil değil) fiyatları bul:
# orta_segment = fiyatlar[(fiyatlar > 100) & (fiyatlar < 300)]
# # Sonuç: [250]
#
# 3. SADECE BELİRLİ BİR DEĞERİ HARİÇ TUTMA (Eşit Değildir: !=):
# fiyatlar[fiyatlar != 50] # 50 dışındaki hepsini getirir.
# ==========================================

import numpy as np

ages= np.array([[10,22,18,89,11,24,13,25], 
                [30,33,35,47,49,12,32,34]])

print(ages[ages>=30]) # => [89 30 33 35 47 49 32 34]
teenagers= ages[ages<18]
print(teenagers) # => [10 11 13 12]

