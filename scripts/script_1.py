import os
import pandas as pd
import shutil


images = os.listdir('sentiment/sentiment-dataset/images')
print(len(images))

df = pd.read_csv('sentiment/sentiment-dataset/annotations.csv',delimiter=';')

folders = os.listdir('dataset')
print(folders)

for i in range(len(df)):
    current = df.iloc[i]
    filename = str(current['filename'])
    class_label = str(current['A1.Q1'])
    old_name = 'sentiment/sentiment-dataset/images/' + filename
    abs_path = os.path.abspath(old_name)
    #print(abs_path)
    abs_folder = os.path.abspath('dataset/'+class_label)
    #print(abs_folder)
    new_name = abs_folder + '/' + filename + '.jpg'
    shutil.copy(abs_path,new_name)
    
   
