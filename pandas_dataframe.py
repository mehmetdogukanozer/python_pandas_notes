#DATAFRAME OPERASYONLARI VE METOTLARI

import pandas as pd

df = pd.read_csv("pokemon.csv")


#df.head()  #ilk baştaki 5 satırı gösterir. Parantez içine sayı koyarsak o sayı kadar gösterir

#df.describe()  # tablo değerlerini gösterir istatistik

#print(df["Name"])
#print(df["Sp. Atk"])

#print(df["HP"]> 100) # TRUE FALSE DEĞER VERİYOR tek tek bakıyor verilere ve 100 üstü olanları true olmayanları false olarak gösteriyor.
"""
hp_deneme = df["HP"] > 100

print(df[hp_deneme])
"""

#print(df[(df["Name"] == "Abra") | (df["Name"] == "Kadabra") | (df["Name"] == "Alakazam") ])

#print(df[(df["Total"] >= 680) | (df["Name"] == "Flareon")])


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
def harf(abc):
    return str(abc)[:2]


df["harf"] = df["Name"].apply(harf) #içine aldığı fonkisyonu datay ekliyor. 

df.drop("harf", axis=1, inplace=True )

print(df)

"""
#pokemonlara level atayıp dataya yazma

def OP(power):

    if power < 320:
        return "*"
    elif power < 430:
        return "**"
    elif power < 500:
        return "***"
    else:
        return "****"             


df["Star"] = df["Total"].apply(OP) #apply cok yavas onun yerine vectorize komutu daha kullanışlı

print(df[df["Star"] == "****"])



#Sıralama .sort_values()
"""
#print(df.sort_values("Total")) #Totale göre sıralama 

#print(df.sort_values("Total", ascending=False)) #Totali azalana göre sıralama
"""

#Değer sayma
"""
print(df["Type 1"].value_counts()) #type 1 değerlerindeki verilerin sayılarını sayıyor

"""

## nlargest & nsmallest
"""
print(df.nlargest(10, "HP")) # canı en yüksek 10 pokemonu gösterir

#nsmallest de tam tersi
"""

##Between 
"""
print(df[df["HP"].between(50,65)]) # canları 50 ile 65 arası olan pokemonlar

"""

## Özgün Değerler

"""
print(df["Type 1"].unique()) #type 1 içinde kaç tane eşsiz değer var onu gsterir

print(df["Type 1"].nunique()) #type 1 içindeki eşsiz değerlerin sayısını verir

"""

#Korelassyon  (iki değişkenin birbiri ile ne kadar ilişkili olduğunu gösterir )
 
""" 
print(df[["Attack", "Sp. Atk", "HP"]].corr()) #içindeki 3 değerin birbiriyle ilişkisini yazdıran kod

"""

#Değer değiştirme

df["Star"] = df["Star"].replace(to_replace="*", value="weak")

print(df)



