son=int(input("Son kirgazing (0-99 gacha):"))
onlik=int(son/10)
birlik=int(son%10)

if onlik==1 :
    print("O'n", end=" ")
elif onlik==2:
    print("Yigirma", end=" ")
elif onlik==3 :
    print("O'ttiz", end=" " )
elif onlik==4 :
    print("Qirq", end=" ")
elif onlik==5 :
    print("Ellik", end=" ")
elif onlik==6 :
    print("Oltmish", end=" ")
elif onlik==7 :
    print("Yetmish", end=" ")
elif onlik==8 :
    print("Sakson", end=" ")
elif onlik==9 :
    print("To'qson", end=" ")
else :
    print("Siz ikki xonali son kiritmadingiz.")
if birlik==1 :
    print("bir")
if birlik==2 :
    print("ikki")
if birlik==3 :
    print("uch")
if birlik==4 :
    print("to'rt")
if birlik==5 :
    print("besh")
if birlik==6 :
    print("olti")
if birlik==7 :
    print("yetti")
if birlik==8 :
    print("sakkiz")
if birlik==9 :
    print("to'qqiz")
