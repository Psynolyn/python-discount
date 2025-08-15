def calculate_discount(price, discount_percent):
    if(discount_percent >= 20):
        return price*(1-(discount_percent/100))
    else:
        return price

user_price = int(input("Input price : "))
user_percent = int(input("Input discount %: "))

print(f'new item price is {calculate_discount(user_price, user_percent)}')