def mode_of_transport(miles):
    if miles<3:
        suggested_mode="walking"
    elif miles>=3 and miles<300:
        suggested_mode="driving"
    else:
        suggested_mode="flying"
    
    return suggested_mode

    


miles = int(input ("How far would you like to travel in miles?:"))

#if miles are negative show error
if miles<=0:
    print ("enter valid input")
#when miles are positive or zero calculate mode of transport
else:
    mode = mode_of_transport(miles)
    print ("suggested mode of transport is {}".format(mode))

