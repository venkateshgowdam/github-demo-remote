#add implementation
def add(x,y):
    return x+y
#sub implementation
def sub(x,y):
    return x+y
#mul implementation
def mul(x,y):
    return x*y #on Bug456 branch
#div implementation
def div(x,y):
    if y==0:		#on master branch
      return DIVIDE_BY O_ERROR
    else:
      return x/y
#square implemenation
def square(x):
     return x*x