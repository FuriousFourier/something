import os

os.system("cls" if os.name=="nt" else "clear")
print ("ASCII Code\n\nExit: Esc + enter\n")
while 1:
  user_input=input("Type a character and press enter: ")
  if len(user_input)==0:
    character='\n'
  else:
    character=user_input[0]
  if (ord(character)==27):
    quit()
  print ("Your character: "+character)
  print ("Its ASCII Code is: "+str(ord(character)))
  
