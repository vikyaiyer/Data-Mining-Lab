import math
def mergeCluster(c1,c2):
        for i in cluster[c2]:
                cluster[c1].append(i)
        #print cluster[c1]
        del cluster[c2]
        
def distPoint(x,y):
        dist = 0.0
        for i in range (len(x)-1):     #drops 'label'
                dist += (float(x[i]) - float(y[i])) ** 2
        return math.sqrt(dist)

def distCluster(clust1,clust2):
        dist = 0.0
        for v1 in clust1:
                for v2 in clust2:
                        dist = distPoint(v1,v2)
        return dist
                        
def iterateCluster():
        min_dist = 999999.9
        print "Total Clusters: "+str(len(cluster))+" \t Min Diatance: "+str(min_dist)
        while(True):
                
                if len(cluster)<=1:
                        break
                min_dist = 999999.9
                c1 = 0
                c2 = 0
                curr_dist = 0.0
                for i in range(len(cluster)):
                        for j in range(i+1,len(cluster)):
                                curr_dist = distCluster(cluster[i],cluster[j])
                                if curr_dist < min_dist:
                                        min_dist = curr_dist
                                        c1 = i
                                        c2 = j
                print "Merge cluster "+str(c1)+" and "+str(c2)
                mergeCluster(c1,c2)
                print "Total Clusters: "+str(len(cluster))+" \t Min Diatance: "+str(min_dist)

def loadFile(fileName):
        file_n = open(fileName, "r+")
        for line in file_n:
        	dataset.append(line.strip().split(","))
        file_n.close()
        print "Dataset "+str(file_n)+" loaded"
        print "Total elements: "+str(len(dataset))+" Attributes: "+str(len(dataset[0])-1)
        return dataset
                               
dataset = []
cluster = []
loadFile("iris.data")
cluster = [[] for i in range(len(dataset))]
for i in range (len(dataset)):
        cluster[i].append(dataset[i])
iterateCluster()
