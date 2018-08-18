#simple calc:

def num(x,a,b):
    if x is "add":
        z = a + b
        return(z)
    elif x is "sub":
        z = a - b
        return(z)
    elif x is "div":
        z = a / b
        return(z)
    elif x is "mul":
        z = a * b
        return(z)

pop = num("add",12,12)

print(pop)





