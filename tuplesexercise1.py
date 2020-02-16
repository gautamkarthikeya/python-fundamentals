airports=[
    ('Indhira ghandi International airport','IND'),
    ('London Heathrow','LON'),
    ('Los Angeles International Airport','LAX')
    ]
def print_airports (airports):
    for (airport,code) in airports:
        print ('The code for {} is {}'.format(airport,code))

print_airports (airports)

