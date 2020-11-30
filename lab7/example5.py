password = input("Enter a password: ")
is_uppercase = False
is_lowercase = False
is_number = False
length = len(password)
for i in password:
  if "a" <= i <= "z":
    is_lowercase = True
  elif "A" <= i <= "Z":
    is_uppercase = True
  elif "0" <= i <= "9":
    is_number = True
if is_lowercase and is_number and is_uppercase and (length>=8):
  print("Valid password")
else:
  print("Invalid password")