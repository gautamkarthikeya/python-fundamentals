#create a function to print contacts


def print_contacts(x):
    for name in x:
        print ('{}: phone: {} email:{}'.format(name,x[name]["phone"],x[name]["email"]))

#create an emty contacts list
contacts = {
            'Gautam': {"phone":'23423432',"email":'Gautam@Gmail.com'}, 
            'daddy':{"phone": '1234567890',"email":'daddy@Gmail.com'}, 
            'uma':{"phone": '0987654321',"email":'Uma@Gmail.com'}, 
            'Mahitha':{"phone": 'no number',"email":'Mahitha@Gmail.com'}
            }
grocery={'milk':'2 liters','pizza':'2'}

print ('Gautam:')
print (contacts['Gautam'])

print ('mahitha:')
print (contacts['Mahitha'])

print_contacts (contacts)

#delete Mahitha from the list
del contacts['Mahitha']
#print the updated list                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             .
print('Updated Contacts after deleting Mahitha:')
print('----------------------------------------')
print_contacts (contacts)

#insert Mahitha to the list

contacts['Mahitha']={"phone":'1213456789',"email":'mahitha@Gmail.com'}
contacts['Aditya']={"phone":"7867654921","email":'Aditya@Gmail.com'}

#print the updated list
print('Updated Contacts after adding Mahitha:')
print('----------------------------------------')
print_contacts (contacts)
















































