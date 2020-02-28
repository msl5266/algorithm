import matplotlib.pyplot as plt
import numpy as np

path = r"C:\Users\asus\Desktop\十年数据.txt"
data = []
with open(path, "r", encoding="utf-8") as fr:
    r = fr.readlines()
    for d in r:
        if len(d)<5:
            continue
        d = list(d.replace("\n", "").split(","))
        d = d[2:10]
        d.pop(6)
        temp = list(map(int,d))
        data.append(temp)
new_data = np.array(data)
x = new_data[:,0]
y = new_data[:,-1]
print(x)
# # # 散点图
# plt.scatter(x, y, color='r', marker='+')
# plt.show()
# 折线图
# fig = plt.figure(figsize=(100,100))
plt.plot(x, y, color='r',linestyle='-')
plt.show()