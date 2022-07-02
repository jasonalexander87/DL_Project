import os
import pandas as pd
import shutil

def most_frequent(List):
    return max(set(List), key = List.count)


images = os.listdir('sentiment/sentiment-dataset/images')
print(len(images))

df = pd.read_csv('sentiment/sentiment-dataset/annotations.csv',delimiter=';')

folders = os.listdir('dataset')
print(folders)

for i in range(len(df)):
    current = df.iloc[i]
    filename = str(current['filename'])
    class_label1 = current['A1.Q1']
    class_label2 = current['A2.Q1']
    class_label3 = current['A3.Q1']
    class_label4 = current['A4.Q1']
    class_label5 = current['A5.Q1']
    labels=[]
    labels.append(class_label1)
    labels.append(class_label2)
    labels.append(class_label3)
    labels.append(class_label4)
    labels.append(class_label5)
    
    final_label = most_frequent(labels)

    if final_label == 1 or final_label == 2 or final_label == 3:
        final_label = 1
    elif final_label == 4 or final_label == 5 or final_label == 6:
        final_label = 2
    else:
        final_label = 3

    class_label = str(final_label)
    
    old_name = 'sentiment/sentiment-dataset/images/' + filename
    abs_path = os.path.abspath(old_name)
    #print(abs_path)
    abs_folder = os.path.abspath('dataset/'+class_label)
    #print(abs_folder)
    new_name = abs_folder + '/' + filename + '.jpg'
    shutil.copy(abs_path,new_name)
    
   
