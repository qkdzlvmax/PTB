iphonesName = ["Iphone 20 Prm", "Iphone 16 Prm", "Iphone 6 Plus"]
iphonesPrice = [2000, 1000, 100]
yourMomney = 10000
yourShoppingItems = ["Iphone 20 Prm"]
youtShoppingItemsPrice = [2000]
while True:
    print("1.Xem tat ca Iphone co trong cua hang")
    print("2.Xem gio hang cua ban gi lao ?")
    print("3.Them Iphone vao gio hang")
    print("4.Them mat hang Iphone vao cua hang")
    print("5.Xoa Iphone ra khoi cua hang")
    print("6.Xoa Iphone ra khoi gio hang")
    print("7.Sua gia Iphone")
    print("8.Xoa het gio hang")
    print("9.Checkout")
    n = int(input("Nhap lua chon cua ban:"))
    if n == 1:
        print("==============UNOFFICIAL APPLE STORE==============")
        for i in range(len(iphonesName)):
            print("==", iphonesName[i], "-", iphonesPrice[i], "$")
        print("==============UNOFFICIAL APPLE STORE==============")
        x = input()
    elif n == 2:
        print("==============YOUR SHOPPING ITEMS==============")
        for i in range(len(yourShoppingItems)):
            print("==", yourShoppingItems[i])
        print("==============YOUR SHOPPING ITEMS==============")
        x = input()
    elif n == 3:
        print("==============UNOFFICIAL APPLE STORE==============")
        for i in range(len(iphonesName)):
            print("==", iphonesName[i], "-", iphonesPrice[i], "$")
        print("==============UNOFFICIAL APPLE STORE==============")
        n = int(input("Nhap Iphone ban muon mua(bat dau tu 0)"))
        yourShoppingItems.append(iphonesName[n])
        youtShoppingItemsPrice.append(iphonesName[n])
        print("Da them vao gio hang mat hang", iphonesName[n])
        x = input()
    elif n == 4:
        print("==============UNOFFICIAL APPLE STORE==============")
        for i in range(len(iphonesName)):
            print("==", iphonesName[i], "-", iphonesPrice[1], "$")
        print("==============UNOFFICIAL APPLE STORE==============")
        tenIphoneMoi = input("Nhap ten Iphone ban muon ban")
        giaIphoneMoi = int(input("Ban muon ban voi gia bao nhieu $:"))
        iphonesName.append(tenIphoneMoi)
        iphonesPrice.append(giaIphoneMoi)
        print("Da them", tenIphoneMoi, "voi muc gia", giaIphoneMoi)
        x = input()
    elif n == 5:
        print("==============UNOFFICIAL APPLE STORE==============")
        for i in range(len(iphonesName)):
            print("==", iphonesName[i], "-", iphonesPrice[1], "$")
        print("==============UNOFFICIAL APPLE STORE==============")
        vitrimuonxoa = int(input("Nhap Iphone ban muon xoa:"))
        print("Da xoa", iphonesName[vitrimuonxoa], "ra khoi cua hang")
        iphonesName.pop(vitrimuonxoa)
        iphonesPrice.pop(vitrimuonxoa)
        x = input()
    elif n == 6:
        print("==============YOUR SHOPPING ITEMS==============")
        for i in range(len(yourShoppingItems)):
            print("==", yourShoppingItems[i])
        print("==============YOUR SHOPPING ITEMS==============")
        vitrimuonxoa = int(input("Nhap Iphone ban muon xoa"))
        print("Da xoa", yourShoppingItems[vitrimuonxoa], "ra khoi gio hang")
        yourShoppingItems.pop(vitrimuonxoa)
        youtShoppingItemsPrice.pop(vitricuaiphone)
        x = input()
    elif n == 7:
        print("==============UNOFFICIAL APPLE STORE==============")
        for i in range(len(iphonesName)):
            print("==", iphonesName[i], "-", iphonesPrice[1], "$")
        print("==============UNOFFICIAL APPLE STORE==============")
        vitrimuonxoa = int(input("Nhap Iphone muon sua gia"))
        mucgiamoi = int(input("Nhap gia moi cua" + iphonesName[vitrimuonxoa]))
        iphonesPrice[vitrimuonxoa] = mucgiamoi
        print("Da sua gia thanh cong")
        x = input()
    elif n == 8:
        luachon = input("Ban co chac chan muon xoa het gio hang nay khong?")
        if luachon == 'y' or luachon == 'Y':
            yourShoppingItems.clear()
            print("Da xoa het gio hang")
            x = input()
    elif n == 9:
        TongTienCanTra = 0
        for iphone in yourShoppingItems:
            vitricuaiphone = iphonesName.find(iphone)
            mucgiacuaiphone = iphonesPrice[vitricuaiphone]
            TongTienCanTra += mucgiacuaiphone
        yourMomney -= TongTienCanTra

