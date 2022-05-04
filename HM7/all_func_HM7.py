def get_int(word):
    """
    :param word: Приймає рядок який буде описувати для чого необхідно ввести число
    :return: Повертає число у форматі int
    """
    while True:
        my_number = input(word)
        try:
            return int(my_number)
        except:
            print("Помилка, спробуй ще раз ввести число")


def check_palindrome(num):
    """
    Функція для перевірки чи є число паліндромом
    :param num: Число яке перевіряємо
    :return: True якщо число паліндром і False якщо ні
    """
    num = str(num)
    left_bord = ""
    right_bord = ""
    centre = ""
    if int(num) < 10:
        return True
    elif len(num) % 2 == 0:
        for i in range(len(num)):
            if i < len(num) / 2:
                left_bord += num[i]
            else:
                right_bord += num[i]
        return left_bord == right_bord[::-1]
    else:
        for i in range(len(num)):
            if i < (len(num) / 2) - 1:
                left_bord += num[i]
            elif i > (len(num) / 2):
                right_bord += num[i]
            else:
                centre += num[i]
        return left_bord == right_bord[::-1]

if __name__ == '__main__':
    pass