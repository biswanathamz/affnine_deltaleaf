# Affnine deltaleaf
[![GitHub Floow](https://img.shields.io/github/followers/biswanathamz?label=Follow&style=social)](https://github.com/biswanathamz)
[![Last commit](https://img.shields.io/github/last-commit/biswanathamz/affnine_deltaleaf)](https://github.com/biswanathamz)
[![python version](https://img.shields.io/pypi/pyversions/3)](https://github.com/biswanathamz)


Easy way to create a MAP (Undirected Graph)and find the shortest path from one Node to another.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install affnine-deltaleaf.

```bash
pip install affnine-deltaleaf
```

## Quickstart

```python
import affnine_deltaleaf as afn_spf 

newMap=afn_spf.deltaLeaf()         #create a object of affnine deltaleaf

newMap.editNameOfTheMap("Miramar") #assign a name to the map

newMap.updateDistance("A","B",1.1) # Distance from one node to another
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

print(newMap.finder('A','E')) .   # Find shortest distance and 
                                  # path between two nodes

```
## Output:
----------------
![t.o](https://raw.githubusercontent.com/biswanathamz/affnine_deltaleaf/master/src/image/Screenshot%202019-08-18%20at%209.05.56%20PM.png)


## GitHub - Link
[affnine-deltaleaf](https://github.com/biswanathamz/affnine_deltaleaf)

## PyPi - Link
[pypi affnine-deltaleaf](https://pypi.org/project/affnine-deltaleaf/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
