import tkinter as tk
import random

def generate_password():

    password = ''
    if lowercase.get():
        password += random.choice('abcdefghijklmnopqrstuvwxyz')
    if digits.get():
        password += random.choice('0123456789')
    if special_chars.get():
        password += random.choice('!@#$%')


    password_length = password_slider.get()
    while len(password) < password_length:
        if lowercase.get():
            password += random.choice('abcdefghijklmnopqrstuvwxyz')
        if digits.get():
            password += random.choice('0123456789')
        if special_chars.get():
            password += random.choice('!@#$%')

    # Перемешайте символы в пароле для большей безопасности
    password = list(password)
    random.shuffle(password)
    password = ''.join(password)

    result_label.config(text=f"Сгенерированный пароль: {password}")


root = tk.Tk()
root.title("Генератор паролей")


lowercase = tk.BooleanVar()
digits = tk.BooleanVar()
special_chars = tk.BooleanVar()

lowercase_checkbox = tk.Checkbutton(root, text="Включить строчные буквы", variable=lowercase)
lowercase_checkbox.pack()
digits_checkbox = tk.Checkbutton(root, text="Включить цифры", variable=digits)
digits_checkbox.pack()
special_chars_checkbox = tk.Checkbutton(root, text="Включить специальные символы", variable=special_chars)
special_chars_checkbox.pack()


password_slider = tk.Scale(root, from_=8, to=32, orient="horizontal", label="Длина пароля")
password_slider.pack()


generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
generate_button.pack()


result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()