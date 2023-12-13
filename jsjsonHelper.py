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

# posStart: 0-based indexing position in parameter string
# becare: return value (left, right) point to both delimiters
def findPair(string, posStart, delimiter='{}' ):
    bStart, cursor, count, left, right = [0] * 5 ;   
    
    if bStart == 0 :
        for i in range(posStart, len(string)) :
            cursor = i;
            if string[i] == delimiter[0] : 
                bStart = 1
                count = 1
                left = i
                break;
            
    if bStart == 0:
        return (left, right)
    
    pos = cursor+1
    for i in range(pos, len(string)) :
        cursor = i;
        if string[i] == delimiter[0] :
            count +=1
        if string[i] == delimiter[1] :
            count -=1
        if count == 0:
            right =i
            break
        
    return (left, right)
        
def removeFunctionBody(string):
    pattern = r"\b\w+\s*?:\s*?function"
    matches = re.finditer(pattern, string)

    rcStr = ""; cursor =0;
    for m in matches:
        b = findPair(string, m.start(), '{}')
        rcStr += string[cursor:m.end()]
        cursor = b[1]+1

    rcStr += string[cursor:]
    
    return rcStr

# key in javascript can omit the quotes, but in json, using quotes for keys is mandatory
def addQuotes(string):
    # 
    string = re.sub(r"\b(\w+)\s*?:", '\"\\1\":', string);    
    string = re.sub(r"(:\s*?)(\w+)", '\\1\"\\2\"', string);

    return string
    

def removeWhitespace(string):
    return re.sub(r"[ \t\r\n]", "", string);

class jsHelper():
    def __init__(self, jsFile='./gridlist3.js') -> None:
        self._jsFile = jsFile;
        
    def loadFromJavascript(self):
        strjs =''
        with open(self._jsFile) as f:
            strjs = f.read()

        pattern = r"\{\s*\/\/首页板块"
        matches = re.finditer(pattern, strjs, re.MULTILINE | re.DOTALL)
        
        for m in matches:        
            s, e = findPair(strjs, m.start())
            if e <= s:
                print("can not find what you want in the jvascript file")
                return ''
            else:
                return strjs[s:e+1]
        
        return ''
        
    def getDict(self, jsStr):
        # step1: remove any javascript comments like //... and /*...*/
        jsStr = remove_comments(jsStr)
 
        # strip the HREF key:value. here href info is regarded to be in a line    
        jsStr = re.sub(r'\bhref:.*', '', jsStr)
        # this is a strange key:value, strip it
        jsStr = re.sub(r'\bwenhaoFlag.*', '', jsStr)
        # for this kind of key:value 
        # cb: function(that, row){
        #     return tools.formatNumberSyl(that);
        # }
        # we will remove the function body, ie, strip from { to }, thus to strip the function body completely
        jsStr = removeFunctionBody(jsStr)

        # remove redundant spaces and new line 
        jsStr = re.sub(r"\s+?\n", "\n", jsStr, re.MULTILINE|re.DOTALL)

        #to make sure [...] and {...} is not [...  ,] and {...  ,}
        jsStr = re.sub(r",(\s+?])", "\\1", jsStr, re.MULTILINE|re.DOTALL)
        jsStr = re.sub(r",(\s+?})", "\\1", jsStr, re.MULTILINE|re.DOTALL)
        
        jsStr = re.sub(r"'", '"', jsStr)

        # in python, key-value pair should look like "key": "f241", "kkey":"5". but in javascript, they can be key: "f241", kkey:5
        jsStr = addQuotes(jsStr)
        # with open("./ttt1.txt", "w") as f:
        #     f.write(jsStr)
                
        data = json.loads(jsStr)
        
        return data;

def run():
    h = jsHelper()
    jsStr = h.loadFromJavascript()

    data = h.getDict(jsStr)
    print(data)
    
run()



