a = int(input("Nhap canh a:"))
b = int(input("Nhap canh b:"))
c = int(input("Nhap canh c:"))
if a + b <= c or a + c <= b or b + c <= a:
    print("Day khong phai la tam giac")
elif a == b == c:
    print("Day la tam giac deu")
elif a == b or a == c or b == c:
    print("Day la tam giac can")
elif a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + c**2 == b**2:
    print("Day la tam giac vuong")
else:
    print("Day la tam giac thuong")

   












exit()
toan = int(input("Vui long nhap diem toan cua ban:"))
anh = int(input("Vui long nhap diem anh cua ban:"))
van = int(input("Vui long nhap diem van cua ban:"))
while toan < 0 or toan > 10:
    toan = int(input("Vui long nhap lai diem toan (0 --> 10):"))
while anh < 0 or anh > 10:
    anh = int(input("Vui long nhap lai diem anh (0 --> 10):"))
while van < 0 or van > 10:
    van = int(input("Vui long nhap lai diem van (0 --> 10):"))
gpa = (toan + anh + van) / 3
print("Diem tong ket 3 mon cua ban la:", gpa)
exit()
TaiKhoanGame = "khoififai456"
MatKhauGame = "fifaiwilldie"
TKNguoiDung = input("Vui long nhap tk cua ban:")
MKNguoiDung = input("Vui long nhap mk cua ban:")
while TKNguoiDung != TaiKhoanGame or MKNguoiDung != MatKhauGame:
    print("Tai khoan hoac mat khau cua ban k dung, vui long nhap lai")
    TKNguoiDung = input("Vui long nhap lai tk cua ban")
    MKNguoiDung = input("Vui long nhap lai mk cua ban")
print("Dang nhap thanh cong")

import random
number = random.randint(0,1000)
SoNguoiDungNhapVao = int(input("Nhap so cua ban:"))
while SoNguoiDungNhapVao != number:
    if SoNguoiDungNhapVao == -1:
        print("Ban da dung tro choi")
        exit()
    elif SoNguoiDungNhapVao > 1000:
        print("Vui long nhap so tu khoang 0 --> 1000")
        SoNguoiDungNhapVao = int(input("Nhap so cua ban:"))
        continue
    elif number > SoNguoiDungNhapVao:
        print("So can tim lon hon", SoNguoiDungNhapVao)
    elif number < SoNguoiDungNhapVao:
        print("So can tim be hon", SoNguoiDungNhapVao)
    SoNguoiDungNhapVao = int(input("Nhap so cua ban:"))
print("You Win Nga")

