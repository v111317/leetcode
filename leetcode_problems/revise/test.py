for variable_1 in range(10,11,-1):
    print(variable_1, "executed")
    
class Table:                  
    def __init__(self, a, b):       
        self.no_of_legs=4     
        self.glass_top=a   
        self.wooden_top=b
dining_table=Table(1, 2)          
back_table=Table(3, 4)            
front_table=back_table        
back_table=dining_table       
dining_table=front_table      
front_table=back_table    

print(front_table.glass_top)
print(back_table.glass_top)
print(dining_table.glass_top)