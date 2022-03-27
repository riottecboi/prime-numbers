import gmpy2
import json
import random

########## Storing data from json file ##########
with open('example.json', encoding='utf-8') as data:
    cfg = json.load(data)

########## Generate random number list ##########
def generate_random_list_number(start, to):
    randomlist=[]
    for i in range(0, 49):
        n = random.randint(int(start), int(to))
        randomlist.append(n)
    return randomlist

########## Function to check input data is Prime number or not ##########
def check_number(input):
    check = gmpy2.is_prime(input)
    if check is True:
        print(f"The {input} is prime number")
    else:
        print(f"The {input} is not prime number")
    return check

########## Calculate the next prime number by input ###########
def next_prime_number(input, end):
    while True:
        check_number(int(input))
        n_prime = gmpy2.next_prime(int(input))
        if int(input) < int(end):
            input = n_prime
            print('The next prime number is :{}\n'.format(n_prime))
        else:
            break

######### Calculate next prime number whether input is a prime number ########
def calculate_next_prime_number_when_input_is_prime(input):
    checked = check_number(int(input))
    if checked is True:
        n_prime = gmpy2.next_prime(int(input))
        print('The next prime number is :{}\n'.format(n_prime))
    else:
        print('Not calculate this number\n')
        pass


#Un-comment when you want to let it function run
if __name__ == '__main__':
    #next_prime_number(cfg['input_number'], cfg['end_number'])
    for inp in generate_random_list_number(cfg['range_from'], cfg['range_to']):
        calculate_next_prime_number_when_input_is_prime(inp)