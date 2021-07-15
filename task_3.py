from task_2 import group
import json
def sequence_of_year(movies_list):
    years_list=[]
    for index in movies_list:
        # print(index)
        year_modules=index%10
        a=index-year_modules
        if a not in years_list:
            years_list.append(a)
    dict1={}
    # years_list.sort()
    for i in years_list:
        dict1[i]=[]
    for i in dict1:
        year1=i+9
        for year2 in movies_list:
            # print(year2)
            for year3 in movies_list[year2]:
                # print(year3)
                if year2<=year1 and year2>=i:
                    dict1[i].append(year3)
    with open("task3.json","a") as f2:
        json.dump(dict1,f2,indent=4)        
sequence_of_year(group)
         

