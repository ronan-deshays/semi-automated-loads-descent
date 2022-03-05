import numpy as np
target = open("h_poutres_sortie.csv", "w")

# https://www.delftstack.com/howto/python/python-read-csv-into-array/
with open("h_poutres_source.csv") as file_name:
    array = np.loadtxt(file_name, delimiter=";", dtype=str) # https://stackoverflow.com/questions/9476797/how-do-i-create-character-arrays-in-numpy
    
# print(array)

Y_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
X_list = ['1', '2', '3', '4', '5', '6', '8', '9']

print(X_list[1])
print(Y_list.index('D'))

for row in array:
    print(row)

    try:
        if ord(row[0])==ord(row[2]):
            # then numerical increment, except 7
            for i in X_list:
                print(i)
                if ord(i) >= ord(row[1]) and ord(i) <= ord(row[3]):
                    temp_next = X_list[X_list.index(i)+1]
                    target.write(row[0]+";"+i+";"+row[2]+";"+temp_next+";"+row[4]+"\n") # check que pas écrasé
                    
                # next(X_list)

        elif ord(row[1])==ord(row[3]):
            for i in Y_list:
                print(i)
                if ord(i) >= ord(row[0]) and ord(i) <= ord(row[2]):
                    temp_next = Y_list[Y_list.index(i)+1]
                    target.write(i+";"+row[1]+";"+temp_next+";"+row[3]+";"+row[4]+"\n") # check que pas écrasé
                # next(Y_list)

        else:
            print("Erreur")
    except:
        print("Fin ligne")
    
    target.write("\n")
        

# target.write()
target.close()