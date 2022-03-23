print("This is the email slicer".title())
print("\n")
print('This program will slice your email')
print("\n")
#get user email address
email = input("What is your email address?: ").strip()
print("\n")

def Buscar_posición(text,character):
  numbers = []
  for i in range(len(text)):
    if text[i] == character:
      numbers.append(i)
  return numbers

A = Buscar_posición(email,'.')

#slice out user name
user = email[0:email.index('@')]

#slice domain name
domain = email[(email.index("@"))+1:A[-1]]
domain1 = email[(email.index("@"))+1:] 

#format message
print(f"This is your user name: {user}")
print(f"This is your domain: {domain}")
print(f"This is your whole domain: {domain1}")