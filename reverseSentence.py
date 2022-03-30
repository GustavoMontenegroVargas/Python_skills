# This is a excersice from Hacker rank. 
# We need to take the sentence and change it order. 
# in: "aWESOME iS cODING"
# out: "Coding Is Awesome"
# I built two ways to do this.

sentence = "aWESOME iS cODING"

def reverse(sentence):

#SWAPCASE()
  List = []
  for i in sentence:
    if i.islower() == True:
      i = i.upper()
    elif i.isupper() == True:
      i = i.lower()
    List.append(i)
  #print(List)
  
  new_sentence = ""
  
  for word in List:
    new_sentence += str(word) #Suma todos los valores de word
  print(new_sentence)

  #-----------------------
  
  List1 = []
  for i in range(len(new_sentence)):
    if new_sentence[i] == " ":
      List1.append(i)
  
  #print(List1)   
  
  Words = []
  Words.append(new_sentence[0:List1[0]])
  
  for i in range(0,len(List1)-1):
    Words.append(new_sentence[List1[i]+1:List1[i+1]])
    
  Words.append(new_sentence[List1[-1]+1:])
  #print(Words)

  #--------------------------
  
  Words = Words[::-1]
  final_sentence = ""
  
  for word1 in Words:
    final_sentence += str(word1) + " "
  #print(final_sentence)

  return final_sentence

print("This is the complex way: ", reverse(sentence))


#-------------------------
#another way to do this

sentence1 = "wAY eASIEST tHE"

def reverse_easy(sentence1):
  
  sentence1 = sentence1.swapcase()
  Words1 = sentence1.split()
  Words1 = Words1[::-1]
  final_sentence = ""
  for word2 in Words1:
    final_sentence += word2 + " "
  return final_sentence
  
print("This is the easiest way: ", reverse_easy(sentence1))


  


  



