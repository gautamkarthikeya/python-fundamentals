list_grocery = ["pizza","milk","cheeze","bananas","chocolates"]
print (list_grocery)
more_groceries = ["bread", "jam"]
list_grocery.extend (more_groceries) 
print (list_grocery)
list_grocery.insert (2,"jam")
print (list_grocery)

list_grocery_slice_1 = list_grocery[1:6]
print (list_grocery_slice_1)

list_grocery_slice_2 = list_grocery[:5]
print (list_grocery_slice_2)

list_grocery_slice_3 = list_grocery[3:]
print (list_grocery_slice_3)     


try:
    pie_index = list_grocery.index("cheeze")
except:
    pie_index = ('No pies found')
print (pie_index)