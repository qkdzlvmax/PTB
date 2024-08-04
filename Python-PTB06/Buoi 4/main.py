# n = int(input())
# if n % 2 ==0:
#     print(n, "la so chan")
# else:
#     print(n, "la so le")
# if n == 0:
#     print(n, "khong phai so chan khong phai so le")

# n = int(input("Vui long chon nhan vat"))
# if n == 1:
#     print("Ban chon Songoku")
# elif n == 2:
#     print("Ban chon Vegeta")
# elif n == 3:
#     print("Ban chon Black-Goku")
# elif n == 4:
#     print("Ban chon Chi Chi")
# elif:
#     print("Mr,Beast toi chon ban")

#Cau 1
print("Chao mung den voi ung dung Math Quiz - Lop PTB06")
print("Moi cau hoi co 4 dap an trac nghiem - Dung +1 diem - Sai - 2 diem")
print("Co tong cong la 10 cau hoi")
CauHoi = "1 + 1 = may ?"
print("Cau hoi dau tien", CauHoi)
LuaChon = "1. 0  2. 2  3. 3  4. 4"
print("Lua chon:", LuaChon)
DapAn = int(input("Nhap lua chon"))
Score = 0
if DapAn == 1:
    score += 1
    print("Chinh xac! Diem cua ban la:", Score)
else:
    Score -= 1
    print("Khong chinh xac! Diem cua ban bay gio la:", Score)
#Cau 2
CauHoi = "Hoang Sa Truong Sa la cua nuoc nao?"
print("Cau hoi thu hai", CauHoi)
LuaChon = "1. Viet Nam  2. Cali  3. China  4. Campuchia"
print("Lua chon:", LuaChon)
DapAn = int(input("Nhap lua chon"))
Score = 0
if DapAn == 2:
    score += 1
    print("Chinh xac! Diem cua ban la:", Score)
else:
    Score -= 1
    print("Khong chinh xac! Diem cua ban bay gio la:", Score)