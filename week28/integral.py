# get user input
x = int(input("Enter a number"))

# create empty dictionary
dictionary = {}             
        
# add elements to dictionary
for i in range(1, x+1):     
    dictionary[i] = i*i     
                            
# print dictionary
print(dictionary)           
