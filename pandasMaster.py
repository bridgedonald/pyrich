import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range("20130101", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))


df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

import datetime


import json

jFile = "person.txt"

df2.index
df2.columns

import os
def checkData():
    data = ''
    if os.path.exists(jFile) :
        with open(jFile, 'r') as f:
            data = json.load(f)
            today = datetime.date.today().isoformat()
            if today in data.keys():
                print("Data of today exists")
                return pd.DataFrame(json.loads(data[today]))

    print("will load data and save")
    dict = {datetime.date.today().isoformat() : df2.to_json()}
    with open(jFile, 'w') as f:
        json.dump(dict, f)
    return df2

checkData()


import requests
import pandas as pd
from pandas import DataFrame
import json
from pandas import json_normalize
import re
import json

def remove_comments(string):
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    def _replacer(match):
        # if the 2nd group (capturing comments) is not None,
        # it means we have captured a non-quoted (real) comment string.
        if match.group(2) is not None:
            return "" # so we will return empty to remove the comment
        else: # otherwise, we will return the 1st group
            return match.group(1) # captured quoted-string
    return regex.sub(_replacer, string)

def removeFunction(string):
    s1 = re.sub(r"\b\w+:function.*\},", ',', string, count = 0)
    return s1;
    
jsFile = "test.txt"
lstLines =[]
with open(jsFile) as f:
    lstLines = f.readlines()
    js = ''
    for lin in lstLines:
        js += (lin + "\n")

js = remove_comments(js)
js = re.sub(r"'", '"', js)
js = re.sub(r"[ \t\r\n]", "", js)
print(js)
js = removeFunction(js)
print(js)


# jsFile = "gridlist3.js"
jsFile = "test.txt"
lstLines =[]
with open(jsFile) as f:
    lstLines = f.readlines()
js = ''
flagStart = 0
for lin in lstLines:
    if flagStart == 0 :
        s = re.findall(r"//首页板块", lin)
        if len(s)>0:
            flagStart = 1;
            print("FFFFFFFFFound")
    
    if flagStart == 1 :        
        s = re.findall(r"//债券市场  可转债比价表", lin)
        if len(s)>0:
            print(lin)
            print("ffffffffound")
            break

        js += (lin + "\n")


data = remove_comments(js)
data = re.sub(r"'", '"', data)
data = re.sub(r"[ \t\r\n]", "", data)
print(data)
# target = re.findall(r"hushenAStock:.+sumcount.+\}\,", data, re.DOTALL)
# print(target[0])
s = f"[{data}]"
s1 = re.sub(r"\b(\w+):", '\"\\1\":', s)
print(s1)
src = json.loads(s1)
print(type(src))

employee_string = """["hushenAStock":{"fields":"f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152","head":[{"title":"序号","type":"seq","show":true,"name":"number"},{"title":"代码","key":"f12","order":true,"href":"<ahref="//quote.eastmoney.com/unify/r/{{0}}.{{1}}"></a>","data":["f13","f12"],"show":true,"name":"Code"},{"title":"加自选","key":"addzixuan","order":true,"href":"<ahref="//quote.eastmoney.com/unify/r/{{0}}.{{1}}"></a>","data":["f13","f12"],"show":true,"name":"Links"}],"sumcount":20},]"""
# s = json.loads(employee_string)
# print(s[0])

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

# raw_data = re.sub(r"^\s+", "_", data, count=0)
# print(type(raw_data))
# print(raw_data)

def readHeads():
    jsFile = "test.txt"
    lstLines =[]
    with open(jsFile) as f:
        lstLines = f.readlines()
    data =''
    print(lstLines)
    for s in lstLines:
        print(type(s))
        s1 = re.sub(r"^\s+|\s+$", s)
        data +=  (s1 +"\r\n")
    print(data)
    raw_data = re.sub(r"^\s+|\s+$", "_", data, count=0)
    print(type(raw_data))
    print(raw_data)
    # jData = re.findall(r'^\s+hushenAStock', data);
        
    # print(jData)

readHeads()   


target_str = "      Jessa   knows testing and machine " + "\r\n" 
target_str += "     222         444 " + "\r\n" 
target_str += "       333             " + "\r\n" 
print(target_str)
res_str = re.sub(r"^\s+|\s+$", "*", target_str, count=0)
print(res_str)


