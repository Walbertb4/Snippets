import pandas as pd
import numpy as np

# ==========================================
# PANDAS DATAFRAME (VERİ ÇERÇEVESİ) ÖZETİ
# ==========================================
# Nedir?: 2 boyutlu (satır ve sütunlardan oluşan), etiketli veri yapısıdır.
# Excel tablolarının Python'daki karşılığıdır. 
#
# OLUŞTURMA ŞEKİLLERİ:
# import pandas as pd
#
# 1. SÖZLÜKTEN (DICTIONARY) OLUŞTURMA (En Yaygın Yöntem):
# (Key'ler sütun isimlerini, Value'lar ise o sütundaki verileri temsil eder)

data = {
    "Isim": ["Ali", "Ayşe", "Veli", "Fatma"],
    "Yas": [25, 30, 22, 28],
    "Maas": [40000, 50000, 35000, 45000]
}
df = pd.DataFrame(data)

# print(df)
"""
    Isim  Yas   Maas
0    Ali   25  40000
1   Ayşe   30  50000
2   Veli   22  35000
3  Fatma   28  45000
"""

# ------------------------------------------
# 1. VERİYİ İNCELEME (Temel Metotlar):
# df.head(2)    # Tablonun İLK 2 satırını getirir (Önizleme için harikadır).
# df.tail(2)    # Tablonun SON 2 satırını getirir.
# df.info()     # Sütun tiplerini ve boş (NaN) değer olup olmadığını gösterir.
# df.describe() # Sayısal sütunların istatistiksel özetini verir (ortalama, min, max).

# ------------------------------------------
# 2. VERİ SEÇME VE ERİŞİM:

# SÜTUN SEÇME:
# isimler_serisi = df["Isim"]  # Tek sütun seçersen sonuç bir Pandas Series olur!
# bazi_sutunlar = df[["Isim", "Maas"]]  # İKİ KÖŞELİ PARANTEZ! Sonuç yeni bir DataFrame olur.

# SATIR SEÇME (.loc ve .iloc ile):
# Tıpkı Series'lerdeki gibi çalışır.
# df.iloc[0]    # 0. sıradaki tüm satırı (Ali'nin bilgileri) getirir.
# df.iloc[0:2]  # İlk iki satırı getirir.

# BELİRLİ BİR HÜCREYİ SEÇME (Satır ve Sütun Kesişimi):
# Kural: df.loc[satır_etiketi, sütun_etiketi]
# df.loc[1, "Yas"]  # 1. indexli satırın (Ayşe), "Yas" sütunundaki değerini (30) getirir.
# df.iloc[1, 1]     # Aynı işlemi tamamen index numaralarıyla (1. satır, 1. sütun) yapar.

# ------------------------------------------
# 3. SÜTUN EKLEME VE SİLME:

# Yeni Sütun Ekleme:
# df["Sehir"] = ["Istanbul", "Ankara", "Izmir", "Bursa"]

# Sütun Silme (drop):
# axis=1 sütun demek, axis=0 satır demektir. 
# inplace=True parametresi, orijinal tabloyu kalıcı olarak günceller.
# df.drop("Yas", axis=1, inplace=True) 
# ==========================================

# İki series'i birleştirmek
s1= pd.Series([10,20,30])
s2= pd.Series(["a","b","c"])
data={"numbers":s1,"letters":s2}
dataframe=pd.DataFrame(data)
print(dataframe)
"""
   numbers letters
0       10       a
1       20       b
2       30       c
"""

#dataframe oluşturma
df=pd.DataFrame([1,2,3,4,5])
print(df)
"""
   0
0  1
1  2
2  3
3  4
4  5
"""

df=pd.DataFrame([[1,2,3,4,5],[6,7,8,9,0]])
print(df)
"""
   0  1  2  3  4
0  1  2  3  4  5
1  6  7  8  9  0
"""

data=[[10,"ali"],[20,"mehmet"],[39,"bugra"]]
df=pd.DataFrame(data=data,columns=["points","names"])
print(df)
"""
   points   names
0      10     ali
1      20  mehmet
2      39   bugra
"""

#dictionary ile dataframe oluşturma
data={"Names":["bombo","bamba","bimba","bumba"],"Points":[10,32,45,64],"Cars":["bmw","mercedes","opel","ferrari"]}
df=pd.DataFrame(data,index=[10,20,30,40])
print(df)
"""
    Names  Points      Cars
10  bombo      10       bmw
20  bamba      32  mercedes
30  bimba      45      opel
40  bumba      64   ferrari
"""
