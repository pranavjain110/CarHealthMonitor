from alertsys import checkcond
import time
import json

debug = True


def select_thresh():
    """This is a function to set thresholds of parameters
    These would be used by the notification system to compare
    with the sensor values and send an email.
    Returns:
        {(int,int,str)} -- (threshold 1, thereshold 2,user's email)
    """

    # load data from the parameters.txt file
    with open('parameters.txt', 'r') as f:
        data = f.read()
    data = data.replace('\'', '\"')
    json_dict = json.loads(data)

    # extract data from the json
    category1 = json_dict['category1']
    category2 = json_dict['category2']
    email = json_dict['email']

    # set default values for category1 and category2, in case they have not been set
    if category1 == "":
        category1 = "Summer"
    if category2 == "":
        category2 = "Car"

    # for debuging
    if debug:
        print('Selected categories: ')
        print('category2: ' , category2, end = ', ')
        print('category1: ', category1 )

    print('-'*100)
    # threshold selection criterion
    if category2 == "Car":
        if category1 == "Summer":
            # Temperature in celsius
            thresh_engineTemp = 107
            print('Engine temperature threshold set to: ', thresh_engineTemp)
            # Pressure in psi
            thresh_tirePressure = 28
            print('Time pressure threshold set to: ', thresh_tirePressure)
        elif category1 == "Winter":
            thresh_engineTemp = 102
            print('Engine temperature threshold set to: ', thresh_engineTemp)
            thresh_tirePressure = 31
            print('Time pressure threshold set to: ', thresh_tirePressure)
    elif category2 == "Truck":

        if category1 == "Summer":
            thresh_engineTemp = 115
            print('Engine temperature threshold set to: ', thresh_engineTemp)
            thresh_tirePressure = 31
            print('Time pressure threshold set to: ', thresh_tirePressure)

        elif category1 == "Winter":
            thresh_engineTemp = 110
            print('Engine temperature threshold set to: ', thresh_engineTemp)
            thresh_tirePressure = 34
            print('Time pressure threshold set to: ', thresh_tirePressure)

    thresh_tireDistanceKm = 60000
    print('Tire max distance threshold set to: ', thresh_tireDistanceKm)
    thresh_oilTimehrs = 5000
    print('oil max time threshold set to: ', thresh_oilTimehrs)
    print('\n')

    return (thresh_engineTemp, thresh_tirePressure, thresh_oilTimehrs, thresh_tireDistanceKm, email)

# intialize flag as false indicating no maintainance or replacement is required
f = False

# an infite loop which will continue running until maintainance or replacement is required
while True:
    print('_'*100)

    if not f:
        print('waiting for update')
        print('Comparing data with thresholds ... ')
        (t1, t2, t3, t4, email) = select_thresh()
        f = checkcond(f, t1, t2, t3, t4, email)
    else:
        break
    time.sleep(5)
