correct_answers = 0

# Soru 1
answer1 = input("2 + 2 kaç eder? ")
if answer1 == "4":
    correct_answers += 1

# Soru 2
answer2 = input("Dünyanın en büyük okyanusu hangisidir? ")
if answer2.lower() == "pasifik":
    correct_answers += 1

# Soru 3
answer3 = input("Yerçekimi hangi fiziksel kavrama dayanır? ")
if answer3.lower() == "kütle":
    correct_answers += 1

# Sonuçları göster
print("IQ Testi Sonuçları:")
print("Doğru cevaplanan sorular: ", correct_answers)
print("Yanlış cevaplanan sorular: ", 3 - correct_answers)
print("Toplam puan: ", correct_answers * 33.33)
