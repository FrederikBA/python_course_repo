import os

def get_file_names(folderpath ,out='output.txt'):
  with open(out, 'w') as file_object:
    for f in os.listdir(folderpath):
      file_object.write(f + '\n')
      
      
def get_all_file_names(folderpath,out='output.txt'):
  with open(out, 'w') as file_object:
      for (root, dirs, files) in os.walk(folderpath):
          for f in files:
            file_object.write(f + '\n')
      
            
def print_line_one(folderpath):
  for file in os.listdir(folderpath):
    with open(file) as file_object:
      print(file_object.readline())
      
      
def print_emails(folderpath):
  for file in os.listdir(folderpath):
    with open(file) as file_object:
      for line in file_object.readlines():
        if '@' in line: print(line)
  
  
def write_headlines(folderpath, out='output.txt'):
  with open(out, 'w') as file_obj:
    for file in os.listdir(folderpath):
      if file.endswith('.md'):
        with open(file) as file_object:
          for line in file_object.readlines():
            if line.startswith('#'):
                file_obj.write(line + '\n')


if __name__ == '__main__':
  #get_file_names('/home/jovyan/my_notebooks')
  #get_all_file_names('/home/jovyan/my_notebooks/handins')
  #print_line_one('/home/jovyan/my_notebooks/handins/exercise02')
  #print_emails('/home/jovyan/my_notebooks/handins/exercise02')
  #write_headlines('/home/jovyan/my_notebooks/handins/exercise02')
  print('hello world')
  