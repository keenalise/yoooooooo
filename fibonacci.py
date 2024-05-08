'''
fibonacci series: 0,1,1,2,3,5,8.....
user input: 
0: invalid number
1: [0]
2: [0,1]
3: [0,1,1]


'''



def get_fibonacci_series(num):
    if not isinstance(num,int):
        
        return None
    
    if num <= 0:
        
        return False
        
    if num == 1:
        return [1]
    
    fibonacci_series = [0,1]
    
    
    for i in range(num-2):
        next_item = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_item)
        
    return fibonacci_series