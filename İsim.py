def kullanici_dogrula():
    kullanici_adi = input("Kullanıcı adınızı girin: ")

    if kullanici_adi.lower() == "elif":
        print("Elif")
    else:
        print("Hatalı kullanıcı adı.")

if __name__ == "__main__":
    kullanici_dogrula()
