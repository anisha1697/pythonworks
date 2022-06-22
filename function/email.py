def validate_email(email):
    return email.endswith("@gmail.com")
print(validate_email("abc@gmail.com"))