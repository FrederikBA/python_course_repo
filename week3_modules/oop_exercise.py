import string

class TextContainer():
  
  def __init__(self, my_text):
    self.my_text = my_text
    
  def count_words(self):
    words = self.my_text.split()
    return len(words)
  
  def count_chars(self):
    return len(self.my_text)
  
  def count_ascii(self):
    count = 0
    for c in self.my_text:
      if c in string.ascii_letters:
        count += 1
    return count
  
  def remove_punct(self):
    new_string = self.my_text.translate(str.maketrans('','', string.punctuation))
    return new_string      
  

tc = TextContainer('Lorem! Ipsum# Dolo# Latin! Stuff?')
print(tc.count_words())
print(tc.count_chars())
print(tc.count_ascii())
print(tc.remove_punct())
  
    
    