import math

class KMedoid:
    dataset=[]
    k=1
    clusterMedoid=[]
    cluster=[]

    def initialize(self):
        self.dataset=[]
        self.clusterMedoid=[]
        self.cluster=[]

    def initialLoad(self):
        self.cluster=[[] for i in range (self.k)]

        for i in range (self.k):
            self.cluster[i].append(self.dataset[i])
            self.clusterMedoid.append(self.dataset[i])

        for i in range (self.k,len(self.dataset)):
            index=self.checkCluster(self.dataset[i][:len(self.dataset[0])-1])
            self.cluster[index].append(self.dataset[i])

        self.calculateMedoid()

    def iterateCluster(self):
        while True:
            flag=True
            for c in range (len(self.cluster)):
                for i in self.cluster[c]:
                    index=self.checkCluster(i)
                    if(c!=index):
                        flag=False
                        tmp=i
                        self.cluster[c].remove(tmp)
                        self.cluster[index].append(tmp)
            self.calculateMedoid()
            if(flag):
                break

    def calculateMedoid(self):
        for c in range (len(self.cluster)):
            len_clust=len(self.cluster[c])
            min_dist=99999.9
            index1=0
            for i in range(len(self.cluster[c])):
                curr_dist=0.0
                for j in range(i+1,len(self.cluster[c])):
                    curr_dist+=self.distPoint(self.cluster[c][i],self.cluster[c][j])

                    if curr_dist<min_dist:
                        min_dist=curr_dist
                        index=i
            self.clusterMedoid[c]=self.cluster[c][index]


    def distPoint(self,vec1,vec2):
        dist=0.0
        for i in range (len(vec1)-1):
            dist+=(float(vec1[i])-float(vec2[i]))**2
        return math.sqrt(dist)

    def checkCluster(self,vec):
        dist_vec=[]
        for i in range (len(self.clusterMedoid)):
            tmp=0
            for j in range (len(self.clusterMedoid[0])-1):
                try:
                    tmp+=(float(self.clusterMedoid[i][j])-float(vec[j]))**2
                except:
                    print " sadasd"+str(self.clusterMedoid[i][j])
            tmp=math.sqrt(tmp)
            dist_vec.append(tmp)
        return dist_vec.index(min(dist_vec))

    def printCluster(self):
        for c in range(len(self.cluster)):
            print "\nCluster: "+str(c)+" \tTotal Elements: "+str(len(self.cluster[c]))
            for i in self.cluster[c]:
                print "  "+str(i)

    def printMedoid(self):
        for c in range (len(self.clusterMedoid)):
                print "Cluster: "+str(c)+" \tElements: "+str(len(self.cluster[c]))+" \tMedoid: "+str(self.clusterMedoid[c])

    def createClusters(self,dataset,k):
        self.initialize()
        self.dataset=dataset
        self.k=k
        self.initialLoad()
        self.iterateCluster()
        self.printCluster()
        self.printMedoid()
        return self.cluster

def loadFile(fileName):
        file_f=open(fileName,"r+")
        for i in file_f:
            dataset.append( i.strip().split(","))
        file_f.close()
        print ("\nDataset '"+fileName+"' loaded")
        print ("Total Elements: "+str(len(dataset))+" \tAttributes: "+str(len(dataset[0])-1))
        return dataset

dataset = []
k = int(input("Number of cluster: "))
loadFile("iris.data")
km=KMedoid()
cluster=km.createClusters(dataset,k)
