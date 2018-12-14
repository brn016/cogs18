"""A collection of function for doing my project."""

# Imports
import random as rand
import math


# The range for a primes are between 1 to 500, so the
# program can run quickly.
def generate_prime_number():
    """
    Generate prime number
    
    Parameters
    ----------
    None
    
    Returns
    -------
    A prime number between 1 to 500.
    """
    prime_number = rand.randint(1,500)
    while(not is_prime(prime_number)):
        prime_number = rand.randint(1,500)
    return prime_number


# Primality test using 6k + 1 optimization 
# based on Wiki article on Primality test
# https://en.wikipedia.org/wiki/Primality_test
def is_prime(num):
    """
    Check if number is a prime
    
    Parameters
    ----------
    num: int
        The number to check if its prime.
    
    Returns
    -------
    True: Number is prime.
    False: Number is not a prime.

    """
    if (num <= 3):
        return num > 1
    elif (num % 2 == 0 or num % 3 == 0):
        return False
    i = 5
    while(i*i <= num):
        if (num % i == 0 or num % (i + 2) == 0):
            return False
        i = i + 6;
    return True
        

def get_n(p,q):
    """
    Generates n
    
    n is used as modulus for both the public and private keys
    
    Parameters
    ----------
    int p
    int q
    
    Returns
    -------
    int: n = p*q

    """
    return p*q    


# The algorithm was written by StackOverflow used orlp.
# https://stackoverflow.com/a/18114286
def phi(n):
    """
    Computes the Eulers Totient Function
    Eulers Totient Function counts the number of postive 
    integers up to a given integer n that are relatively prime to n.
    
    φ = phi
    
    If n is a positive integer, 
    then φ(n) is the number of integers k in the range 1 ≤ k ≤ n 
    for which gcd(n, k) = 1. (https://en.wikipedia.org/wiki/Euler%27s_totient_function)
        
    Parameters
    ----------
    int n (the value created by get_n function)
    
    Returns
    -------
    int: amount

    """
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

# find lcm between p and q
def lcm(a, b):
    """
    Generates least common multiple between 2 numbers
        
    Parameters
    ----------
    int a
    int b
    
    Returns
    -------
    int: lcm(a,b)

    """
    return abs(a*b//math.gcd(a, b)) 

def coprime(lambda_n):
    """
    Generate coprime
    
    Chooses an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; i.e., e and λ(n) are coprime.
    
    Parameters
    ----------
    int lambda_n
    
    Returns
    -------
    A coprime
    
    """    
    while(1):
        e = rand.randint(1,lambda_n)
        if(math.gcd(e, lambda_n) == 1):
            return e


def get_d(e,lambda_n):
    """
    Generate d
    
    Parameters
    ----------
    int e
    int lambda_n
    
    Returns
    -------
    d
    
    """
    e = e % lambda_n; 
    for x in range(1, lambda_n) : 
        if ((e * x) % lambda_n == 1) : 
            return x 

def get_e(p,q):
    """
    Generate e
    
    Parameters
    ----------
    int p
    int q
    
    Returns
    -------
    int e
    
    """
    phi_p = phi(p)
    phi_q = phi(q)
    return coprime(lcm(phi_p,phi_q))

def get_lamda_n(p,q):
    """
    Generate lamda_n
    
    Parameters
    ----------
    int p
    int q
    
    Returns
    -------
    int e
    
    """
    return lcm( phi(p), phi(q))

def encryptor(char_array):
    """
    Generate encrypted text
    
    Parameters
    ----------
    char array
    
    Returns
    -------
    encrypted char array
    
    """
        
    p = generate_prime_number()
    q = generate_prime_number()
    
    n = get_n(p,q)
    lamda_n = phi(n);
    
    e = coprime(lamda_n)
    
    d = get_d(e,lamda_n)
    
    print("""Don't lose the private key or n. You will not be able decrypt your text otherwise!\n""")
    print("n: ", n)
    print("private key: ", d,"\n")
    
    encrypt_char = []

    for char in char_array:
        m = (char ** e) % n
        encrypt_char.append(m)
        
    return encrypt_char

def decryptor(char_array,private_key,n):
    """
    Generate decrypted text
    
    Parameters
    ----------
    char array, int private_key, int n
    
    Returns
    -------
    decrypted char array
    
    """
    decrypt_char = []
    for char in char_array:
        value = (char ** private_key) % n
        decrypt_char.append(value)
    return decrypt_char


def char_to_ASCII(text):
    """
    Generate char array to ASCII array
    
    Parameters
    ----------
    char array
    
    Returns
    -------
    int ASCII array
    
    """
    ASCII_array = [];
    for char in text:
        ASCII_array.append(ord(char))
    return ASCII_array

def ASCII_to_char(text):
    """
    Generate ASCII array to string
    
    Parameters
    ----------
    int array
    
    Returns
    -------
    string
    
    """
    chars = [];
    for char in text:
        chars.append(chr(char))
        
    string = ''.join(chars)
    return string
    
