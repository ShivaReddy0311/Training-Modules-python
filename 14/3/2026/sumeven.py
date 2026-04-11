def sum_even_numbers(my_tuple):

    return sum(num for num in my_tuple if num % 2 == 0)


data_tuple = (1, 2, 3, 4, 5, 6)
print(f"The sum of even numbers is: {sum_even_numbers(data_tuple)}") 
