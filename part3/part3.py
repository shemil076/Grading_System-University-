# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Uow ID: w1836048        
# IIT ID: 20200612 

# Date:  11/04/2021

#Part 3 - Staff Version with Histogram 

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
print("*        >>>>>>>>    Horizontal Histogram     <<<<<<<<       *")
print("*                                                            *")
print("**************************************************************")




progress = 0
trailer = 0
retriever =  0
excluded = 0
print("\nStaff Version with Histogram ")

def check(credits_input):
    credit = [0, 20, 40, 60, 80, 100, 120]                                                                 # valid range of values 
    return True if  credits_input in credit else False                                                     # check whether the inputs are valid or not 




def again ():                                                                                              # repeating function (user define)
    global progress 
    global trailer 
    global retriever 
    global excluded 
    start  = True
    while start:                                                                                            # loop until the program gets valid inputs
        try:                                                                                                # validation
            credit_at_pass = int(input("\nPlease enter your credit at pass  : "))
            if check(credit_at_pass) == True:
                credit_at_defer = int(input("Please enter your credit at defer : ")) 
                if check(credit_at_defer) == True:
                    credit_at_fail = int(input("Please enter your credit at fail  : "))
                    if check(credit_at_fail) == True:
                        if credit_at_pass + credit_at_defer + credit_at_fail == 120:                        # checking whether the total of inputs are equal to 120
                            if credit_at_pass == 120:                                                       # checking for condition satisfaction for the output 'Progress'
                                print("\n> Progress\n")
                                progress += 1                                                               # increment of a global variable
                                start = False                                                               # terminate the infinite loop if the inputs and conditions are valid 
                            else:
                                if credit_at_pass == 100:                                                   # checking for condition satisfaction for  the output 'Progress(module trailer)'
                                    print("\n> Progress (module trailer)\n")
                                    trailer += 1                                                            # increment of a global variable
                                    start = False                                                           # terminate the infinite loop if the inputs and conditions are valid                                      
                                elif credit_at_fail >= 80:                                                  # checking for condition satisfaction for the output 'Exclude'                                             
                                    print("\n> Exclude\n")
                                    excluded += 1                                                           # increment of a global variable
                                    start = False                                                           # terminate the infinite loop if the inputs and conditions are valid 
                                else:                                                                       # checking for condition satisfaction for the output 'Do not Progress - module retriver'               
                                    print("\n> Do not Progress - module retriever\n")
                                    retriever += 1                                                          # increment of a global variable
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

def histogram():                                                                                            # creates the histogram  
    global progress 
    global trailer 
    global retriever 
    global excluded
    print("Horizontal Histogram")
    total = progress + trailer + retriever + excluded                                                       # total number of progress, trailer, retriever and excluded  
    print(f'{"Progress"} {progress:4} {":":>2} {"*"*progress}')                                             # Construction of the histogram
    print(f'{"Trailer"} {trailer:4} {":":>3} {"*"*trailer}')
    print(f'{"Retriever"} {retriever:4} {":":>1} {"*"*retriever}')
    print(f'{"Excluded"} {excluded:4} {":":>2} {"*"*excluded}')
    print()
    print(total, "Outcomes in total.")

again()                                                                                                     # Call the function to start the program for inputs

while True:                                                                                                                    
    condition = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")      
    condition = condition.lower()
    if condition == "y":                                                                                      # checking the condition for repeating
        again()                                                                                               # repeat the process if the user need                                                                                          
    elif condition == "q":                                                                                    # else stop the process and display the histogram
        print("-----------------------------------------------------------------------------------------")
        histogram()
        print()                                                                                               # call the histogram at last.
        break                                                                                                 # Break from the loop and end the program
print("\n**************************************************************")
print("*                                                            *")
print("*                        THANK YOU                           *")
print("*              >>>>>> program is over <<<<<<                 *")
print("*                                                            *")
print("**************************************************************")     
print("-----------------------------------------------------------------------------------------")
