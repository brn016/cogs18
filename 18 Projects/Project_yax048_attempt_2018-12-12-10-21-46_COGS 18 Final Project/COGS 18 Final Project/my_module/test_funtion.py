"""Test for my funtion"""

#Test if the remove_key function could work

from reservation import remove_key
from reservation import reservation_list as p
r = p()

##
##

def test_remove_key():

    test = remove_key(r.availiable,'3')
    
    assert (test == {'1':['12/25/2018-9am'],
                        '2':['12/25/2018-10am'],
                        '4':['12/25/2018-12pm'],
                        '5':['12/25/2018-1pm'],
                        '6':['12/25/2018-2pm'],
                        '7':['12/25/2018-3pm'],
                        '8':['12/25/2018-4pm'],
                        '9':['12/25/2018-5pm'],
                        '10':['12/26/2018-9am'],
                        '11':['12/26/2018-10am'],
                        '12':['12/26/2018-11am'],
                        '13':['12/26/2018-12pm'],
                        '14':['12/26/2018-1pm'],
                        '15':['12/26/2018-2pm'],
                        '16':['12/26/2018-3pm'],
                        '17':['12/26/2018-4pm'],
                        '18':['12/26/2018-5pm'],
                        '19':['12/27/2018-9am'],
                        '20':['12/27/2018-10am']})