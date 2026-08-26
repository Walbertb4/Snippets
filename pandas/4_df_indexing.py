# ==========================================
# PANDAS DATAFRAME - SATIR VE SÜTUN SEÇİMLERİ
# ==========================================
# Veri seti (df) içerisinden istediğimiz parçayı koparıp alma işlemleri.

# 1. SÜTUN (COLUMN) SEÇİMİ
# Tek bir sütun seçmek (Sonuç bir Pandas Series olur):
# isimler = df["Isim"]

# Çoklu sütun seçmek (İki köşeli parantez [[ ]] KULLANMAK ZORUNLUDUR! Sonuç DataFrame olur):
# ozel_tablo = df[["Isim", "Maas", "Sehir"]]

# 2. SATIR (ROW) SEÇİMİ (.loc ve .iloc)
# .loc  -> Senin atadığın özel index isimleriyle çalışır.
# .iloc -> Sadece klasik sayısal sıraya (0, 1, 2...) bakar.

# İlk satırı seçme (Sıra numarası ile):
# ilk_satir = df.iloc[0]

# Belirli satırları dilimleme (Slicing) - İlk 3 satırı alma:
# ilk_uc_satir = df.iloc[0:3]

# 3. BELİRLİ BİR HÜCREYİ / KESİŞİMİ SEÇME
# Altın Kural: df.loc[Satır, Sütun] veya df.iloc[Satır_No, Sütun_No]

# "Ali" indexine sahip kişinin sadece "Maas" bilgisini çekme:
# ali_maas = df.loc["Ali", "Maas"]

# 2. satırın 1. sütunundaki veriyi çekme (Tamamen numarayla):
# hucre_verisi = df.iloc[2, 1]

# Tüm satırları ( : ) ama sadece belirli bir sütunu alma:
# maaslar = df.loc[:, "Maas"]

# 4. KOŞULLU SEÇİM (FİLTRELEME - MASKING)
# Sadece maaşı 50.000'den büyük olan satırları (kişileri) komple seç:
# yuksek_maaslilar = df[df["Maas"] > 50000]

# Hem maaşı yüksek HEM DE İstanbul'da yaşayanlar:
# ozel_hedef = df[(df["Maas"] > 50000) & (df["Sehir"] == "İstanbul")]
# ==========================================

import pandas as pd
import numpy as np

# Rastgele sayılarla dolu dataframe oluşturma
df=pd.DataFrame(np.random.randint(1,100,size=(3,3)),columns=["column 1","column 2","column 3"], index=["A","B","C"])
print(df)
"""
   collumn 1  collumn 2  collumn 3
A         36         42         55
B         19         26         42
C          5         18         27
"""

# -----------------Column ile indexleme-----------------
print(df["column 1"])
"""
A    54
B    78
C    62
Name: column 1, dtype: int32
"""

print(df[["column 1","column 2"]])
"""
   column 1  column 2
A        23        91
B        25        43
C        72        58
"""

# -----------------Row ile indexleme-----------------
# .loc bizim verdiğimiz index adına göre arar.
# loc["row","column"] => satır, sütun araması
# loc["row"] => sadece satır araması
# loc[":","column"] => sadece sütun araması

print(df.loc["A"])
"""
column 1    94
column 2    97
column 3    45
Name: A, dtype: int32
"""

print(df.loc[["A","B"]])
"""
   column 1  column 2  column 3
A        60        17        21
B        55        25         7
"""

# .loc["row","column"]
print(df.loc["A","column 1"]) # => 27

# .iloc klasik indexlemeye göre arar.
print(df.iloc[[0,1]])
"""
   column 1  column 2  column 3
A        57        78        29
B        14        40        11
"""

# Örnekler
result = df.loc["A"] # A satırı
result = df.iloc[2] # 2. index satırı
result = df.loc[:,"column 1"] # tüm satırlar ve 1. sütun
result = df.loc[:,["column 1","column 2"]] # tüm satırlar ve sütun 1, sütun 2
result = df.loc[:,"column 1":"column 2"] # tüm satırlar ve sütun 1'den sütun 2'ye olan tüm sütunlar
result = df.loc[:,:"column 2"] # tüm satırlar ve sütun 2 ye kadar olan tüm sütunlar
result = df.loc["A":"B",:"column 2"] # A satırından B satırına kadar olan tüm satırlar ve sütun 2 ye kadar olan tüm sütunlar
result = df.loc[:"B",:"column 2"] # B' ye kadar olan tüm satırlar ve sütun 2 ye kadar olan tüm sütunlar
result = df.loc["A","column 2"] # A satırı ve sütun 2
result = df.loc["C","column 1"] # C satırı ve sütun 1
result = df.loc[["A","B"],["column 1","column 2"]] # A ve B satırı, sütun 1 ve sütun 2
print(result)

# Yeni sütun ekleme
df["column 4"] = pd.Series(np.random.randint(1, 100, size=3), index=["A", "B", "C"]) # 1. yöntem
df["column 4"] = np.random.randint(1, 100, size=3) # 2. yöntem
df["column 5"] = df["column 1"] + df["column 3"]
print(df)

# Sütun silme
df.drop("column 5", axis = 1, inplace = True)
print(df)

df.drop("A",axis=0)
print(df)