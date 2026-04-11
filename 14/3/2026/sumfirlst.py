def sum_first_and_last(my_tuple):
    
    if len(my_tuple) == 0:
        return 0 
        
   
    return my_tuple[0] + my_tuple[-1]


data_tuple = (10, 20, 30, 40, 50)
print(f"Standard tuple sum: {sum_first_and_last(data_tuple)}") 



single_element_tuple = (5,)
print(f"Single element sum: {sum_first_and_last(single_element_tuple)}") 
