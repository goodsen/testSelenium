import csv

date = csv.reader(open(r'C:\\Users\gh\Desktop\loginParament.csv'))
#取用户的邮箱地址
for user in date:
    print(user[0])
