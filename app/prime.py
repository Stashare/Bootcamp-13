def prime_generator(n):
    count =0
    primes=[i for i in range(2,n+1)]
    
    for test_number in range(2,n):
        for number in primes:
            if number != test_number  and number % test_number == 0:
                primes.remove(number)

    return primes


print prime_generator(100)