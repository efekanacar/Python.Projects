a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))
c = input("işleminizi seçiniz(+,-,*,/):",)
if c == '+':
    print("Sonuç:",a+b)
elif c == '-':
    print("Sonuç:",a-b)
elif c == '*':
    print("Sonuç:",a*b)
elif c == '/':
    print("Sonuç:",a/b)
else:
    print("Geçersiz İşlem")
