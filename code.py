def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    if b==0:
        print("sayilar 0'a bolunemez")
        exit()
    return a/b
def hata():
    print("bir hata olustu")

print("islemler:\n")
print("""1. toplama
2. cikarma
3. carpma
4. bolme\n""")
secim=int(input("lutfen yapmak istediginiz islemi seciniz(1/2/3/4):"))
if secim>4 or secim<1:
    hata()
    exit()

sayi1=int(input("lutfen 1. sayiyi giriniz:"))
sayi2=int(input("lutfen 2. sayiyi giriniz:"))

if secim==1:
    print(f"{sayi1}+{sayi2}={toplama(sayi1,sayi2)}")

elif secim==2:
    print(f"{sayi1}-{sayi2}={cikarma(sayi1, sayi2)}")

elif secim==3:
    print(f"{sayi1}x{sayi2}={carpma(sayi1, sayi2)}")

elif secim==4:
    print(f"{sayi1}/{sayi2}={bolme(sayi1, sayi2)}")

