# ==========================================
# NUMPY AGGREGATE (TOPLULAŞTIRMA) FONKSİYONLARI ÖZETİ
# ==========================================
# Nedir?: Çok sayıda elemanı olan bir veriyi (array) özetleyerek 
# genellikle tek bir değere (skaler) dönüştüren işlemlerdir.
#
# Ne işe yarar?: Verinin bütünü (veya belirli bir ekseni) hakkında 
# istatistiksel veya genel bir özet çıkarır.
#
# En Sık Kullanılan Aggregate Fonksiyonları:
# np.sum(array)  -> Dizideki tüm elemanların toplamını verir.
# np.mean(array) -> Elemanların aritmetik ortalamasını hesaplar.
# np.max(array)  -> Dizideki en büyük değeri bulur.
# np.min(array)  -> Dizideki en küçük değeri bulur.
# np.std(array)  -> Standart sapma bulur. 
#
# ÖNEMLİ İPUCU: 
# Bu fonksiyonlar varsayılan olarak tüm array'i tek bir değere indirger.
# Ancak 'axis' parametresi kullanarak (örn: np.sum(array, axis=0)) 
# sadece sütunlar veya satırlar bazında da özetleme yapabilirsin.
# ==========================================

import numpy as np

array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])
print(np.sum(array)) # => 55
print(np.argmax(array)) # => 9 en büyük elemanın indeksi
print(np.argmin(array)) # => 0 en küçük elemanın indeksi

print(np.sum(array, axis=1)) # => [15 40] satırların elemanlarını toplar
print(np.sum(array, axis=0)) # => [ 7  9 11 13 15] sütunların elemanlarını toplar