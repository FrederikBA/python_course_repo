import argparse

#Exercise 1
#1.A
def read_csv_file(file):
  with open(file) as file_object:
    contents = file_object.read()
    print(contents)

#1.B
def write_list_to_file(output_file, *args):
  with open(output_file, 'w') as file_object:
    for i in args:
      file_object.write(i + '\n')
  
#1.C
def read_csv(input_file):
  with open(input_file) as file_object:
    file_list = [line.strip() for line in file_object]
    print(file_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that can read from a file given a path and print it')
    parser.add_argument('path', help='Path to the csv file')
    args = parser.parse_args()
    #read_csv_file('numbers.csv')
    #write_list_to_file('textfile.txt', 'Johan', 'Anders', 'Line')
    read_csv(args.path)

  
  

  
  