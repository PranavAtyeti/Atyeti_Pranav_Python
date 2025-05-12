from shop import calculate_bill, check_stock

item = "apple"
price = 20
quantity = 3

stock = check_stock(item)
print(f"{item}: {stock}")

if isinstance(stock,int) and stock>= quantity:
    total = calculate_bill(price, quantity)
    print(f"Total bill for {quantity} {item}(s): ${total}")
else:
    print("Stock out")