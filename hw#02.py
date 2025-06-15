import random
def get_numbers_ticket(min_v, max_v, quantity_v):
    win_lottery=[]
    #chek if min sis more then 1, less than max and max is min than 1000
    if not (1 <= min_v < max_v <= 1000): 
        return [] #return empty list
     #chek if more than 0 and less than minimum 2
    if not ( 0 < quantity_v <=(max_v-min_v+1)):
        return [] #return empty list

    win_lottery=random.sample(range(min_v,max_v+1),quantity_v) #generat
    return sorted(win_lottery)
    
###---------####
try:
    input_min= int(input("Please, enter the value of min:>>> "))
    input_max= int(input("Please, enter the value of max:>>> "))
    input_quantity=int(input("Please, enter the value of quantity:>>> "))
    print(get_numbers_ticket(input_min, input_max,input_quantity))
except ValueError:
    print("Error of input")