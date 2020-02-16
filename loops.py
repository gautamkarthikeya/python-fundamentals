list_grocery = ["pizza","milk","cheeze","bananas","chocolates",'apple pie','apple','apples']
list_grocery = sorted(list_grocery)

for grocery_item in list_grocery:
    pie_index = list_grocery.index(grocery_item)
    print(grocery_item+' is at index: ',pie_index)

table = 75
line = 99
while line<21:
    print('{}*{}={}'.format(line,table,line*table))
    line=line+1


for line in  range (1,99):
    print ('{}*{}={}'.format(line, table,line*table))
    
    