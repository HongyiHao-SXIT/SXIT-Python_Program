run_list = ["0分钟","20分钟","40分钟","60分钟"]
swim_list = ["0米","200米","400米","600米"]
calories_list = []
for i in range(len(run_list)):
    for j in range(len(swim_list)):
        calories_list.append(i * 200 + j * 100)
print("卡路里列表：",calories_list)
print(f"运动计划中最多消耗{max(calories_list)}卡路里，最少消耗{min(calories_list)}卡路里")