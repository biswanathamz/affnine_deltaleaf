import affnine_deltaleaf as afn_spf        
def main():
    newMap=afn_spf.deltaLeaf()
    newMap.editNameOfTheMap("Miramar")
    newMap.updateDistance("A","B",1.1)
    newMap.updateDistance("A","D",2)
    newMap.updateDistance("A","E",4)
    newMap.updateDistance("B","E",2)
    newMap.updateDistance("C","E",1)
    newMap.updateDistance("C","D",5)
    newMap.updateDistance("D","F",3)
    newMap.updateDistance("E","F",3.4)
    newMap.updateDistance("F","A",3)
    newMap.updateDistance("G","B",3)
    newMap.updateDistance("H","A",3)
    newMap.updateDistance("I","C",3)
    newMap.updateDistance("J","B",3)
    newMap.updateDistance("K","E",3)
    newMap.createDacMatrix()
    #newMap.testPrint()
    print(newMap.finder('A','E'))

#########################################################################################################################################
if __name__== "__main__":
  main()
#########################################################################################################################################