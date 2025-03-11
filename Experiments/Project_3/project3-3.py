products = [("牛奶",5),("鸡蛋",20),("香蕉",10),("杯子",10)]
shopping_list = []
money = float(input("请输入您的购物资金："))
while True:
    print("*"*30)
    print("商品列表如下：")
    for index,product in enumerate(products):
        print(f"{index+1}.商品：{product[0]}，价格：{product[1]}")
    print("*" * 30)
    option = input("请输入您要购买的商品(退出请键入q)：")
    if option.isdigit():
        option = int(option)
        if 0 <= option-1 < len(products):
            option_product = products[option - 1]
            if option_product[1] <= money:
                shopping_list.append(option_product)
                money -= option_product[1]
                print("购买成功！")
            else:
                print(f"您的余额不足，余额为：{money}")
        else:
            print("您选的商品不存在！")
    elif option == "q":
        print("-" * 10, "购物清单", "-" * 10)
        for item in shopping_list:
            print(f"已购商品：{item[0]}，价格：{item[1]}")
        print("您的余额为：", money)
        break
    else:
        print("您的输入不合法！")
