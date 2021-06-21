# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Uow ID: w1836048        
# IIT ID: 20200612 

# Date:  03/04/2021

#Part 1 - Student Version



print("-----------------------------------------------------------------------------------------")
print("**************************************************************")         
print("*                          INSTRUCTIONS                      *")                                   	
print("*                                                            *")
print("*        1: Enter your credits when the program asked!       *")
print("*        2: Please enter integers as inputs..                *")
print("*        3: Credits must be less  than or equal to 120       *")
print("*        4: Credits must be greater than or equal to 0       *")
print("*        5: Credits must be [0,20,40,60,80,100,120]          *")
print("*                                                            *")
print("*                                                            *")
print("*        >>>>>>>> STUDENT PROGRESSION OUTCOME <<<<<<<<       *")
print("*                                                            *")
print("**************************************************************")



credit_at_pass = int(input("\nPlease enter your credit at pass  : "))           
credit_at_defer = int(input("Please enter your credit at defer : "))
credit_at_fail = int(input("Please enter your credit at fail  : "))

if credit_at_pass == 120:                                                       # checking for condition satisfaction for the output 'Progress'
    print("\n> Progress")
else:
    if credit_at_pass == 100:                                                   # checking for condition satisfaction for  the output 'Progress(module trailer)'
        print("\n> Progress (module trailer)")                                          
    elif credit_at_fail >= 80:                                                  # checking for condition satisfaction for the output 'Exclude'                                               
        print("\n> Exclude")
    else:                                                                       # checking for condition satisfaction for the output 'Do not Progress - module retriver'               
        print("\n> Do not Progress - module retriever")
        
print("\n**************************************************************")
print("*                                                            *")
print("*                        THANK YOU                           *")
print("*              >>>>>> program is over <<<<<<                 *")
print("*                                                            *")
print("**************************************************************")
print("-----------------------------------------------------------------------------------------")

