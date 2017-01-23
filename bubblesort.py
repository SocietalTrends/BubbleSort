# -*- coding: utf-8 -*-

data = [11, 4, 2, 5, 3 ,9]

for i in range(len(data)-1):
    for j in range(len(data)-1, i, -1):
        if(data[j] < data[j-1]):
            tmp = data[j]
            data[j] = data[j-1]
            data[j-1] = tmp


print("after sort: %s" % data)
