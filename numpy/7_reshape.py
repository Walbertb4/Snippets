# ==========================================
# NUMPY RESHAPE (YENİDEN BOYUTLANDIRMA) ÖZETİ
# ==========================================
# Nedir?: Bir array'in içindeki verileri (elemanları) değiştirmeden, 
# sadece satır ve sütun düzenini (shape) değiştirmektir.
#
# ALTIN KURAL: 
# Başlangıçtaki toplam eleman sayısı ile yeni durumdaki toplam eleman 
# sayısı BİREBİR AYNI olmak zorundadır. (Örn: 12 elemanlı bir dizi, 
# 3x4 veya 2x6 matris yapılabilir ama 3x3 yapılamaz!)
#
# KULLANIMI:
# a = np.array([1, 2, 3, 4, 5, 6])  # 1 Boyutlu (6 elemanlı)
# 
# b = a.reshape(2, 3)  # 2 satır, 3 sütunlu 2 Boyutlu matris yapar
# # Sonuç: [[1, 2, 3],
# #         [4, 5, 6]]
#
# HAYAT KURTARAN TAKTİK: '-1' Kullanımı
# Eğer boyutlardan birine -1 yazarsan NumPy'a şunu demiş olursun: 
# "Bir boyutu ben verdim, diğerini kalan eleman sayısına göre sen hesapla!"
# a.reshape(3, -1) -> 3 satır olmasını şart koşar, sütun sayısını (2) kendi bulur.
# ==========================================


# ==========================================
# NUMPY CONCATENATE & STACK (BİRLEŞTİRME) ÖZETİ
# ==========================================
# Nedir?: İki veya daha fazla array'i birbirine ekleme/yapıştırma işlemidir.
# DİKKAT: İşleme sokulan array'ler her zaman bir TUPLE () içinde verilmelidir!
#
# 1. CONCATENATE (Mevcut eksende uc uca yapıştırma)
# Yeni bir boyut(dimension) yaratmaz, sadece dizileri mevcut eksende uzatır.
# a = np.array([[1, 2]]) 
# b = np.array([[3, 4]])
#
# np.concatenate((a, b), axis=0) -> ALT ALTA birleştirir (Satır sayısı artar)
# np.concatenate((a, b), axis=1) -> YAN YANA birleştirir (Sütun sayısı artar)
#
# 2. STACK (Yeni bir boyutta üst üste dizme)
# Krepleri üst üste koyup 3 boyutlu bir krep kulesi yapmak gibidir. 
# Boyut sayısını (dimension) 1 artırır.
# x = np.array([1, 2, 3])  # 1 Boyutlu (1D)
# y = np.array([4, 5, 6])  # 1 Boyutlu (1D)
#
# np.stack((x, y)) # Sonucu 2 Boyutlu (2D) yapar.
# # [[1, 2, 3],
# #  [4, 5, 6]]
#
# KISAYOLLAR (Çok Sık Kullanılır):
# np.vstack((x, y)) -> Vertical Stack (Dikey/Alt alta birleştirme)
# np.hstack((x, y)) -> Horizontal Stack (Yatay/Yan yana birleştirme)
# ==========================================