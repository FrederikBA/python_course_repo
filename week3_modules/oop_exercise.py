class TextContainer():
  
  def __init__(self, my_text):
    self.my_text = my_text
    
  def count_words(self):
    words = self.my_text.split()
    return len(words)
  
  def count_chars(self):
    return len(self.my_text)
  

tc = TextContainer('Lorem Ipsum Dolo Latin Stuff')
print(tc.count_words())
print(tc.count_chars())
  
    
    