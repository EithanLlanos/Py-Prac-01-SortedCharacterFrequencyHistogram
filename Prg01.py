import time
try:
    # srcN = input("Enter the source fille name: \n")
    srcN = "Doc1.txt"
    srcF = open(srcN,"r")
except:
    print("An error has occurred")
    exit(0)
dic={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
# dic={}
buffer=64
readin=0
readin=srcF.read(buffer)
while(readin!=""):
    readin=srcF.read(buffer).lower()
    print(readin)
    for i in readin:
        if i in dic:
            dic[i]+= 1
        
if not len(dic):
    print(srcN + " has no alphabetic character")
    
def val(x):
    return x[1]
dic=sorted(dic.items(),key=val,reverse=True)
for k,v in  dic:
    if v==0 : continue
    print(k + " -> " + str(v))
