def check_password_strength(password):
    # Şifre uzunluğunu kontrol etme
    if len(password) < 8:
        return "Şifre çok kısa. En az 8 karakter içermelidir."

    # Büyük harf kontrolü
    if not any(char.isupper() for char in password):
        return "Şifre en az bir büyük harf içermelidir."

    # Küçük harf kontrolü
    if not any(char.islower() for char in password):
        return "Şifre en az bir küçük harf içermelidir."

    # Rakam kontrolü
    if not any(char.isdigit() for char in password):
        return "Şifre en az bir rakam içermelidir."

    # Özel karakter kontrolü
    special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    if not any(char in special_characters for char in password):
        return "Şifre en az bir özel karakter içermelidir."

    return "Şifre güvenli."


# Kullanıcıdan şifre isteme
password = input("Şifre girin: ")

# Şifrenin güvenliğini kontrol etme
result = check_password_strength(password)
print(result)
