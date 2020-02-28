
list=[]
while True:
    
    inputs=input('Enter a sentence that you want to capitalise: ')
    if len(inputs)==0:
        break
    
    list.append(inputs)

list.reverse()

for sentence in list:
    print('You entered: {}, {}, {}. '.format(sentence,sentence.upper(),sentence.lower()))





















