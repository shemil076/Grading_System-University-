import time
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Uow ID: w1836048        
# IIT ID: 20200612 

# Date:  26/04/2021

# Part 5 – Alternative Staff Version (optional extension)


print("**************************************************************")
print("*                          INSTRUCTIONS                      *")                                   	
print("*                                                            *")
print("*           Data has been added to the program.              *")
print("*                                                            *")
print("*        >>>>>>> STUDENT PROGRESSION OUTCOME <<<<<<<<        *")
print("*            Please wait until the program over              *")
print("*                                                            *")
print("**************************************************************")
time.sleep(0.5)
data = [[120, 0, 0], [100, 20, 0], [100, 0, 20], [80,20, 20], [60, 40, 20], [40, 40, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100], [0, 0, 120]]  #mark list

progress = 0
trailer = 0
retriever =  0
excluded = 0
index = 0
table = []                                                                                          # set an empty list

def get_data():                                                                                                     
    global progress     
    global trailer  
    global retriever 
    global excluded 
    global index  
    global table  
    for i in range(len(data)):                                                                      # Go through the list
        table = data[index]                                                                         # Assigning one list to the 'table'(empty list) at a moment
        if table[0] == 120:                                                                         # checking for condition satisfaction for the output 'Progress'
            time.sleep(0.5)
            print("> Progress")                                                                      
            progress += 1                                                                           # Increase the global variable
        elif table[0] == 100:
            time.sleep(0.5)
            print("> Progress (module trailer)")                                                      # checking for condition satisfaction for  the output 'Progress(module trailer)'
            trailer += 1                                                                            # Increase the global variable
        elif table[2] >= 80:                                                                        # checking for condition satisfaction for the output 'Exclude'
            time.sleep(0.5)
            print("> Exclude")
            excluded += 1                                                                           # Increase the global variable
        else:                                                                                       # checking for condition satisfaction for the output 'Do not Progress - module retriver'
            time.sleep(0.5)               
            print("> Do not Progress - module retriever")
            retriever += 1                                                                          # Increase the global variable
        index += 1                                                                                  # Increase the index
    
def histogram():
    global progress 
    global trailer 
    global retriever 
    global excluded
    print()
    total = progress + trailer + retriever + excluded                                               # counting the total
    print(f'{"Progress":9} {progress:>4} {":":>1} {"*"*progress}')                                  # creating the Histogram
    print(f'{"Trailing":9} {trailer:>4} {":":>1} {"*"*trailer}')
    print(f'{"Retriever":9} {retriever:>4} {":":>1} {"*"*retriever}')
    print(f'{"Excluded":9} {excluded:>4} {":":>1} {"*"*excluded}')
    print()
    print(total, "outcomes in total.")



get_data()                                                                                          # Calling the function to start the program
histogram()                                                                                         # finaly calling the function to create the histogram
print()
time.sleep(0.5)
print("\n**************************************************************")
print("*                                                            *")
print("*                        THANK YOU                           *")
print("*              >>>>>> program is over <<<<<<                 *")
print("*                                                            *")
print("**************************************************************") 
