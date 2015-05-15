__author__ = 'diwakarsharma'

import requests as req
from progressbar import ProgressBar
import matplotlib.pyplot as plt
from sys import argv

#method to find the server names and their frequency
def updatedict(_dictserver, _filename):
    try:
        pbar = ProgressBar()
        with open(_filename,'r') as wl:
            lines = wl.readlines()
        for items in pbar(lines):
            r = req.get(items)
            dict = r.headers
            #loop
            for key in dict:
                if key == 'server':
                    if _dictserver.has_key(dict[key]):
                        _dictserver[dict[key]] = _dictserver.get(dict[key])+1
                    else:
                        _dictserver[dict[key]] = 1
    except:
        print "Some web addresses are corrupted and causing connection issues"
    finally:
        return _dictserver


if __name__=='__main__':

    script, filename = argv
    dictserver = {}
    #calling the function to get the name
    print updatedict(dictserver, filename)

    #plotting graph of the servernames and their frequency
    plt.title('Server Frequency')
    plt.ylabel('Server Count')
    plt.xlabel('Server Name')
    plt.bar(range(len(dictserver)), dictserver.values(), align='center')
    plt.xticks(range(len(dictserver)), list(dictserver.keys()))
    plt.savefig('serverplot.png')
    plt.show()
