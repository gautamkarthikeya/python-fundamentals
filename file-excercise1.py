#Create a line counter variable and set it to 0
line_counter=0
#OPen file mystory.txt using with
with open ('C:\\Users\\eswar\\Downloads\\mystory.txt') as my_story:
    for line in my_story:
        #increment counter by 1 for each line
        line_counter=line_counter+1
        print ('{}: {}'.format(line_counter,line.rstrip()))
        

