
#create a function to print contacts


def print_contacts(contacts):
    for name in contacts:
        print ('{}:{}'.format(name,contacts[name]))

#create an emty contacts list
contacts = {'Gautam': '9620959584', 'daddy': '1234567890', 'uma': '0987654321', 'Mahitha': 'no number'}
grocery={'milk':'2 liters','pizza':'2'}

print ('Gautam:') 
print (contacts['Gautam'])

print ('mahitha:')
print (contacts['Mahitha'])

print_contacts (contacts)

#delete Mahitha from the list
del contacts['Mahitha']
#print the updated list
print('Updated Contacts after deleting Mahitha:')
print('----------------------------------------')
print_contacts (contacts)

#insert Mahitha to the list

contacts['Mahitha']='1213456789'
contacts['Aditya']= '7867654921'

#print the updated list
print('Updated Contacts after adding Mahitha:')
print('----------------------------------------')
print_contacts (contacts)
