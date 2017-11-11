from itertools import permutations

def permutation(itemset):
    perm=[]
    for item in itemset:
        perm+=([''.join(p) for p in permutations(item)])
    return perm

def prior_rule(x,s):
    a=''
    b=''
    for l in range(1,len(x)):
        a=x[0:l]
        b=x[l:]
        s.add(''.join(sorted(a))+','+''.join(sorted(b)))
    file = open('example.txt')
    for l in file:
        l = str(l.split())
    file.close()
 
def rule_mining(minsup,s):
    for item in s:
        a,b=map(str,item.split(','))
        if (conf(a,b)>=minsup):
            print('('+a+'->'+b+')'+'[conf='+str(conf(a,b))+']')

def conf(a,b):
    file = open('example.txt')
    ac=0
    bc=0
    for line in file:
        str=''.join(line.split(' '))
        if contains(a,str):
            ac+=1
            if contains(b,str):
                bc+=1
    return bc/(float)(ac)

def contains(a,b):
    c=0
    for i in a:
        if i in b:
            c+=1
    if c==len(a):
        return True
    else:
        return False

def generation(Itemset, length):
    item = []
    item_index = 0
    for i in range (0,length):
        e = str(Itemset[i])
        for j in range (i+1,length):
            e1 = str(Itemset[j])
            if e[0:(len(e)-1)] == e1[0:(len(e1)-1)]:
                    uset = e[0:(len(e)-1)]+e1[len(e1)-1]+e[len(e)-1] 
                    uset = ''.join(sorted(uset))
                    item.append(uset)
    return item

def prune(Ck,minsup):
    L = []
    for i in Ck:
        if Ck[i] >= minsup:
            L.append(i)
    return sorted(L)

def subset_count(item,item_len):
    Lk = dict()
    file = open('example.txt')
    for l in file:
        l = str(l.split())
        count = 0
        for i in range (0,item_len):
            key = str(item[i])
            if key not in Lk:
                Lk[key] = 0
            flag = True
            for k in key:
                if k not in l:
                    flag = False
            if flag:
                Lk[key] += 1
    file.close()
    return Lk

def main(minsup):
    C1={} 
    file = open('example.txt')
    for line in file:
        for item in line.split():
            if item in C1:
                C1[item] +=1
            else:
                C1[item] = 1
    file.close()
    C1.keys().sort()
    L = []
    L1 = prune(C1,minsup)
    L = generation(L1,len(L1))
    print 'Frequent 1-itemset is',L1
    x=permutation(L)

    k=2
    s=set()
    while L != []:
        C = dict()
        C = subset_count(L,len(L))
        fruquent_itemset = []
        fruquent_itemset = prune(C,minsup)
        print 'Frequent',k,'-itemset is',fruquent_itemset
        x=permutation(fruquent_itemset)
        for item in x:
            prior_rule(item,s)
        L = generation(fruquent_itemset,len(fruquent_itemset))
        print(L)
        k += 1
    rule_mining(0.3,s)

main(3)
