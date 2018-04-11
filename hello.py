
print("Kullanici tarafindan girilen iki sayinin toplami programi")

num1 = int(input("birinci sayiyi giriniz :"))
num2 = int(input("ikinci sayiyi giriniz :"))


sum = int(num1) + float(num2)

print('{0} + {1} = {2}'.format(num1, num2, sum))

print('\n')

print("İki sayinin ortalamasini yazdirma")

num3 = 200
num4 = 5

division = int(num3) / int(num4)

print('{0} / {1} = {2}'.format(num3, num4, division))

print('\n')

print("Iki sayinin yer degistirmesi")

num5 = 75
num6 = 42


print('Oncesi')
print('Ilk Sayi:{0} '.format(num5))
print('Ikinci Sayi:{0} '.format(num6))
print('\n')

num5 = num5+num6
num6 = num5-num6
num5 = num5-num6

print('Sonrasi')
print('Ilk Sayi:{0} '.format(num5))
print('Ikinci Sayi:{0} '.format(num6))
