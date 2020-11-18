import nltk
from prepro_lib.text_cleaner import *

class TextOperations:
     words = None
     def __init__(self,text):
        self.words = text
        #Splitting text into words:
        self.words = nltk.word_tokenize(text)
        
     #Removing repetitive neighbour words in text:           
     def reptWords(self):
         limit = len(self.words)-1
         repWords = []
         for i in range(0,limit):
             if self.words[i]==self.words[i+1]:
                repWords.append(i)
                
         setIndex = 0
         for j in repWords:
             del self.words[j-setIndex]
             setIndex += 1
         return self.words
     
     #Correction of repetitive characters and misspelled words:
     def reptChar_spell(self,corrSent):
         reptReplacer = RepetitionCorrector()
         spellReplacer = SpellingCorrector()
         correctWords = []
         for i in self.words:
              if not i.isalpha():
                   correctWords.append(i)
              else:
                  process1 = reptReplacer.replace(i)
                  process2 = spellReplacer.replace(process1)
                  correctWords.append(process2)
                  
         del self.words
         return correctWords
     
     #Replacing negative words with their antonyms:
     def negWords(self,corrWords):
         negRemover = NegationRemover('antonyms_list.yml')
         cleanWords = negRemover.remove_negations(corrWords)
         return cleanWords
