import random

coinf=int("0")
coinA=int("0")
coinz=int("0")
coina=int("0")

print("Loading...")

for i in range(1000000):
    coin1=random.randint(0,1)
    coin2=random.randint(0,1)
    coinA+=1
    coinALL=coin1+coin2

    if coinALL==0:
        coinf=coinf+1
        coinALL=int("3")
    if coinALL==1:
        coinz=coinz+1
        coinALL=int("3")
    if coinALL==2:
        coina=coina+1
        coinALL=int("3")

print("\n总共抛硬币次数:"+str(coinA))
print("两次为正:"+str(coinf))
print("一正一反:"+str(coinz))
print("两次为反:"+str(coina))
print("\n")