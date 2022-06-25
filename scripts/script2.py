import os
import pandas as pd
import shutil
import random

images = os.listdir('sentiment/sentiment-dataset/images')
print(len(images))

df = pd.read_csv('sentiment/sentiment-dataset/annotations.csv',delimiter=';')

folders = os.listdir('dataset')
#Na brw 30 ana klash kai na ta diagrapsw apo ton katqalogo xtypaei gia ton fakelo test
for i in folders:
    if i != 'test':
      a = len(os.listdir('dataset/'+i))
      randomlist = random.sample(range(1, a), 50)

      files = os.listdir('dataset/'+i)
      print(len(files))

      counter = 0

      for t in files:
          if counter in randomlist:
              old_name = 'dataset/' + i + '/' + t
              abs_path = os.path.abspath(old_name)
              abs_folder = os.path.abspath('dataset/test/'+i)
              new_name = abs_folder + '/' + t + '.jpg'
              shutil.copy(abs_path,new_name)
              os.remove(abs_path)

          counter = counter +1 
          

        



 