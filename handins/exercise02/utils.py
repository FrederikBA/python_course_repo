import argparse
import os

def get_file_names(folderpath ,out='output.txt'):
  with open(out, 'w') as file_object:
    for f in os.listdir(folderpath):
      file_object.write(f + '\n')
      
      
      
def get_all_file_names(folderpath,out='output.txt'):
  with open(out, 'w') as file_object:
      for (root, dirs, files) in os.walk(folderpath):
        file_object.write(''.join(files) + '\n')
      
  
if __name__ == '__main__':
  #get_file_names('/home/jovyan/my_notebooks')
  #get_all_file_names('/home/jovyan/my_notebooks')
  print('Hello World')