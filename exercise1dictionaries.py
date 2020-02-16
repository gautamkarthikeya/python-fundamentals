def print_people (people):
    for g in people:
        print ('{}: {}'.format(g,people[g]))

people={
    'Gautam':'He can solve the rubics cube',
    'Mahitha':'She can hula hoop',
    'Uma':'Makes delicious food',
    'Daddy':'Is a good programmer'
    }
print_people (people)

#update a fact 
people ['Gautam']='is a very good table tennis player'
print_people (people)
#add new person
people ['Aditya']='Is very good at cricket'
print_people (people)