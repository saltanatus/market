from meat_milk import meat_milk_dep
from Bakingfinal import baking_dep
from cleaning_materials import cleaning_dep



def greeting():
    total_sum = 0
    print("Здраствуйте")
    greet = int(input("1: Здраствуйте\n 0: Выход\n Ваш выбор-->"))
    while greet > 0:
        print("""
            Добро пожаловать в наш супермаркет!
            Вы можете войти в один из отделов нашего маркета:
            1 - Мясо и молочная продукция
            2 - Хлеб и выпечка
            3 - Мыломойка
            4 - Посмотреть общий счёт
            5 - Пройти в кассу и расшитаться
            0 - Выйти из магазина
            Ваш выбор: 
            """)
        choice = int(input("Ваш выбор-->"))
        if choice == 1:
           total_sum += meat_milk_dep()
        elif choice == 2:
            total_sum += baking_dep()
        elif choice == 3:
            total_sum += cleaning_dep()
        elif choice == 4:
            print(total_sum)
        elif choice == 5:
            try:
                money = int(input("Введите количество денег: "))
                if money > total_sum:
                    change = money - total_sum
                    total_sum = 0
                    print(change)
                elif money == total_sum:
                    total_sum = 0
                    change = 0
                elif money < total_sum:
                    raise Exception("Вам недостаточно денег!")
            except ValueError:
                print("Вы ввели не число!")
            break



        elif choice == 0:
            break
greeting()
