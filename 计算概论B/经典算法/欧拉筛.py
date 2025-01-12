N=int(input('检索多少范围内的质数：'))
isprime=[True]*(N)
isprime[1]=False
isprime[0]=False
primes=[]
for i in range(2,N):
    if isprime[i]:
        primes.append(i)
    for prime in primes:
        if i*prime>=N:
            break
        isprime[i*prime]=False
        if i%prime==0:
            break