import pickle

def not_defteri():
    try:
        with open("notlar.pkl", "rb") as dosya:
            notlar = pickle.load(dosya)
    except FileNotFoundError:
        notlar = []

    while True:
        print("1. Notları Görüntüle")
        print("2. Not Ekle")
        print("3. Not Düzenle")
        print("4. Not Sil")
        print("5. Çıkış")

        secim = input("Bir seçenek seçin: ")

        if secim == "1":
            if notlar:
                for i, notum in enumerate(notlar, 1):
                    print(f"{i}. {notum}")
            else:
                print("Not bulunmamaktadır.")
        elif secim == "2":
            yeni_not = input("Bir not girin: ")
            notlar.append(yeni_not)
            print("Not başarıyla eklendi.")
        elif secim == "3":
            if notlar:
                not_indisi = int(input("Düzenlemek istediğiniz notun numarasını girin: "))
                if 1 <= not_indisi <= len(notlar):
                    yeni_not = input("Yeni notu girin: ")
                    notlar[not_indisi - 1] = yeni_not
                    print("Not başarıyla düzenlendi.")
                else:
                    print("Geçersiz not numarası.")
            else:
                print("Not bulunmamaktadır.")
        elif secim == "4":
            if notlar:
                not_indisi = int(input("Silmek istediğiniz notun numarasını girin: "))
                if 1 <= not_indisi <= len(notlar):
                    silinecek_not = notlar.pop(not_indisi - 1)
                    print(f"{silinecek_not} başarıyla silindi.")
                else:
                    print("Geçersiz not numarası.")
            else:
                print("Not bulunmamaktadır.")
        elif secim == "5":
            with open("notlar.pkl", "wb") as dosya:
                pickle.dump(notlar, dosya)
            print("Not defteri kapatılıyor...")
            break
        else:
            print("Geçersiz bir seçenek girdiniz.")

not_defteri()
