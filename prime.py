import gmpy2

def next_prime_number(input, end):
    while True:
        n_prime = gmpy2.next_prime(int(input))
        if input < end:
            input = n_prime
            print('The next prime number is :{}'.format(n_prime))
        else:
            break

prime = next_prime_number(1, 100)