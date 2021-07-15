from pprint import pprint
import requests
import json
import re
from bs4 import BeautifulSoup
r=requests.get("https://affyo.com/networks/gamblingpro/")
soup=BeautifulSoup(r.text,"html.parser")
div=soup.find('div',id="bo")
div2=div.find('div',class_="wr")
sec=div2.find('section',id="ma")
def main():
    nav=sec.find('nav',id="ne-li")
    ull=nav.find('ul').get_text()
    a=re.findall('.[^A-Z]*',ull)
    return a

def main2():
    tr1=sec.find("div",id="ne-ca")
    tr2=tr1.find("table",id="ne-ca-ra",class_="ne-ca-ta ne-ta")
    tr3=tr2.find_all("tr")
    i=1
    a=[]
    b=[]
    while i<len(tr3):
        rat=tr3[i].get_text()
        a.append(rat[-4:])
        b.append(rat[:-4])
        i=i+1
    i=0
    global main_dic
    main_dic={}
    while i<len(a):
        main_dic[b[i]]=a[i]
        i+=1
main2()

def contact():
    cn1=sec.find("div",id="ne-ca")
    cn2=cn1.find("table",id="ne-ca-me",class_="ne-ca-ta ne-ta")
    cn3=cn2.find_all("tr")
    i=1
    list1=[]
    list2=[]
    while i<len(cn3):
        cn4=cn3[i].get_text()
        i=i+1
        for j in cn4:
            if j=="[":
                list1.append(cn4[-11:])
                x=cn4.replace(cn4[-12:],"")
                list2.append(x)
            if j=="/":
                list1.append(cn4[-3:])
                y=cn4.replace(cn4[-3:],"")
                list2.append(y)
    list1.append(cn4[-7:])
    z=cn4.replace(cn4[-7:],"")
    list2.append(z)
    i=0
    global dic2
    dic2={}
    while i<len(list1):
        dic2[list2[i]]=list1[i]
        i+=1
contact()

def tracking():
    trc1=sec.find("div",id="ne-ov-3")
    trc2=trc1.find("table",id="ne-ov-3-ta",class_="ne-ta")
    trc3=trc2.find_all("tr")
    list3=[]
    list4=[]
    i=1
    while i<len(trc3):
        trc4=trc3[i].get_text()
        li=trc4.replace(trc4[-3:],"")
        list3.append(li)
        list4.append(trc4[-3:])
        i=i+1
    global dic3
    dic3={}
    dic3[list3[0]]=list4[0]

tracking()

def offers():
    o1=sec.find("div",id="ne-ov")
    o2=o1.find('table',id="ne-ov-ta",class_="ne-ta")
    o3=o2.find_all("tr")
    i=1
    global dic
    dic={}
    while i<len(o3):
        a=o3[i].get_text()
        if i==1:
            b=a[:15]
            c=a.replace(b,"").split(" ")
            dic[b]=c 
        if i==2:
            b=a[:14]
            a=a.replace(b,"")
            a=a.replace(" ","")
            s=re.findall('.[^A-Z]*', a)
            list1=[]
            list2=[]
            for l in s[:2]:
                list1.append(l)
            for l in s[2:]:
                list2.append(l)
            n=""
            for k in list1:
                n+=k
                n=n+" "
            m=""
            for q in list2:
                m+=q
                m+=""
            dic[b]=[n,m]
        i+=1
offers()


def payment():
    global dictionary
    dictionary={}
    p1=sec.find("div",id="ne-ov-2")
    p2=p1.find("table",id="ne-ov-2-ta",class_="ne-ta")
    p3=p2.find_all("tr")
    i=1
    dic_1={}
    dic_2={}
    dic_3={}
    while i<len(p3):
        z=p3[i].get_text()
        if i==1:
            li=[]
            en=z[-6:]
            li.append(en)
            z=z.replace(en,"")
            dic_1[z]=li
        if i==2:
            global li3
            x=p3[i].get_text()
            li1=[]
            enn=x[13:18]
            ett=x[19:]
            li1.append(enn)
            li1.append(ett)
            li3=x.replace(x[-12:],"")
            dic_2[li3]=li1
        if i==3:
            global li5
            y=p3[i].get_text()
            li4=[]
            li4.append(y[14:22])
            li4.append(y[23:])
            li5=y.replace(y[14:],"")
            dic_3[li5]=li4
        i+=1
    dictionary.update(dic_1)
    dictionary.update(dic_2)
    dictionary.update(dic_3)
payment()

main_dict={}
main_dict["Rating"]=main_dic
main_dict["contact"]=dic2
main_dict["tracking"]=dic3
main_dict["Offers"]=dic
main_dict["payment"]=dictionary

with open("gamling.json","w") as f:
    json.dump(main_dict,f,indent=4)

