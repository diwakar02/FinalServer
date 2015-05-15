__author__ = 'diwakarsharma'

import requests as req
from progressbar import ProgressBar
import matplotlib.pyplot as plt
from sys import argv
import warnings
warnings.filterwarnings('ignore')
import re
#method to find the server names and their frequency
def updatedict(_dictserver, _filename):
    pbar = ProgressBar()
    count = 0
    with open(_filename,'r') as wl:
        lines = wl.readlines()
    for items in pbar(lines):
        try:
            r = req.get(items)
            dict = r.headers
            #loop
            for key in dict:
                if key == 'server':
                    str = dict[key]
                    newkey = re.findall(r"['\w']+", str)
                    if _dictserver.has_key(newkey[0]):
                        _dictserver[newkey[0]] = _dictserver.get(newkey[0])+1
                    else:
                        _dictserver[newkey[0]] = 1
        except req.exceptions.ConnectionError:
            count += 1
            continue
        except req.exceptions.TooManyRedirects:
            count += 1
            continue
    print('Total corrupted files are %d' %count)
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
    plt.savefig('server.png')
    plt.show()
