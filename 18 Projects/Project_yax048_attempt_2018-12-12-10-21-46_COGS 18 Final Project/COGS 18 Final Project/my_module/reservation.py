
def remove_key(dict, i):
    """Remove the key, value pair from a given list"""
    if i in dict:
        del dict[i]
    return dict

class reservation_list:
    """Create a class"""
    
    # The dictionary includes all availiable times
    availiable = {'1':['12/25/2018-9am'],
                        '2':['12/25/2018-10am'],
                        '3':['12/25/2018-11am'],
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
                        '20':['12/27/2018-10am']}
    
    def __init__(self, appointment={}):
        """initialization"""
        # Set appointment dictionary default as empty.
        self.appointment = appointment
        
    def add_appointment(self, job, number):
        """add a new appointment"""
        if number in self.availiable.keys():
            # If the number(date and time) user choose is availiable, append the name of job into the value of the key.
            value = self.availiable[number]
            value.append(job)
            # Then add the key to the appointment dictionary, send the user confirmation message.
            self.appointment[number]=value
            print('Okay I got it! You are all set! Your appointment# is' + ' ' + number)
            # Remove the key from avaliable times
            remove_key(self.availiable, number)
        # If the time user choose is not availiable, tell user time not availiable
        else:
            print('The time you choose is not availiable.')
    
    def check_appointment(self, number):
        """check if appointment in the appointment dictionary"""
        # If the appointment number exist in appointment keys, remind user the time and job 
        if number in self.appointment.keys():
            print('Your appointment is on ', (self.appointment[number][0]), 'for', (self.appointment[number][1]))
        # If the appointment number not exist in appointment keys, tell user appointment not found
        else:
            print('Sorry we cannot find your reseravation')
            
    def cancel_appointment(self, number):
        """remove an appointment from the appointment dictionary"""
        # If the appointment number exist in appointment keys, delete the job from the the value
        # Add it back to availiable time dictionary
        if number in self.appointment.keys():
            self.availiable[number]=[self.appointment[number][0]]
            # Remove the key from appointment dictionary
            remove_key(self.appointment, number)
            print('Your appointment has been canceled.')
            
        # If the appointment number not exist in appointment keys, tell user appointment not found
        else:
            print('Sorry we cannot find your reseravation')
            
    def check_avaliable(self):
        """print out all avaliable times"""
        for i in self.availiable:
            print(i,self.availiable[i])

