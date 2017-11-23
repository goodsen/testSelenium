import csv #导入csv

#读取本地CSV文件
csv_file = csv.reader(open(r'C:\\Users\gh\Desktop\loginParament.csv'))#多加\防止转义
#循环输出每一行信息
for user in csv_file:
    print(user)