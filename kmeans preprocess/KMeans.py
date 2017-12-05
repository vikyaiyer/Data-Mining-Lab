import math

class KMeans:
    dataset=[]
    k=1
    meanCluster=[]
    cluster=[]

    def initialize(self):
        self.dataset=[]
        self.meanCluster=[]
        self.cluster=[]

    def initialLoad(self):
        self.cluster=[[] for i in range (self.k)]

        for i in range (self.k):
            self.cluster[i].append(self.dataset[i])
            self.meanCluster.append(self.dataset[i][1:])
            

        for i in range (self.k,len(self.dataset)):
            index=self.checkCluster(self.dataset[i][1:])
            self.cluster[index].append(self.dataset[i])

        self.calculateMean()

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
            self.calculateMean()
            if(flag):
                break

    def calculateMean(self):
        for c in range (len(self.cluster)):
            len_clust=len(self.cluster[c])
            for i in range (len(self.meanCluster[c])):
                self.meanCluster[c][i]=0.0
            for i in range (len_clust):
                for j in range (1,len(self.meanCluster[c])):
                    self.meanCluster[c][j]+=float(self.cluster[c][i][j])
            for i in range (len(self.meanCluster[c])):
                if(len_clust!=0):
                    self.meanCluster[c][i]/=len_clust

    def checkCluster(self,vec):
        mean_vec=[]
        for i in range (len(self.meanCluster)):
            tmp=0
            for j in range (1,len(self.meanCluster[0])):
                try:
                    tmp+=(float(self.meanCluster[i][j])-float(vec[j]))**2
                except:
                    print vec[j]
            tmp=math.sqrt(tmp)
            mean_vec.append(tmp)
        #    print mean_vec
        return mean_vec.index(min(mean_vec))

    def printCluster(self):
        for c in range(len(self.cluster)):
            print "\nCluster: "+str(c)+" \tTotal Elements: "+str(len(self.cluster[c]))
            for i in self.cluster[c]:
                print "  "+str(i)

    def printMean(self):
        for c in range (len(self.meanCluster)):
                print "Cluster: "+str(c)+" \tElements: "+str(len(self.cluster[c]))+" \tMean: "+str(self.meanCluster[c])

    def createClusters(self,dataset,k):
        self.initialize()
        self.dataset=dataset
        self.k=k
        self.initialLoad()
        self.iterateCluster()
        self.printCluster()
        self.printMean()
        return self.cluster

def preprocess():
        for i in dataset:
            for j in range(len(i)):
                if("?" in i[j]):
                    dataset.remove(i)
                    break
                
def loadFile(fileName):
        file_f=open(fileName,"r+")
        for i in file_f:
            dataset.append( i.strip().split(","))
        file_f.close()
        print ("\nDataset '"+fileName+"' loaded")
        print ("Total Elements: "+str(len(dataset))+" \tAttributes: "+str(len(dataset[0])-1))
        return dataset

dataset = []
k = int(input("Enter number of clusters: "))
km = KMeans()
loadFile("StoneFlakes.data")
preprocess()
print "Elements after preprocesssing: "+(str(len(dataset)))
cluster=km.createClusters(dataset,k)
