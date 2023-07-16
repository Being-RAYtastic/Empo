import argparse

import features.getMainBoxResult as getMainBoxResult
import features.getSideBoxResult as getSideBoxResult

parser = argparse.ArgumentParser()

# arguments
parser.add_argument("query")    
parser.add_argument("-s", "--short", action="store_true")
parser.add_argument("-e", "--engine", choices=["google", "duckduckgo"])
args = parser.parse_args()

shortAns = args.short   # -s or --short argument
search_engine = args.engine    # -e or --engine argument: choices(google, duckduckgo)
query = str(args.query).lower()

if __name__ == '__main__':
        
    try:
        if shortAns==True:
            getMainBoxResult.getMainBoxResult(query, search_engine)
        else:
            getSideBoxResult.getSideBoxResult(query, search_engine)
            getMainBoxResult.getMainBoxResult(query, search_engine)


    
    except AttributeError:
        getMainBoxResult.getMainBoxResult(query)
        
    except Exception as e:
        print("No Result!") 
                