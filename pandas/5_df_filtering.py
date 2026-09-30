# ==========================================
# PANDAS DATAFRAME - FİLTRELEME (FILTERING) ÖZETİ
# ==========================================
# Nedir?: Koca bir tablonun içinden, sadece senin belirlediğin şarta 
# uyan satırları süzüp yeni bir tablo olarak alma işlemidir.
# 
# ALTIN KURAL: NumPy'daki gibi 'and/or' kelimeleri YERİNE 
# '&' (Ve) ile '|' (Veya) sembollerini kullanırız. 
# Çoklu şartlarda her koşul MUTLAKA parantez () içine alınmalıdır!

# 1. TEK KOŞULLU FİLTRELEME
# Sadece yaşı 30'dan büyük olan satırları (kişileri) getir:
# yasli_kullanicilar = df[df["Yas"] > 30]

# 2. ÇOK KOŞULLU FİLTRELEME 
# Hem yaşı 30'dan büyük OLSUN (&) Hem de maaşı 50.000'den fazla OLSUN:
# hedef_kitle = df[(df["Yas"] > 30) & (df["Maas"] > 50000)]

# Şehri "Ankara" OLSUN (|) Veya "İzmir" OLSUN:
# ankara_izmir = df[(df["Sehir"] == "Ankara") | (df["Sehir"] == "İzmir")]

# ------------------------------------------
# HAYAT KURTARAN FİLTRELEME METOTLARI
# ------------------------------------------

# 3. ÇOKLU DEĞER ARAMA ( .isin() Metodu )
# Üstteki "Veya" (|) işlemini uzun uzun yazmak yerine bir liste veririz.
# hedef_sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa"]
# secilenler = df[df["Sehir"].isin(hedef_sehirler)]

# 4. METİN (STRING) İÇİNDE KELİME ARAMA ( .str.contains() )
# Adının içinde "Ali" geçen herkesi bul (Ali, Alican, Alihan vb.):
# ali_olanlar = df[df["Isim"].str.contains("Ali")]

# 5. FİLTRELEME SONRASI BELİRLİ SÜTUNLARI GETİRME
# "Yaşı 30'dan büyük olanları bul ama TÜM BİLGİLERİNİ DEĞİL, 
# sadece 'Isim' ve 'Maas' sütunlarını getir:"
# ozel_sonuc = df[df["Yas"] > 30][["Isim", "Maas"]]
# ==========================================

import pandas as pd
import numpy as np

#random dataframe oluşturma
data = np.random.randint(10,100,size=(15,5))
df=pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5",])
print(df)
"""
    Column1  Column2  Column3  Column4  Column5
0        99       37       60       43       65
1        87       57       79       42       73
2        45       51       56       79       23
3        97       13       94       58       68
4        82       18       69       49       89
...
"""

print(df.head(10)) # => ilk 10 satırdaki tüm kayıtları getirir.
print(df.tail(10)) # => sondan 10 satırdaki tüm kayıtları getirir.

print(df["Column1"].head(5))
"""
0    66
1    24
2    35
3    81
4    37
Name: Column1, dtype: int32
"""
print(df[5:15][["Column1","Column2"]].head(5)) # => index 5'den index 9'a kadar olan Column1 ve Column2 deki verileri getirir.
"""
   Column1  Column2
5       57       94
6       98       41
7       70       38
8       37       98
9       81       42
"""


