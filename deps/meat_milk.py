# отдел супермаркета, в котором продается хлеб и выпечка
def meat_milk_dep():
    meat_milk_items = {"говядина": 500, "курица": 400, "рыба": 550, "молоко": 70, "сыр": 110, "кефир": 80}
    shopping_cart = {}
    price = {}
    total_ = []
    choice = None
    while choice != "0":
        print(
                """
                    Вы в отделе мяса и молочных изделий! Выберите пункт меню:
                    0 - Выйти из этого отдела
                    1 - Просмотреть список товаров с ценами
                    2 - Найти товар по имени
                    3 - Добавить товар в корзину
                    4 - Очистить корзину
                    5 - Посмотреть список товаров в корзине
                    6 - Удалить определенный товар из корзины
                    7 - Завершить покупки и пройти на кассу, произвести расчет

                """ 
                )
        try:
            choice = int(input("Ваш выбор: "))
        except ValueError:
            print("Вы ввели не число")

        if choice == 0:
            print("До свидания, приходите к нам еще")
            break
            
        elif choice == 1:
            print(meat_milk_items)

        elif choice == 2:
            target_item = input("Какой товар Вы ищете? ").lower()
            if target_item in meat_milk_items:
                print(f"У нас есть {target_item} по цене {meat_milk_items[target_item]} сом")
            else:
                print("К сожалению, у нас нет того, что Вы ищете")
                    
        elif choice == 3:
            try:
                while choice == 3:
                    name_ = input("Введите название товара или 'выход': ").lower()
                    if name_ == "выход":
                        break
                    count_ = int(input("Введите количество товара: "))
                    shopping_cart[name_]=count_
                    price = meat_milk_items[name_]*shopping_cart[name_]
                    total_.append(price)
                    total_meat_milk = sum(total_)
                    print(f"Сумма покупок в корзине: {total_meat_milk}")
                print(f"""
                    Список товаров в корзине:
                    {shopping_cart}
                    Ваш счет составляет: {total_meat_milk} сом
                    """)
            except KeyError:
                print("Такого товара нет в продаже!")
            except ValueError:
                print("Количество товара должно быть числом!")

        elif choice == 4:
            shopping_cart.clear()
            print("Корзина очищена")

        elif choice == 5:
            print(f"""
            Товары в вашей корзине:
            {shopping_cart}
            """)

        elif choice == 6:
            try:
                name_del = input("Введите название товара для удаления: ").lower()
                del shopping_cart[name_del]
                print(f"""
                Товары в вашей корзине:
                {shopping_cart}
                """)
            except KeyError:
                print("Этого товара нет в корзине!")

        elif choice == 7:
            pass



