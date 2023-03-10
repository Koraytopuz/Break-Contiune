harfler="abcdr"
while True:
    tahmin=input("bir harf tahmin edin")
    if tahmin not in harfler:
        break
    else:
        print("dogru tahmin")