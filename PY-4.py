odd=set([I for I in range(1,11) if i%2==1])
primes=set()
for I in range(2,10):
for j in range(2,i):
If (i%j==0):
Break
else:
Primes.add(i)
print(“odd numbers:”,odd)
print(“Prime numbers:”,primes)
print(“union:”,odd.union(primes))
print(“intersection”,odd.intersection(primes))
print(“difference:”,odd.difference(primes))
print(“symmetricdifference”,odd.symmetric_difference(primes))