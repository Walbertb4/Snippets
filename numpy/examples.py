import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.

array=np.array([10,15,30,45,60])


# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.

array=np.arange(5,16)

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.

array=np.arange(50,101,5)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.

array=np.zeros(10)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.

array=np.ones(10)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.

array= np.linspace(0,100,5)

# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.

array=np.random.randint(10,30,size=5)

# 8- [-1 ile 1] arasında 10 adet sayı üretin.

array = np.random.uniform(-1, 1, 10)

# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.

matris=np.random.randint(10,51,size=(3,5))
print(matris)

# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız ?

satir_toplamlari = matris.sum(axis=1)
sutun_toplamlari = matris.sum(axis=0)

# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?

print(f"{np.max(matris)},{np.min(matris)},{np.mean(matris)}")

# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır ?

print(np.argmax(matris))

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

array=np.arange(10,21)
print(array[:3])

# 14- Üretilen dizinin elemanlarını tersten yazdırın.

print(array[::-1])

# 15- Üretilen matrisin ilk satırını seçiniz.

print(matris[0])

# 16- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir ?

print(matris[1,2])

# 17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.

print(matris[:,0])

# 18- Üretilen matrisin her bir elemanının karesini alınız.

print(matris**2)

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ? 
#     Aralığı (-50,+50) arasında yapınız.
matris=np.random.randint(-50,51,size=(3,5))
print(matris)
print(matris[(matris%2==0) & (matris>0)])
