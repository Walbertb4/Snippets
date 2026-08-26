# ==========================================
# PANDAS VERİ OKUMA (DATA IMPORT) ÖZETİ - GÜNCEL KULLANIM
# ==========================================
# Nedir?: Dışarıdaki bir dosyayı (CSV, Excel, JSON vb.) Python ortamına 
# bir Pandas DataFrame (Tablo) olarak çekme işlemidir.
#
# import pandas as pd
#
# 1. CSV DOSYASI OKUMA (En Sık Kullanılan)
# CSV (Comma Separated Values) genelde virgül veya noktalı virgülle ayrılır.
# df = pd.read_csv("veriler.csv")
#
# Hayat Kurtaran Parametreler (CSV):
# df = pd.read_csv("veriler.csv", sep=";")        # Eğer veri virgül yerine noktalı virgülle ayrılmışsa.
# df = pd.read_csv("veriler.csv", encoding="utf-8") # Türkçe karakter hatası (ş, ğ, ı) alıyorsan.
# df = pd.read_csv("veriler.csv", index_col=0)    # İlk sütunu otomatik index yapmak için.
#
# 2. EXCEL DOSYASI OKUMA
# GÜNCEL NOT: Pandas artık Excel okumak için arka planda 'openpyxl' 
# kütüphanesine ihtiyaç duyar (pip install openpyxl ile kurmalısın).
# df = pd.read_excel("rapor.xlsx")
#
# Spesifik Bir Sayfayı (Sheet) Okumak İçin:
# df = pd.read_excel("rapor.xlsx", sheet_name="Sayfa1")
#
# 3. JSON DOSYASI OKUMA
# API'lerden veya web'den gelen hiyerarşik verileri okumak için kullanılır.
# df = pd.read_json("kullanicilar.json")
#
# 4. KLASÖR DİZİNİ (PATH) BELİRTMEK
# Eğer dosya kodunla aynı klasörde değilse tam yolunu yazmalısın.
# Windows'da ters slash (\) bazen kaçış karakteri sayılır, bu yüzden 
# yolun başına 'r' (raw string) koymak en güvenli modern yöntemdir:
# df = pd.read_csv(r"C:\Users\Masaustu\Projeler\Veriler\data.csv")
#
# ==========================================

import pandas as pd
import sqlite3

#csv okuma
df=pd.read_csv("pandas/datasets/sample.csv")

#json okuma
df=pd.read_json("pandas/datasets/sample.json",encoding="UTF-8") # encoding kısmı türkçe karakterler için

#excel okuma
df=pd.read_excel("pandas/datasets/sample.xlsx")  # xlrd ve openpyxl kütüphanesi indirilmeli.

#sql okuma
connection=sqlite3.connect("pandas/datasets/sample.db")
df=pd.read_sql_query("SELECT * FROM students", connection)

print(df)