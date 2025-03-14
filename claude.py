def sinav():
    puan = 0
    toplam_soru = 3
    
    # 1. Soru
    print("\nSoru 1: Türkiye'nin başkenti neresidir?")
    cevap1 = input("Cevabınız: ").lower()
    if cevap1 == "ankara":
        print("Doğru!")
        puan += 1
    else:
        print("Yanlış. Doğru cevap: Ankara")
    
    # 2. Soru
    print("\nSoru 2: 15 + 25 kaçtır?")
    cevap2 = input("Cevabınız: ")
    if cevap2 == "40":
        print("Doğru!")
        puan += 1
    else:
        print("Yanlış. Doğru cevap: 40")
    
    # 3. Soru
    print("\nSoru 3: Dünyanın uydusu nedir?")
    cevap3 = input("Cevabınız: ").lower()
    if cevap3 == "ay":
        print("Doğru!")
        puan += 1
    else:
        print("Yanlış. Doğru cevap: Ay")
    
    # Sonuç
    yuzde = (puan / toplam_soru) * 100
    print(f"\nSınav bitti!")
    print(f"Toplam puanınız: {puan}/{toplam_soru}")
    print(f"Başarı yüzdeniz: %{yuzde}")

# Programı başlat
print("Sınav uygulamasına hoş geldiniz!")
sinav()