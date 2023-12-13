import requests
import pandas as pd
from pandas import DataFrame
import json
from pandas import json_normalize
import re
import json



class SymbolList() :
    def __init__(self, jsonFile='./symbol.json') -> None:
        self._urlHead = 'https://99.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124016220284909428906_1701954683581'
        self._urlTail = 'po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1701954683613'
        self._total = 0
        self._pz = 50
        self.df = pd.DataFrame();
        self.getTotalStocks()
        self._jsonFile = jsonFile;
    
    def getJson(self, url):
        text = requests.get(url).text;
        jData = re.findall(r'\{.*\]\}\}', text);
        data = json.loads(jData[0]);
        return data;

    def getTotalStocks(self):
        pn = 1; 
        url = f"{self._urlHead}&pn={pn}&pz={self._pz}{self._urlTail}";
        # &pn=4&pz=20

        data = self.getJson(url)
        self._total = int(data['data']["total"]);

    def fetchStockList(self) :
        pages = int(self._total/self._pz) + 1;
        
        print(f"total: {self._total}    pages: {pages}")
        resDF = DataFrame()
        for pn in range(1, pages):
            url = f"{self._urlHead}&pn={pn}&pz={self._pz}{self._urlTail}";
            data = self.getJson(url)

            d = data['data']["diff"][0];

            df0 = pd.json_normalize(d);

            df0 = df0.loc[:, ["f12", "f14"] ];
            
            print(df0); 
            resDF = [resDF, df0]

        print("\r\n\r\n\r\nfklsjkldjflsjdfj;sj\r\n\r\n")
        
        print(resDF)
        
        print("\r\n\r\njkafsjkjkf")
        print(resDF.loc[:, ["f12"]])
        
def run():
    s = SymbolList()
    s.fetchStockList()
    
run()
