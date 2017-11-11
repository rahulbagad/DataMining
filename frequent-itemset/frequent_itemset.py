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
    k=2
    while L != []:
        C = dict()
        C = subset_count(L,len(L))
        fruquent_itemset = []
        fruquent_itemset = prune(C,minsup)
        print 'Frequent',k,'-itemset is',fruquent_itemset
        L = generation(fruquent_itemset,len(fruquent_itemset))
        k += 1

main(3)