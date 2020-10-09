import os
from os import path
import json
import sys
# import pandas as pd
filepath = "studentRecords.json"

def student_create(student) :
    
    i=1
    if path.exists(filepath) :
        if os.stat(filepath).st_size != 0 :
            with open(filepath , 'r',encoding='utf-8') as my_file :
                a = json.load(my_file)
            for key in a :
                i+=1
        
            student1 = {i : student}
            
            with open(filepath , 'w') as my_file :
                a.update(student1)
                json.dump(a,my_file,indent=2)
                
            return student1
        
        else :
            with open(filepath , 'w') as my_file :
                student1 = {i : student}
                json.dump(student1,my_file,indent=2)

            return student1
    else :
        with open(filepath , 'w+') as my_file :
                student1 = {i : student}
                json.dump(student1,my_file,indent=2)

        return student1
    
    
def student_list() :
    with open(filepath,'r',encoding='utf-8') as my_file :
        data = json.load(my_file)
        return data
    #print(pd.read_json(filepath))
        
  #      print('Convert Students Record into the File Type : \n Type 1 for txt file . \n Type 2 for csv file . \n Type 3 json file .')
  #      file_form = input()
  #      if file_form == '1' :
            # Save to txt file
  #      if file_form == '2' :
            # Save to csv file
  #      else :
            # Save to Json file
            
def student_update(a,student) :
    if os.stat(filepath).st_size == 0 :
        txt = "No Student Records Available ."
        return txt
    else :
        with open(filepath,'r',encoding='utf-8') as my_file :
            data = json.load(my_file)
            if data[a] != None :
               data[a] = student 
               with open(filepath,'w') as my_file :
                   json.dump(data,my_file,indent=2)
               return data
        
            else :
                txt = "There is ,No Record is available for this Roll Number ."
                return txt
    
        

def student_delete(a) :
    if os.stat(filepath).st_size == 0 :
        txt = "No Student Records Available"
        return txt
    else :
        with open(filepath,'r',encoding='utf-8') as my_file :
            data = json.load(my_file)
            
            if data[a] != None :
                #del data[a]
                data[a]="This Record is Deleted from System"
            else :
                txt = "There is already , No Record is available for this Roll Number ."
                return txt
    
        with open(filepath,'w') as my_file :
            json.dump(data,my_file,indent=2)
            return data[a]
        
def class_search(class_no) :
#    class_st =[]
#    if os.stat(filepath).st_size == 0 :
#        txt = "No Student Records Available"
#        return txt
#    else :
#        with open(filepath,'r') as my_file :
#            data = json.load(my_file)
#            for x in data :
#                if data[x]["stu_class"] == class_no :
#                    class_st[x] = data[x]
#        return class_st
    txt = "Under Construction Mode"
    return txt

