import zlib #imports the zlib library
import sys #this allows us to functions like getsizeof
import time
import base64
from itertools import groupby # these are helpful for looping


            
def zlibCompress():   

        filename = input('\nEnter the name of the file (with extension) that you would like to compress. \n \nNote: the file must be in the same directory as this function or else FileNotFoundError will be raised \n –– ')
   
           

    text = open(filename, 'r').read() # r is for read only

    byte_text = str.encode(text) #converts text to bytes; compressed functions takes in bytes as input as of Python 3
   
    level = -1
    while 0 > level or 9 < level:
        try:
            level = int(input("Enter desired compression level (0-9): "))
        except ValueError:
            print("Please enter a valid number (0-9) ")
            
    compressed = zlib.compress(byte_text, level) #stores the compressed version of the file
    original_size = sys.getsizeof(text) #get original size of fiel
    new_size = sys.getsizeof(compressed) #get new size of file
    percent_save = int((((original_size - new_size)/original_size) * 100)) #calculate %byte reduction
    print('Raw size:', original_size) #outputs
    print('level ',level,' compressed size: ',new_size,' bytes')
    print('That is a ',percent_save,' % decrease!')
    
    print(compressed)





def groupbyRunLengthEncode(text):
    res = [] #res is the result list
    for k,i in groupby(text):
        run = list(i)
        if(len(run) > 4):
            res.append("/{:02}{}".format(len(run), k))
        else:
            res.extend(run)

    return "".join(res)


# a separate function is made to print the output

def printRLE():
    i = input('Please enter a string of characters you would like to compress: ') #i is just a temporary variable
    print('Compressed text:',groupbyRunLengthEncode(i))
    original_size = sys.getsizeof(i)
    print('Original size in bytes:',original_size)
    new_size = sys.getsizeof(groupbyRunLengthEncode(i))
    print('New size in bytes:',new_size)
    percent_save = int((((original_size - new_size)/original_size) * 100))
    print('That is a ',percent_save,' % decrease!')





def simpleEncode(text): #also uses Run Length Encoding as explained in notebook
    if not text:
        return ""
    else:
        last_char = text[0]
        max_index = len(text)
        i = 1
        while i < max_index and last_char == text[i]:
            i += 1
        return last_char + str(i) + simpleEncode(text[i:])

 
 # a separate function is made to print the output

def printEncode(): 
    i = input('Please enter a string of characters you would like to compress: ')
    print('Compressed text:',simpleEncode(i))
    original_size = sys.getsizeof(i)
    print('Original size in bytes:',original_size)
    new_size = sys.getsizeof(simpleEncode(i))
    print('New size in bytes:',new_size)
    percent_save = int((((original_size - new_size)/original_size) * 100))
    print('That is a ',percent_save,' % decrease!')


