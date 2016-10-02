# O(n^2) 

def unique_digit(n):
    if(n > 10):
        return unique_digit(10)
    elif(n ==1):
        return 10
    else:
        unique_digit_sum = 10
        for n_iterate in range(2, n+1):
            n_digit_sum = 9
            for i in range(n_iterate-1):
                choice_num = 9-i
                n_digit_sum = n_digit_sum * choice_num
            unique_digit_sum += n_digit_sum
    print(unique_digit_sum)
    return unique_digit_sum
    
def main():
    unique_digit(10)
    
main()