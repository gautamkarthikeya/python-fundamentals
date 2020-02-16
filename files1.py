'''my_story=open ('C:\\Users\\eswar\\Downloads\\mystory.txt')
#print (my_story.read(3000))

#find where is the current position

print(my_story.tell())

#move curser to read from start
my_story.seek(0)
print(my_story.tell())
print (my_story.read(10))
#read five lines
my_story.seek(0)
for i in range (1,11):
    print (my_story.readline().rstrip())

my_story.close()
'''

with open('C:\\Users\\eswar\\Downloads\\mystory.txt') as my_story:
    for line in my_story:
        print (line.rstrip())



