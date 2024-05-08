import fibonacci


def main ():
    print ("Starting main...")
    number = int(input("Enter the length of the series" ))
    
    series = fibonacci.get_fibonacci_series(number)
    
    if series is None:
        print("Invalid input, please enter positive number")
    
    print (series)
    
main ()
