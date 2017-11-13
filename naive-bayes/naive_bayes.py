import pandas as pd


def show(df):
    print(df)


def predict(df,l):
    s=set()
    dict={}
    for i in df.iloc[:,-1]:
        s.add(i)
  
    i=0
    for el in s:
        dict[i]=el
        i+=1
   
    p=[]
    class_dict={}
    for el in s:
        class_dict[el]=df.iloc[:,-1][df.iloc[:,-1]==el].count()/df.iloc[:,-1].count()
    prob=1
    for el in s:
        for i in range(len(l)):
            #print(df.iloc[:,i][(df.iloc[:,-1]==el)&( df.iloc[:,i]==l[i])].count())
            prob=prob*((df.iloc[:,i][(df.iloc[:,-1]==el)&( df.iloc[:,i]==l[i])].count()/df.iloc[:,i].count())/class_dict[el])
        p.append(prob)
        prob=1
    psum=0
    for i in p:
        psum+=i
    for i in range(len(p)):
        p[i]=p[i]/psum
    print(psum)
    print(p)
    print(dict[p.index(max(p))])
        
def main():
    df=pd.read_csv('play.csv')
    l=[]
    attr=df.columns.values
    show(df)
    for i in range(len(attr)-1):
        l.append(input('Enter value for '+attr[i]+':'))
    
   
    predict(df,l)

main()
