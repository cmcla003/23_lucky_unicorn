# loop for testing 
while True: 
  # Ask user if they have played before
  show_instructions = input("Have you played Lucky Unicorn before? ").lower()
  
  # If  yes, output 'program continues'
  if show_instructions == "yes" or show_instructions == "y":
      print("Program continues")
  
  # If no output 'display instructions'
  elif show_instructions== "no" or show_instructions == "n":
      print("Display Instructions")
  
  else:
      print("Please enter yes or no")
    