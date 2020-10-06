#All type of strings can be reversed !

Str = "String"

NewString = ""

#loop from endind to start of the string 
for letter in Str[::-1]:
  
  #adding letter to NewString
  NewString+=letter


#Reversed string will be printed now 
print(NewString)  
