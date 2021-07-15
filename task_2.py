from task_1 import scrapping
import json
def group_by_year(movies_list1):
    years=[]
    for i in movies_list1:
        year=i["year"]
        # print(year)
        if year not in years:
            years.append(year)
        years.sort()
    years1={}
    for i in years:
        years1[i]=[]
    for i in movies_list1:
        for j in years1:
            year=i["year"]
            if str(j)==str(year):
                years1[j].append(i)
    with open("task2.json","w") as f2:
        json.dump(years1,f2,indent=4)        
    return years1
group=group_by_year(scrapping)
# print(group_by_year(scrapping))