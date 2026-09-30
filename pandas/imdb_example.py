import pandas as pd

df=pd.read_csv("pandas/datasets/imdb.csv")

# 1- Dosyada hakkındaki bilgiler.
print(df.info())
# 2- ilk 5 kaydı gösterin
print(df.head(5))
# 3- ilk 10 kaydı gösterin
print(df.head(10))
# 4- Son 5 kaydı gösterin
print(df.tail(5))
# 5- Son 10 kaydı gösterin
print(df.tail(10))

# 6- Sadece Movie_Title kolonunu alın.
print(df["Movie_Title"])
# 7- Sadece Movie_Title kolonunu içeren ilk 5 kaydı alın.
print(df["Movie_Title"][:5])
# 8- Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın.
print(df[["Movie_Title","Rating"]][:5])
# 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın.
print(df[["Movie_Title","Rating"]][-7:])
# 10- Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alın.
print(df[["Movie_Title","Rating"]][5:10])
# 11- Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 ve üstünde olan kayıtlardan ilk 50 tanesini alınız.
print(df[df["Rating"]>=8.0][["Movie_Title","Rating"]].head(50))
# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.
print(df[(df["YR_Released"]>=2014)&(2015>=df["YR_Released"])]["Movie_Title"])
# 13- Değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı 8 ile 9 arasında olan filmleri listeleyiniz.
print(df[(df["Num_Reviews"]>=100000) | (df["Rating"].between(8,9))]["Movie_Title"])

