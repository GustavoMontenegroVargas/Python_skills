# This is an interview excersice from Hackerank
# The objective is to transform the sentence
# in: "a Blue MOON"
# out: "a Blue MOOn"
# We need to modify the sentence keeping the first letter of each word without changes. 
# If the last letter is earlier into the english alphabet, then change the next letter to uppercase and viceversa.

def transformSentence(sentence):

  word = sentence
  Words = word.split()
  
  #print(Words)
  List = []
  
  for word in Words:
    List.append(word[0])
    
    for i in range(1,len(word)):
  #--------------- Is lower
      if word[i].islower() == True:
        
        if (word[i] > word[i-1].lower()):
          List.append(word[i].upper())
        elif word[i] == word[i-1].lower():
          List.append(word[i])
        elif word[i] == " ":
          List.append(word[i])
        elif (word[i] < word[i-1].lower()):
          List.append(word[i].lower())
  
  #--------------- Is upper
  
      elif word[i].isupper() == True:
  
        if (word[i] > word[i-1].upper()):
          List.append(word[i].upper())
        elif word[i] == word[i-1].upper():
          List.append(word[i])
        elif word[i] == " ":
          List.append(word[i])
        elif (word[i] < word[i-1].upper()):
          List.append(word[i].lower())
    
    List.append(" ")
  #print(List)
  
  new_sentence = ""
  
  for i in List:
    new_sentence += i


  return new_sentence

sentence = "a Blue MOON"
print(transformSentence(sentence))



# Si la letra anterior está antes en el orden del alfabeto: Hacerla Mayúscula.

#Si la letra anterior está después en el orden del afabeto: Hacerla Minúscula. 