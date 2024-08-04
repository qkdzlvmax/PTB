# loai = int(input("Loai giay to:"))
# sotrang = int(input("So trang:"))
# if loai == 1:
#     print("So luong giay can dung:", sotrang)
# if loai == 2:
#     print("So luong giay can dung:", sotrang//2)
# kwh = int(input("Nhap so tien tieu thu:"))
# if kwh < 50:
#     print("So tien dien can phai tra:", kwh*1700)
# elif kwh < 100:
#     print("So tien dien can phai tra:", 50*1700+(kwh-50)*1900)
# elif kwh < 200:
#     print("So tien dien can phai tra:", 50*1700+50*1900+(kwh-100)*2100)
# elif kwh > 200:
#     print("So tien dien can phai tra:", 50*1700+50*1900+100*2100+(kwh-200)*3000)
n = int(input)
if n < 17:
    print(n*7000,end = "")
elif n < 50:
    print(16*7000+(n-16)*8500,end = "")
else:
    print(16*7000+34*8500+(n-49)*100000,end ="")

