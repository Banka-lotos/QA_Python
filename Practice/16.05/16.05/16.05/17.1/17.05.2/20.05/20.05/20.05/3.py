

def val_text_len(text, max_len):
    if len(text) <= max_len:
        return True
    else:
        return False

# Пример
text = "текс пров длинырппррпрпрпрпрпрп"
max_len = 20

if val_text_len(text, max_len):
    print("Длина не превыш max")
else:
    print("Длина прев max")