def factorial(num):
    i = 2
    x = True
    while x == True:
        num = num / i
        if num == 1:
            x = False
            return("factorial")
        elif num < 1:
            x = False 
            return("None")
        i += 1 



        
