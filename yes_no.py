def yes_no(question):
  valid = False
  while not valid: 
    response = input(question)
  
    # assess user response 
    if response  == "yes" or response == "y":
      response = "yes"
      return response 
  
    elif response == "no" or response == "n":
      response = "no"
      return response
    else:
        print("Please enter yes or no")


# loop for testing 
while True:
  # calls function 
  instructions = yes_no("Have you played before? ")
  # show instructions if not played before 
  if instructions == "no":
    print("Display Instructions ")
  else:
    print("Program continues")