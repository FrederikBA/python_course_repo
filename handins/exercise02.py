#Exercise 1
#A
def read_csv_file(file):
  with open(file) as file_object:
    contents = file_object.read()
    print(contents)

#B
def write_list_to_file(output_file, *args):
  with open(output_file, 'w') as file_object:
    for i in args:
      file_object.write(i + '\n')
  
#C
def read_csv(input_file):
  with open(input_file) as file_object:
    names = [name.strip() for name in file_object]
    print(names)
      

if __name__ == '__main__':
  #read_csv_file('exercise02files/numbers.csv')
  #write_list_to_file('exercise02files/textfile.txt', 'Johan', 'Anders', 'Line')
  read_csv('exercise02files/textfile.txt')
  
  

  
  