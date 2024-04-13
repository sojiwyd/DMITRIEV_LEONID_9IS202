# by LEONID DMITRIEV 9IS-202

purchases = []
coins = [1, 5, 7, 10, 15]
paymentcoins = []

def coinChange(coins, amount):
    changecoin = []
    coins.sort(reverse=True)
    length = len(coins)
    i = 0
    while amount > 0:
        if coins[i] <= amount:
            changecoin.append(coins[i])
            amount -= coins[i]
            coins.pop(i)
            length -= 1
        else:
            i += 1
        if i >= length: 
            break
    print(f"Ваши сдача: {changecoin}")

while True:
    print(purchases)
    print("1. Выбрать товары для покупки")
    print("2. Удалить товар из корзины")
    print("3. Оплатить заказ")
    choice_purchases = input("Введите цифру:")
    
    if choice_purchases == "1":
         print("Список товаров:")
         print("1. Хлеб: 30 руб.")
         print("2. Молоко: 50 руб.")
         print("3. Шоколад: 60 руб.")
        
         choice_product = input("Введите номер товара:")
         if choice_product == "1":
             Bread = {"product": "Bread", "price": 30}
             purchases.append(Bread)
         elif choice_product == "2":
             Milk = {"product": "Milk", "price": 50}
             purchases.append(Milk)
         elif choice_product == "3":
             Chocolate = {"product": "Chocolate", "price": 60}
             purchases.append(Chocolate)
         else:
             print("Неверный номер товара")
    
    elif choice_purchases == "2":
         print(purchases)
         delete_product = input("Введите номер предмета, который вы хотите удалить:")
         if delete_product == "1":
             purchases.pop(0)
         elif delete_product == "2":
             purchases.pop(1)
         elif delete_product == "3":
             purchases.pop(2)
         else:
             print("Неверный номер товара")
            
    elif choice_purchases == "3":
        print(f"Ваш список товаров: {purchases}") 
        paysum = 0
        for item in purchases:
            paysum += item["price"]
        print(f"Сумма вашего заказа составляет: {paysum}") 
        
        while True:
            paymentcoin = input("Введите монету, которые вы хотите отдать(для отмены напишите y):")
            paymentcoins.append(paymentcoin)
            if paymentcoin == "y":
                paymentcoins.pop(-1) 
                break
        
        amount = sum([int(item) for item in paymentcoins]) - int(paysum)
        coinChange(coins, amount)
        int_paymentcoins = [int(item) for item in paymentcoins]
        coins += int_paymentcoins
        print(f"МОНЕТЫ, КОТОРЫЕ ОСТАЛИСЬ В КАССЕ: {coins}")
        break