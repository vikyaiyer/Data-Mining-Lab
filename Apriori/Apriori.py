import itertools

def loadFile(filename):
    D=[]
    f=open(filename,"r")
    transactions=0
    for line in f:
        T = []
        transactions += 1
        for word in line.split():
            T.append(word)
            if word not in C1.keys():
                C1[word] = 1
            else:
                count = C1[word]
                C1[word] = count + 1
        D.append(T)
    print "\nDataset: "+filename+" \t Total Elements: "+str(len(D))
    for i in D:
        print " "+str(i)

    print C1
    return D

def computeInitialItemset():
    L1 = []
    for key in C1:
        if (100 * C1[key]/transactions) >= float(support):
            list = []
            list.append(key)
            L1.append(list)
    print "\nFrequent Itemset: 1 \t Elements: "+str(len(L1))
    for i in L1:
        print " "+str(i)
    return L1

def apriori_gen(Lk_1, k):
    length = k
    Ck = []
    for list1 in Lk_1:
        for list2 in Lk_1:
            count = 0
            c = []
            if list1 != list2:
                while count < length-1:
                    if list1[count] != list2[count]:
                        break
                    else:
                        count += 1
                else:
                    if list1[length-1] < list2[length-1]:
                        for item in list1:
                            c.append(item)
                        c.append(list2[length-1])
                        if not has_infrequent_subset(c, Lk_1, k):
                            Ck.append(c)
                            c = []
    return Ck

def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def has_infrequent_subset(c, Lk_1, k):
    list = []
    list = findsubsets(c,k)
    for item in list:
        s = []
        for l in item:
            s.append(l)
        s.sort()
        if s not in Lk_1:
            return True
    return False

def frequent_itemsets():
    k = 2
    Lk_1 = []
    Lk = []
    L = []
    count = 0
    transactions = 0
    for item in L1:
        Lk_1.append(item)
    while Lk_1 != []:
        Ck = []
        Lk = []
        Ck = apriori_gen(Lk_1, k-1)

        for c in Ck:
            count = 0
            transactions = 0
            s = set(c)
            for T in D:
                transactions += 1
                t = set(T)
                if s.issubset(t) == True:
                    count += 1
            if (100 * count/transactions) >= float(support):
                c.sort()
                Lk.append(c)
        Lk_1 = []
        print "\nFrequent Itemset: "+str(k)+" \t Elements: "+str(len(Lk))
        for i in Lk:
            print " "+str(i)
        for l in Lk:
            Lk_1.append(l)
        k += 1
        if Lk != []:
            L.append(Lk)

    return L

def generateAssociationRules():
    s = []
    r = []
    length = 0
    count = 1
    inc1 = 0
    inc2 = 0
    num = 1
    m = []
    L= frequent_itemsets()
    print ("\nAssosication Rules:")
    for list in L:
        for l in list:
            length = len(l)
            count = 1
            while count < length:
                s = []
                r = findsubsets(l,count)
                count += 1
                for item in r:
                    inc1 = 0
                    inc2 = 0
                    s = []
                    m = []
                    for i in item:
                        s.append(i)
                    for T in D:
                        if set(s).issubset(set(T)) == True:
                            inc1 += 1
                        if set(l).issubset(set(T)) == True:
                            inc2 += 1
                    if (100*inc2/inc1 >= float(confidence)):
                        for index in l:
                            if index not in s:
                                m.append(index)
                        print (" Rule: %d \t %s -> %s \t Support: %d \t Confidence: %d" %(num, s, m, 100*inc2/len(D), 100*inc2/inc1))
                        num += 1


C1 = {}
transactions = 0
D = []
T = []
L1=[]

support = input("Enter Support in percentage %: ")
confidence = input("Enter Confidence in percentage %: ")

D=loadFile("DataSet.txt")
transactions=len(D)
L1=computeInitialItemset()
generateAssociationRules()
