# ==========================================
# PANDAS SERIES (PANDAS SERİLERİ) ÖZETİ
# ==========================================
# Nedir?: Tek boyutlu (1D), etiketli (indexli) bir veri yapısıdır. 
# Excel'deki tek bir sütuna benzer. Farklı veri tiplerini (int, string vs.) tutabilir.
#
# NumPy'dan En Büyük Farkı: NumPy'da indexler her zaman 0, 1, 2.. diye giderken,
# Pandas serilerinde indexleri (etiketleri) biz belirleyebiliriz (Örn: "A", "B", "Ocak").
#
# KULLANIM VE OLUŞTURMA ŞEKİLLERİ:
# import pandas as pd  # Önce kütüphaneyi çağırmayı unutma!
#
# 1. LİSTELERDEN SERİ OLUŞTURMA (Özel İndex ile):
# veriler = [85, 90, 75]
# isimler = ["Ali", "Ayşe", "Can"]
#
# pd.Series(data=veriler, index=isimler)
# # ÇIKTI:
# # Ali     85
# # Ayşe    90
# # Can     75
#
# 2. SÖZLÜKTEN (DICTIONARY) SERİ OLUŞTURMA:
# (Sözlüğün key'leri otomatik olarak index, value'ları veri olur)
# maaslar = {"Müdür": 50000, "Asistan": 30000}
# s = pd.Series(maaslar)
#
# ------------------------------------------
# EN ÇOK KULLANILAN ÖZELLİKLER (Attributes):
# s = pd.Series([10, 20, 30], index=["A", "B", "C"])
#
# s.values -> Sadece verileri bir NumPy array olarak döndürür: [10, 20, 30]
# s.index  -> Sadece etiketleri döndürür: Index(['A', 'B', 'C'])
#
# VERİYE ERİŞİM:
# s["A"]   -> "A" indexindeki veriyi (10) getirir.
# ==========================================

# ==========================================
# PANDAS INDEXING (.loc ve .iloc) - GÜNCEL KULLANIM
# ==========================================
# UYARI: Özel index atanmış serilerde s[0] gibi doğrudan köşeli 
# parantez kullanımı Pandas 2.0+ ile kaldırılmıştır!
#
# s = pd.Series([20, 30, 40, 50], index=['a', 'b', 'c', 'd'])
#
# 1. .iloc (Integer Location - Sayısal Sıra ile Erişim):
# Sadece klasik 0, 1, 2 gibi sıra numaralarına bakar. 
# Senin atadığın index isimlerini tamamen görmezden gelir.
#
# s.iloc[0]  -> 20 (Dizideki 0. sıradaki eleman)
# s.iloc[-1] -> 50 (Dizideki en son eleman)
# s.iloc[0:2] -> 20, 30 (Slicing/Dilimleme de yapılabilir)
#
# 2. .loc (Location - Etiket İsimleriyle Erişim):
# SADECE senin atadığın özel index isimleriyle (etiketlerle) çalışır.
#
# s.loc['a'] -> 20 ('a' etiketindeki eleman)
# s.loc['d'] -> 50 ('d' etiketindeki eleman)
# ==========================================

import pandas as pd
import numpy as np

#Series oluşturma
#numpy'de tüm veri tipi aynı olmak zorundayken pandas'da farklı olabilir.
strings=["a","b","c","20"]
series=pd.Series(strings)
print(series)
"""
0    a
1    b
2    c
3    20
dtype: str
"""

#index'i de kendimiz belirleyebilriz.
series=pd.Series(strings, index=["ali","mehmet","ayse","bugra"])
names=["ali","mehmet","ayse","bugra"]
series=pd.Series(strings, index=names)
print(series)
"""
ali        a
mehmet     b
ayse       c
bugra     20
dtype: str
"""

#dictionary bilgisinide series'e çevirebiliriz.
dictionary={"elma":10,"armut":20,"kiraz":15,"portakal":35}
series=pd.Series(dictionary)
print(series)
"""
elma        10
armut       20
kiraz       15
portakal    35
dtype: int64
"""

#numpy array'i pandas series'i olarak kullanmak
numbers=np.array([1,2,3,4,5])
series=pd.Series(numbers,index=["a","b","c","d","e",])
print(series)
"""
a    1
b    2
c    3
d    4
e    5
dtype: int64
"""

#numpy ile beraber kullanım örneği
random_numbers=np.random.randint(10,90,5)
series=pd.Series(random_numbers)
print(series)
"""
0    56
1    46
2    28
3    54
4    88
dtype: int32
"""

#Series içindeki elemanlara erişmek
numbers=[1,2,3,4,5]
letters=["a","b","c","d","e",]
series=pd.Series(numbers,index=letters)
print(series["a"]) # => 1
#print(series[0]) # => pandas'dan kaldırıldı. yerine iloc(klasik index) ve loc(kendi atadığımız index) eklendi.
print(series.iloc[0]) # => 1
print(series.loc["a"]) # => 1

print(series[["a","d"]])
"""
a    1
d    4
dtype: int64
"""

print(series[:2])
"""
a    1
b    2
dtype: int64
"""

#numpy komutları pandas series'lerde de kullanılabilir
print(series.shape) # => (5,)
print(series.sum()) # => 15
print(series.max()) # => 5
print(series.mean()) # => 3.0

print(series + series)
"""
a     2
b     4
c     6
d     8
e    10
dtype: int64
"""

print(series + 10)
"""
a    11
b    12
c    13
d    14
e    15
dtype: int64
"""

print(np.sqrt(series))
"""
a    1.000000
b    1.414214
c    1.732051
d    2.000000
e    2.236068
dtype: float64
"""

evens= series[series%2 == 0]
print(evens)
"""
b    2
d    4
dtype: int64
"""

print(series>=3)
"""
a    False
b    False
c     True
d     True
e     True
dtype: bool
"""

#örnek
opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","Grandland","insignia"])
total = opel2018 + opel2019
print(total)

"""
Grandland     NaN
astra        60.0
corsa        60.0
insignia     20.0
mokka         NaN
dtype: float64
"""