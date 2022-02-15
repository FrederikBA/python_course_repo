class InvalidArgumentException(ValueError):
  
  def __init__(self, message):
    self.message = message
    

class Person():

  def __init__(self, name):
    self.name = name
        
  def check_name(self):
    if self.name[0].isupper() == False:
      raise InvalidArgumentException('Name has to start with capital letters')
    else:
      print('Name is fine')
 
p1 = Person('Lars')
p2 = Person('Jens')

p1.check_name()
p2.check_name()


    