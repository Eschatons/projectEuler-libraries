""" common arithmetic series """

def trianglular(n):
	''' returns nth triangular number '''
	if n < 1 or n != n // 1:
		raise(ValueError('input must be a positive integer')
	else:
		return (n*n+1) //2

def square(n):
	''' returns nth square number '''
	if n < 1 or n != n // 1:
		raise(ValueError('input must be a positive integer')
	else:
		return n**2


def pentagonal(n):
	''' returns nth pentagonal number '''
	if n < 1 or n != n // 1:
		raise(ValueError('input must be a positive integer')
	else:
		return (n*(3*n-1))//2

def hexagonal(n):
	'''returns nth hexagonal number '''
	if n < 1 or n != n // 1:
		raise(ValueError('input must be a positive integer')
	else:
		return n*(2*n-1)

	
def heptagonal(n):
''' returns nth heptagonal number '''
if n < 1 or n != n // 1:
	raise(ValueError('input must be a positive integer')
else:
	return (n*((5*n)-3))//2
	
def octagonal(n):
	''' returns nth octagonal number '''
	if n < 1 or n != n // 1:
		raise(ValueError('input must be a positive integer')
	else:
		return (n*(3*n-2))