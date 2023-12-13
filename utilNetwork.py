import requests
import json
import re

urlFull = "https://53.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407856915289720323_1702297078390&pn=2&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1702297078424"

def printDict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            printDict(v)
        print(f'\t{k} : {v}')
        

def dictUrlParse(urlFull):
    url=''; params=''; py = '';
    dict = { "url": f"{urlFull}", "params" : {} }
    if urlFull.count("?"):
        lst = urlFull.split('?')
        dict["url"] = lst[0] + '?'
        
        params = lst[1]
        lst = params.split('&')

        for l in lst:
            kv = l.split("=")
            dict['params'][kv[0]] = kv[1]

    return dict

def printUrlParse(urlFull):
    url=''; params=''; py = '';
    if urlFull.count("?"):
        lst = urlFull.split('?')
        url = lst[0] + '?'
        params = lst[1]
        py += f'url = \"{url}\"\n\n'
        
        py += 'params = { \n'

        lst = params.split('&')

        for l in lst:
            ss = l.split("=")
            py += f'\t\"{ss[0]}\" : \"{ss[1]}\",\n'

        py += '}\n'

        py = re.sub(r",(\s+?})", "\\1", py, re.MULTILINE|re.DOTALL)
 
        print(py)    

d = {"color": "blue", "fruit": {"A":"apple", "B":1}, "pet": "dog"}        
# d = dictUrlParse(urlFull)
printDict(d)


def right_justify(string, row_length=70):
    l = len(string)
    leadingSpace = ' ' * (row_length - l )
    line = f"{leadingSpace}{string}"
    print(line)


