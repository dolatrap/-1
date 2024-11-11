import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 3

    print("Угадайте число от 1 до 10. У вас есть 3 попытки, чтобы его угадать.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Попытка {attempt}: Угадайте число: "))

        if guess == number_to_guess:
            print(f"Поздравляю! Вы угадали число с {attempt} попытки!")
            break
        else:
            print("Неправильно. Попробуйте снова.")

    else:
        print(f"Вы не угадали. Загаданное число было {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()