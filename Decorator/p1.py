def create_adder(x): 
    print('x',x) #15
    def adder(y): 
        print(y) #10
        return x+y 
 
    return adder 
 
add_15 = create_adder(15) 
 
print(add_15(10)) 