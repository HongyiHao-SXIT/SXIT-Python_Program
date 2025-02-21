weight = float(input("请输入您的体重(kg):"))

height = float(input("请输入您的身高(m):"))

bmi = weight / pow(height, 2)

print(f"BMI 的值为：{bmi:.2f}")

if bmi < 18.5:
    level = "偏瘦，体重太轻了，要增加营养哦"
elif 18.5 <= bmi < 24:
    level = "正常，您的身体非常健康，太棒啦"
elif 24 <= bmi < 28:
    level = "偏胖，规律作息、合理饮食，会变得健康哦"
else:
    level = "肥胖，保持健康的身体是爱护自己的表现，要运动起来呀"

print("身体状况为：", level)