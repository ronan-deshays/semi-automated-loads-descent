# Excel formula python3 parser v0.1.0 - stable

# TO DO : multiline comments + sub-functions copy ability
# LIMITATION : Excel is using # in internal formulas ! ; space in column name is creating issue cause removed


import re
target = open("Excel_formula_out.txt", "w")
source = open("Excel_formula_in.txt", "r")

t = source.read()
t = re.sub("# [^\n]*","",t) # remove comments
t = t.replace("\n","") # remove line breaks
t = t.replace(" ","") # remove spaces
t = t.replace("=","\n\n=") # add some space between formulas

target.write(t)

target.close()
source.close()




