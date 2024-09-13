def gcd(a,b):
    while b!=0:
        t = b
        b = a%b
        a = t
    return a

def sgn(a):
    return int(a/abs(a))

def lcd(a,b):
    return int(abs(a*b)/gcd(a,b))

def prime(n):
    # creates a list of primes until n
    nums=range(2,n)
    def is_prime(n):
        for i in range(2,n):
            if (n%i)==0:
                return False
        return True
    primes=list(filter(is_prime,nums))
    return primes

# print(lcd(12,3))

def prime_factors(a):
    #lists down the prime factors with primes up to 1000
    a=int(a)
    import math
    p_factors=[]
    primes=prime(20000)
    i,j=0,0
    while i<=len(primes):
        if j==1:
            j=0
            i-=1
        if i==(len(primes)-1) and a!=1:
            return("Factors are beyond the scope of within 1000 primes")
        if a==1:
            break
        if a%primes[i]==0:
            p_factors.append(primes[i])
            a=a/primes[i]
            j+=1
        i+=1    
        print(int(a),",",primes[i],",",j,i)
    return p_factors
print(prime_factors(400000))
# print(prime(100000))