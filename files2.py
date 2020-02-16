

animals_list=[]

with open ('C:\\Users\\eswar\\Downloads\\animals.txt') as animals:

    for animal in animals:
        animals_list.append(animal)

    print (sorted(animals_list))   

#create new file animals-sorted.txt
sorted_animals=open ('C:\\Users\\eswar\\Downloads\\animals-sorted.txt',"w")
# loop through sorted animals_list
for animal in sorted(animals_list):
    # append animals to new file    
    sorted_animals.write(animal)

# close files
sorted_animals.close


