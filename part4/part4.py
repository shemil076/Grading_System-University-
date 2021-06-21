# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Uow ID: w1836048        
# IIt ID: 20200612 

# Date:  22/04/2021
#Part 4 - Vertical Histogram (optional extension)

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
print("*        >>>>>>>>     Vertical Histogram      <<<<<<<<       *")
print("*                                                            *")
print("**************************************************************")




progress = 0
trailer = 0
retriever =  0
excluded = 0
print("\nStaff Version with Histogram ")

def check(credits_input):
    credit = [0, 20, 40, 60, 80, 100, 120]                                                                  # valid range of values
    return True if  credits_input in credit else False                                                      # check whether the inputs are valid or not




def again ():                                                                                               ## repeating function (user define)
    global progress 
    global trailer 
    global retriever 
    global excluded 
    start  = True
    while start:                                                                                             # loop until the program gets valid inputs
        try:                                                                                                 # validation
            credit_at_pass = int(input("\nPlease enter your credit at pass  : "))
            if check(credit_at_pass) == True:
                credit_at_defer = int(input("Please enter your credit at defer : ")) 
                if check(credit_at_defer) == True:
                    credit_at_fail = int(input("Please enter your credit at fail  : "))
                    if check(credit_at_fail) == True:
                        if credit_at_pass + credit_at_defer + credit_at_fail == 120:                        # checking wheather the total of inputs are equal to 120
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
                    print("\n>> out of range\n")
            else:
                print("\n>> out of range\n")
        except ValueError:                                                                                  # without terminating, print a error message if user's inputs are not integers 
            print("\n>> Integer required\n")


def histogram():                                                                                            # creates the histogram
    global progress 
    global trailer 
    global retriever 
    global excluded
    total = progress + trailer + retriever + excluded
    table = [progress, trailer, retriever, excluded]                                                        # insert the values to a table
    largest = max(table)                                                                                    # find the largest value in the table
    length = len(table)                                                                                     # number of elements in the table (in this occasion it is 4)
    line = 0                                                                                                # counter of the number lines that should print the histogram
    index = 0                                                                                                
    print(f'{"Progress":9} {progress:3}  {"|"} {"Trailer":>8} {trailer:3} {"|"}  {"Retriever":10} {retriever:3} {"|"}  {"Excluded" :8} {excluded:3} ')                                     
    while line < largest :                                                                                  
        index = 0
        while index < length:                                                                               
            if line < table[index]:                                                                         # compare  number of lines and the value of the element in the table 
                print(f'{"*":>5}', end="            ")
            else:
                print(f'{" ":>5}', end="            ")
            index += 1                                                                                      # increase the table index
        line += 1                                                                                           # increase the line number
        print()
    print(total, "Outcomes in total.")


again()

while True:
    condition = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    condition = condition.lower()
    if condition == "y":
        again()
    elif condition == "q":
        print("-----------------------------------------------------------------------------------------")
        histogram()
        print()
        break
print("\n**************************************************************")
print("*                                                            *")
print("*                        THANK YOU                           *")
print("*              >>>>>> program is over <<<<<<                 *")
print("*                                                            *")
print("**************************************************************")                
print("-----------------------------------------------------------------------------------------")
