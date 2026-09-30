# ==========================================
# PANDAS DATAFRAME - GROUPBY (GRUPLAMA) ÖZETİ
# ==========================================
# Nedir?: SQL'deki 'GROUP BY' mantığıyla aynıdır. Veriyi belirli kategorilere
# (departman, şehir, cinsiyet vb.) göre ayırır, her grup üzerinde toplu 
# matematiksel/istatistiksel işlemler yapar ve sonuçları tek bir tabloda birleştirir.
#
# TEMEL MANTIK (Split - Apply - Combine):
# 1. Split (Böl): Tabloyu verilen sütundaki kategorilere göre parçala.
# 2. Apply (Uygula): Her parça için ortalama (mean), toplam (sum) vb. hesapla.
# 3. Combine (Birleştir): Çıkan sonuçları tek bir özet tablo haline getir.

# 1. TEK SÜTUNA GÖRE GRUPLAMA VE TEMEL İŞLEMLER
# Departmanlara göre grupla ve sadece maaşların ortalamasını al:
# dep_maas_ort = df.groupby("Departman")["Maas"].mean()

# Şehirlere göre grupla ve toplam çalışan sayısını bul:
# sehir_calisan_sayisi = df.groupby("Sehir")["Calisan_ID"].count()

# 2. ÇOKLU SÜTUNA GÖRE GRUPLAMA
# Hem Departman hem de Cinsiyet kırılımında ortalama maaşları getir:
# kirilim = df.groupby(["Departman", "Cinsiyet"])["Maas"].mean()

# 3. ÇOKLU İSTATİSTİK UYGULAMA ( .agg() Metodu )
# Departman bazında maaşların hem ortalamasını, hem toplamını, hem de kişi sayısını bul:
# ozet = df.groupby("Departman")["Maas"].agg(["mean", "sum", "count"])

# Farklı sütunlara farklı işlemler uygulama (Sözlük ile):
# ozel_ozet = df.groupby("Departman").agg({
#     "Maas": "mean",   # Maaşların ortalamasını al
#     "Yas": "max",     # Yaşın en büyüğünü al
#     "Isim": "count"   # Toplam kişi sayısını say
# })

# 4. GRUP GRUP DOLAŞMA VE TEK BİR GRUBU ÇEKME
# Sadece "Yazılım" departmanında çalışanların tüm satırlarını getir:
# yazilimcilar = df.groupby("Departman").get_group("Yazılım")

# 5. ALTIN KURAL: reset_index() KULLANIMI
# Groupby yapıldığında gruplanan sütun otomatik olarak tablonun 'Index'i olur.
# Onu tekrar normal bir sütuna çevirip standart DataFrame formatına döndürmek için:
# temiz_tablo = df.groupby("Departman")["Maas"].mean().reset_index()
# ==========================================

import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}
#dataframe oluştur
df=pd.DataFrame(personeller)

print(df["Maaş"].sum()) # => tüm elemanların maaşlarını topla

print(df.groupby("Yaş").groups) # => tüm yaş elemanlarını grupla indexini ver 
# => {23: [4], 25: [1], 30: [0], 34: [5], 42: [6], 45: [2], 50: [3]}

print(df.groupby(["Departman","Semt"]).groups)# => departman ve semte göre grupla indexi ver
'''
{('Bilgi İşlem', 'Maltepe'): RangeIndex(start=4, stop=5, step=1),
('Bilgi İşlem', 'Tuzla'): RangeIndex(start=1, stop=2, step=1),
('Muhasebe', 'Maltepe'): RangeIndex(start=2, stop=3, step=1),
('Muhasebe', 'Tuzla'): RangeIndex(start=5, stop=6, step=1),
('İnsan Kaynakları', 'Kadıköy'): RangeIndex(start=0, stop=12, step=6),
('İnsan Kaynakları', 'Tuzla'): RangeIndex(start=3, stop=4, step=1)}
'''

print(df.groupby(["Departman","Semt"])["Maaş"].mean())# => departman ve semte göre grupla maaş ortalamasını al
'''
Departman         Semt   
Bilgi İşlem       Maltepe    2750.0
                  Tuzla      3000.0
Muhasebe          Maltepe    4000.0
                  Tuzla      6500.0
İnsan Kaynakları  Kadıköy    4750.0
                  Tuzla      3500.0
'''

#for  döngüsünde kullanımı
semtler= df.groupby("Semt")
for name, info in semtler:
    print(name)
    print(info)
'''
Kadıköy
        Çalışan         Departman  Yaş     Semt  Maaş
0  Ahmet Yılmaz  İnsan Kaynakları   30  Kadıköy  5000
6   Mustafa Can  İnsan Kaynakları   42  Kadıköy  4500
Maltepe
         Çalışan    Departman  Yaş     Semt  Maaş
2  Hasan Korkmaz     Muhasebe   45  Maltepe  4000
4      Ali Turan  Bilgi İşlem   23  Maltepe  2750
Tuzla
       Çalışan         Departman  Yaş   Semt  Maaş
1   Can Ertürk       Bilgi İşlem   25  Tuzla  3000
3  Cenk Saymaz  İnsan Kaynakları   50  Tuzla  3500
5  Rıza Ertürk          Muhasebe   34  Tuzla  6500
'''

#Departman başına maaş ortalaması hesaplama
for name1,group1 in df.groupby("Departman"):
    print(name1)
    print(group1)
    ortmaas=df[df["Departman"] == "Bilgi İşlem"]["Maaş"].mean()
    print(f"Ortalama Maaş: {ortmaas}")

#Gruplandırma yapıp içinden tek bir grup almak
print(df.groupby("Semt").get_group("Kadıköy"))
'''
        Çalışan         Departman  Yaş     Semt  Maaş
0  Ahmet Yılmaz  İnsan Kaynakları   30  Kadıköy  5000
6   Mustafa Can  İnsan Kaynakları   42  Kadıköy  4500
'''

#Çalışanlardan maaşı 4000'den yüksek olanları semte göre filtrele ve isimlerini liste olarak ver
print(df[df['Maaş'] > 4000].groupby("Semt")["Çalışan"].apply(list))
'''
Semt
Kadıköy    [Ahmet Yılmaz, Mustafa Can]
Tuzla                    [Rıza Ertürk]
Name: Çalışan, dtype: object
'''

#Maaş tablosu oluşturup içinden istenilen veriyi çekme
print(df.groupby("Departman")["Maaş"].agg(["mean", "sum", "count"]))
print(df.groupby("Departman")["Maaş"].agg(["mean", "sum", "count"])["mean"].iloc[1])
'''
                         mean    sum  count
Departman                                  
Bilgi İşlem       2875.000000   5750      2
Muhasebe          5250.000000  10500      2
İnsan Kaynakları  4333.333333  13000      3
5250.0
'''