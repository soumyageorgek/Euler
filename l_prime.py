#Program to find the largest prime factor of 600851475143
import sys
def isprime(x):
	i=2
	while i<=(x**(0.5)):
		if x%i==0:
			return False
		i=i+1
	return True
x=600851475143
if isprime(x):	
	print 'the largest prime factor is '+str(x)
	sys.exit(0)
i=2
while i<=int(x**(0.5)):
	if x%i==0:
		if isprime(x/i):	
			print 'largest prime factor is '+str(x/i)
			sys.exit(0)
		elif isprime(i):
			a=i	
		x=x/i
		i=i-1	
	i=i+1
print 'largest prime factor is '+str(a)



	

