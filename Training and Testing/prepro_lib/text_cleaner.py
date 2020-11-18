import re
import yaml
import enchant
from nltk.corpus import wordnet
from nltk.metrics import edit_distance

#Class for removing repetitive characters from a word:
class RepetitionCorrector:
 def __init__(self):
  self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
  self.repl = r'\1\2\3'

 def replace(self, word):
  if wordnet.synsets(word):
   return word

  repl_word = self.repeat_regexp.sub(self.repl, word)

  if repl_word != word:
   return self.replace(repl_word)
  else:
   return repl_word

#Class for correcting misspelled words:
class SpellingCorrector:
 def __init__(self, dict_name='en-US', max_dist=2):
  self.spell_dict = enchant.Dict(dict_name)
  self.max_dist = max_dist

 def replace(self, word):
  if self.spell_dict.check(word):
   return word

  suggestions = self.spell_dict.suggest(word)
  if suggestions and edit_distance(word, suggestions[0]) <= self.max_dist:
   return suggestions[0]
  else:
   return word

#Class for replacing negative words with word's antonyms:
class NegationRemover:
 def __init__(self, fileName):
  self.ant_list = yaml.load(open(fileName))

 def remove(self, word):   
  return self.ant_list.get(word, word)

 def remove_negations(self, sent):
  i, l = 0, len(sent)
  words = []
  while i < l:    
    word = sent[i]
    if word == 'not' and i+1 < l:
      antonym = self.remove(sent[i+1])
      if antonym:
        words.append(antonym)
        i += 2
        continue
    
    words.append(word)
    i += 1
    
  return words
