def check_stock(item):
    stock = {
        "apple": 10,
        "banana": 0,
        "mango": 5
    }
    return stock.get(item, "Item not found")