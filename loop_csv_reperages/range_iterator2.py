#!/usr/bin/env python
# this file is part of this GitHub project : https://github.com/ronan-deshays/excel-formula-parser

import numpy as np
target = open("reperage_sortie.csv", "w")

# https://www.delftstack.com/howto/python/python-read-csv-into-array/
with open("reperage_source.csv") as file_name:
    array = np.loadtxt(file_name, delimiter=";", dtype=str) # https://stackoverflow.com/questions/9476797/how-do-i-create-character-arrays-in-numpy
    
# print(array)

Y_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
X_list = ['1', '2', '3', '4', '5', '6', '8', '9']

print(X_list[1])
print(Y_list.index('D'))

for row in array:
    print(row)

    try:
        for i in X_list:
            print(i)
            if ord(i) >= ord(row[1]) and ord(i) < ord(row[3]):
                temp_next = X_list[X_list.index(i)+1]
            for j in Y_list:
                print(j)
                if ord(j) >= ord(row[0]) and ord(j) < ord(row[2]):
                    temp_next_2 = Y_list[Y_list.index(j)+1]

                    if ord(i) < ord(temp_next) and ord(j) < ord(temp_next_2) :
                        target.write(j+";"+i+";"+temp_next_2+";"+temp_next+";"
                            +row[4]+";"+row[5]+";"+row[6]+";"+row[7]+"\n") # check que pas écrasé

    except:
        print("Fin ligne")
    
    target.write("\n")
        

# target.write()
target.close()