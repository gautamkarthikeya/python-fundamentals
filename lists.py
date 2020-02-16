#create an emty todo list
todo_list=[]

finished=False
#Ask user to enter his or her todo list
#Add todo to todo list
# If nothing typed and enter pressed then exit and print todo list  
while finished==False:
    task=input ('Enter a task for your to­do list. Press <enter> when done:')   
    todo_list.append (task)
    print (task)
    if task == "":
        finished=True
print ('your todo list')
print ('--------------')

for todo in todo_list:
    print (todo)
    