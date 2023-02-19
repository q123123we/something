import datetime

def user_birthday(birthday):
    user_bd = []
    birthday = datetime.date(year=int(input("Введите год вашего рождения: ")), month=int(input("Введите месяц вашего рождения: ")), day=int(input("Введите день вашего рождения: ")))
    user_bd.append(birthday)
    print("Ваш день рождения: " + str(user_bd))
user_birthday(birthday=user_birthday)
1
