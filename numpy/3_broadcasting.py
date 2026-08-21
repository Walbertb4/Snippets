# ==========================================
# NUMPY BROADCASTING (YAYINLAMA) ÖZETİ
# ==========================================
# Nedir?: Farklı boyuttaki array'ler arasında (for döngüsü yazmadan) 
# matematiksel işlem yapmayı sağlar. NumPy, küçük array'i sanal olarak 
# genişletip (ekstra bellek harcamadan) büyük array'in boyutuna uydurur.
#
# UYUM KURALLARI (Shape'ler sağdan sola doğru karşılaştırılır):
# İki boyutun eşleşip işlem görebilmesi için şu İKİ ŞARTTAN BİRİ geçerli olmalıdır:
# 1) Boyutlar birbiriyle TAMAMEN AYNI olmalıdır. (Örn: 3 ve 3)
# 2) Boyutlardan BİRİ KESİNLİKLE 1 olmalıdır. (1 olan boyut, diğerine göre genişletilir)
#
# Örnek:
# (3,5)
# (1,5)
# Olur
#
# Örnek:
# A shape: (4, 3)
# B shape:    (3) -> Başına sanal 1 eklenir (1, 3) gibi davranır. KURALLARA UYAR!
# İşlem sonucu shape: (4, 3) olur.
# ==========================================

import numpy as np

array1= np.array([[1,2,3,4]])
array2= np.array([[1],[2],[3],[4]])
print(array1.shape + array2.shape) # => (1, 4, 4, 1)

print(array1*array2) 
'''[[ 1  2  3  4]
    [ 2  4  6  8]
    [ 3  6  9 12]
    [ 4  8 12 16]]'''

