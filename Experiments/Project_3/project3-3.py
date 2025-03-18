product_list = {
    "苹果": 5,
    "香蕉": 3,
    "牛奶": 8,
    "面包": 6,
    "巧克力": 10
}

while True:
    try:
        budget = float(input("请输入你的购物资金（元）："))
        if budget < 0:
            print("购物资金不能为负数，请重新输入。")
        else:
            break
    except ValueError:
        print("输入无效，请输入一个有效的数字。")

print("商品清单如下：")
for index, (product, price) in enumerate(product_list.items(), start=1):
    print(f"{index}. {product}: {price} 元")

purchased_products = []

while True:
    choice = input("请输入要购买的商品编号（输入 q 退出）：")
    if choice.lower() == 'q':
        break
    try:
        choice = int(choice)
        if 1 <= choice <= len(product_list):
            product = list(product_list.keys())[choice - 1]
            price = product_list[product]
            if budget >= price:
                purchased_products.append(product)
                budget -= price
                print(f"成功购买 {product}，剩余资金：{budget} 元")
            else:
                print("资金不足，无法购买该商品。")
        else:
            print("输入的编号无效，请重新输入。")
    except ValueError:
        print("输入无效，请输入有效的商品编号或 q 退出。")

if purchased_products:
    print("你购买的商品清单如下：")
    for product in purchased_products:
        print(product)
    print(f"购买后剩余资金：{budget} 元")
else:
    print("你没有购买任何商品。")
    