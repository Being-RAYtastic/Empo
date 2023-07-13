import sys
import argparse

import features.getMainBoxResult as getMainBoxResult
import features.getSideBoxResult as getSideBoxResult

parser = argparse.ArgumentParser()

# arguments
parser.add_argument("query")    
parser.add_argument("-s", "--short", action="store_true")

args = parser.parse_args()

shortAns = args.short   # -s or --short argument
query = str(args.query).lower()
# query = input("Ask: ").lower()

if __name__ == '__main__':
        
    try:
        if shortAns==True:
            getMainBoxResult.getMainBoxResult(query)
        else : 
            getSideBoxResult.getSideBoxResult(query)
            getMainBoxResult.getMainBoxResult(query)
    
    except AttributeError:
        getMainBoxResult.getMainBoxResult(query)
        pass
    except Exception as e:
        print("No Result!") 
                