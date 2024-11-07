def calculate_odd_average(numbers):
    """ 
    Returns the avergae of the odd number in [numbers].
    Returns 0 if there's no odd numbers
    """
    total = 0
    total_odd = 0
    for i in range(len(numbers)-1): 
        if (numbers[i] % 2 == 0):  
            total += numbers[i]
        total_odd+=1                
        total += numbers[i]
    avg = total / len(numbers)      
    return avg

def main():    
    num_lst = [5,5,5,5,5]
    avg = calculate_odd_average(num_lst)
    print(f"The average odd numbers of {num_lst} is: {avg}")
    num_lst = [1,5,5,5,6]
    avg = calculate_odd_average(num_lst)
    print(f"The average of {num_lst} is: {avg}")
    num_lst = [2]
    avg = calculate_odd_average(num_lst)
    print(f"The average of {num_lst} is: {avg}")
    num_lst = [1]
    avg = calculate_odd_average(num_lst)
    print(f"The average of {num_lst} is: {avg}")

if __name__ == "__main__":
    main()
