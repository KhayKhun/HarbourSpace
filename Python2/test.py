import time
import functools

def calculate_time(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        b = time.time()

        func(*args, **kwargs)

        e = time.time()
        print("taken", e - b)
    
    return inner

@calculate_time
def sum(x, y):
    """This is doc of sum"""
    print(x + y)


sum(7,8)

# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())

        
def decor1(func):
        def wrap():
               print("************")
               func()
               print("************")
        return wrap
def decor2(func):
        def wrap():
               print("@@@@@@@@@@@@")
               func()
               print("@@@@@@@@@@@@")
        return wrap
    
@decor1
       
@decor2
def sayhellogfg():
         print("Hello")
def saygfg():
         print("GeekforGeeks")
        
sayhellogfg()
saygfg()