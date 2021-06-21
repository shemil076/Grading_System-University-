# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Uow ID: w1836048        
# IIT ID: 20200612 

# Date:  07/04/2021

#Part 2 – Student Version (Validation)

print("-----------------------------------------------------------------------------------------")
print("**************************************************************")                                  # intructions for users
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
print("*        >>>>>>>>      (With Validation)      <<<<<<<<       *")
print("*                                                            *")
print("**************************************************************")


def check(credits_input):
    credit = [0, 20, 40, 60, 80, 100, 120]                                                              # valid range of values 
    return True if  credits_input in credit else False                                                   
    
start  = True
while start:                                                                                            # loops until the program gets valid inputs
    try:                                                                                                 # validation / catch the value errors
        credit_at_pass = int(input("\nPlease enter your credit at pass  : "))
        if check(credit_at_pass) == True:                                                               #  check whether the inputs are valid or not
            credit_at_defer = int(input("Please enter your credit at defer : ")) 
            if check(credit_at_defer) == True:                                                          # check whether the inputs are valid or not
                credit_at_fail = int(input("Please enter your credit at fail  : "))
                if check(credit_at_fail) == True:                                                       # check whether the inputs are valid or not
                    if credit_at_pass + credit_at_defer + credit_at_fail == 120:                        # checking whether the total of inputs are equal to 120
                        if credit_at_pass == 120:                                                       # checking for condition satisfaction for the output 'Progress'
                            print("\n> Progress")
                            start = False                                                               # terminate the infinite loop if the inputs and conditions are valid 
                        else:
                            if credit_at_pass == 100:                                                   # checking for condition satisfaction for  the output 'Progress(module trailer)'
                                print("\n> Progress (module trailer)")
                                start = False                                                           # terminate the infinite loop if the inputs and conditions are valid
                            elif credit_at_fail >= 80:                                                  # checking for condition satisfaction for the output 'Exclude'                                               
                                print("\n> Exclude")
                                start = False                                                           # terminate the infinite loop if the inputs and conditions are valid
                            else:                                                                       # checking for condition satisfaction for the output 'Do not Progress - module retriver'               
                                print("\n> Do not Progress - module retriever")
                                start = False                                                           # terminate the infinite loop if the inputs and conditions are valid
                    else:
                        print("\n>> Total incorrect\n")                                                   
                    
                else:
                    print("\n>> Out of range\n")
            else:
                print("\n>> Out of range\n")
        else:
            print("\n>> Out of range\n")
    except ValueError:                                                                                  # without terminating, print a error message if user's inputs are not integers 
        print("\n>> Integer required\n")



print("\n**************************************************************")                              # end of the program
print("*                                                            *")
print("*                        THANK YOU                           *")
print("*              >>>>>> program is over <<<<<<                 *")
print("*                                                            *")
print("**************************************************************")         
print("-----------------------------------------------------------------------------------------")
