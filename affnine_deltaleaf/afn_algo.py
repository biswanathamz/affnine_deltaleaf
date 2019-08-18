
#.........................................................................................................................................
import sys
class createNewMap:
    def __init__(self):
        self.nameOfTheMap=""
        self.stationList=[]                                         # Describe all the name of the statiob of the map
        self.noOfStation=0                                          # No of total station of the map
        self.hN=[]                               
        self.maxNum=999                   
        self.distance={}    
        self.mapMatrix=[[0 for x in range(1)] for y in range(1)]  
        self.dacMatrix=[[0 for x in range(1)] for y in range(1)] 
        self.deltaLeafMat=[]     
    #.........................(HURISTICS VALUE).................
    #...........................................................(Add Name Of The Map)...#editnameOfTheMap(self,name)......................
    def editNameOfTheMap(self,name):
        self.nameOfTheMap=name
    #...........................................................(Add New Station)...#addStation(self,name)................................
    def addStation(self,name):
        rowCount=0
        self.stationList.append(name)
        self.noOfStation+=1
        dict = {"goal":name}
        self.hN.append(dict)
        for i in self.mapMatrix:
            i.append(0)
            rowCount=rowCount+1
        self.mapMatrix.append([0 for x in range(rowCount+1)])
        rowCount=0
        for i in self.dacMatrix:
            i.append(0)
            rowCount=rowCount+1
        self.dacMatrix.append([0 for x in range(rowCount+1)])

    #...........................................................(Check Existing Stations)...#checkStation(self,name)......................
    def checkStation(self,name):
        for i in self.stationList:
            if (str(i)==str(name)):
                return True
            else:
                return False
    
    #...........................................................(Add Value of Hn)...#addValueOfHN(self,recent,goal,value).................
    def addValueOfHN(self,recent,goal,value):
        for i in self.hN:
            if (i["goal"]==goal):
                for j in i:
                    if(str(j)==str(recent)):
                        if(str(i[j])>str(value)):
                            i[j]=str(value)
                            return 0
                        else:
                            return 0
                i[str(recent)]=str(value)

    #.........................................................(Distance from one node to another node)...#updateDistance(self,f,t,value)..

    def updateDistance(self,f,t,value):
        index=str(str(f)+" "+str(t))
        self.updateMapMatrix(f,t)
        for i in (self.distance):
            if (str(i)==str(index)):
                if(float(self.distance[i])>float(value)):
                    self.distance[i]=value
                    return 0
                else:
                    return 0
        self.distance[str(index)]=float(value)
    #......................................................(Create Map Matrix)...#updateMapMatrix(self,n1,n2)............................
    def updateMapMatrix(self,n1,n2):
        positionOfN1=0
        positionOfN2=0
        errorVAl=0
        for i in self.stationList:
            if(str(i)==str(n1)):
                errorVAl=1
                break
            positionOfN1+=1
        if (errorVAl==0):
            self.addStation(str(n1))
            # sys.exit("ERROR: "+n1+" not found in your MAP list -> Please add it into maplist first")
        errorVAl=0
        for i in self.stationList:
            if(str(i)==str(n2)):
                errorVAl=1
                break
            positionOfN2+=1
        if (errorVAl==0):
            self.addStation(str(n2))
            # sys.exit("ERROR: "+n2+" not found in your MAP list -> Please add it into maplist first")
        self.mapMatrix[positionOfN1][positionOfN2]=str(1)
        self.mapMatrix[positionOfN2][positionOfN1]=str(1)

#...........................................................................................
class dacMatrixCreator(createNewMap):
    def __init__(self):
        createNewMap.__init__(self)
    def createDacMatrix(self):               #befole calculate hN first call this function createDacMatrix()
        elementArray=[]
        indexOfNode1=0
        indexOfNode2=0
        flag=0
        for element in self.distance:
            elementArray=(element.split())
            for i in self.stationList:
                if (str(i)==str(elementArray[0])):
                    indexOfNode1=flag
                flag+=1
            flag=0
            for i in self.stationList:
                if (str(i)==str(elementArray[1])):
                    indexOfNode2=flag
                flag+=1
            flag=0
            self.dacMatrix[indexOfNode1][indexOfNode2]=self.distance[element]
            self.dacMatrix[indexOfNode2][indexOfNode1]=self.distance[element]
        self.hnCal();
#....................................................................................................
#....................................................................................................
class deltaLeaf(dacMatrixCreator):
    def __init__(self):
        dacMatrixCreator.__init__(self)
    def testPrint(self):
        print(self.dacMatrix)
        print(self.distance)
    def findMin(self,n1,n2):
        if float(n1)<float(n2):
            return float(n1)
        else:
            return float(n2)
    def hnCal(self):                            #................... Floyd-Warshall .................
        noOfStation=int(self.noOfStation)
        var=0
        mat=[[0 for x in range(noOfStation)] for y in range(noOfStation)]
        for i in range(0,noOfStation):
            for j in range(0,noOfStation):
                var=self.dacMatrix[i][j]
                if i==j:
                    var=0
                if i!=j:
                    if float(self.dacMatrix[i][j])==0:
                        var=self.maxNum
                mat[i][j]=var
        for k in range(0,noOfStation):
            for i in range(0,noOfStation):
                for j in range(0,noOfStation):
                    mat[i][j]=(self.findMin((mat[i][j]),(mat[i][k])+(mat[k][j])))
        self.deltaLeafMat=mat
        # print(self.deltaLeafMat)
    # def g_n(self,n1,n2):
    #     pass

    # def h_n(self,n1,n2):
    #     pass

    def finder_(self,start_,end_):                  #................... A* algorithm .................
        var_flag1=0
        start_pos=0
        end_pos=0
        h_val=[0 for x in range(self.noOfStation)]
        path=[]
        for i in self.stationList:
            if (str(start_)==i):
                break
            start_pos=start_pos+1
        for i in self.stationList:
            if (str(end_)==i):
                break
            end_pos=end_pos+1

        if(start_pos>(len(self.stationList)-1)): 
            sys.exit("ERROR: "+start_+" not found in your MAP list -> Please add it into maplist first")

        if (end_pos>(len(self.stationList)-1)):
            sys.exit("ERROR: "+end_+" not found in your MAP list -> Please add it into maplist first")
        
        for i in range(0,self.noOfStation):
            h_val[i]=self.deltaLeafMat[i][end_pos]

        while(True):
            var_dic={}
            # print("sata vanga :"+str(start_pos)+str(end_pos))
            if(start_pos==end_pos):
                return path
            for i in range(0,self.noOfStation):
                if(int(self.mapMatrix[start_pos][i])==1):
                    varTotalDistance=self.dacMatrix[start_pos][i]+h_val[i]
                    var_dic[i]=varTotalDistance
            var_flag1=list(var_dic.keys())[0]
            for i in var_dic:
                if(var_dic[i]<var_dic[var_flag1]):
                    var_flag1=i
            path.append(var_flag1)
            start_pos=var_flag1

    def finder(self,start_,end_):
        res=[]
        res_=[]
        res=self.finder_(start_,end_)
        for i in res:
            res_.append(self.stationList[i])
        return res_












