import json


with open('dataset.json', 'r') as json_file:
    data = json.load(json_file)
def grad(res):
    if result=="X":
        d=-1
    elif result=="Y":
        d=1
    c[0]=c[0]+(n*d*a[0])
    c[1]=c[1]+(n*d*a[1])
    c[2]=c[2]+(n*d*a[2])

def perc(w,x,b):
    result=0
    for i in range(0,len(w)):
        result+=w[i]*x[i]
    result+=b
    if result>0:
        return "X"
    elif result<=0:
        return "Y"


c=[0,3,1]
b=-8
a=[]
n=0.2
flag=True
while(flag):
    flag=False
    for x in range(0,len(data)):
        for w in range(0,len(data[x]["data"])):
            for y in range(0,len(data[x]["data"][w])):
                if data[x]["data"][w][y]==1:
                    a=[1,w,y]
                   
        result=perc(c,a,b)
        print(c)
        if result != data[x]["result"]:
            flag=True
            #find the loss function
            grad(result)
    print(c)

t=input("enter attribute 1")
r=input("enter attribute 2")
expected=input("enter expected")
nD=[1,int(t),int(r)]
ans=perc(c,nD,b)
print(ans)
if ans!=expected:
    grad(ans)


print(c)