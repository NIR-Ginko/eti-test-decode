#!/usr/bin/env python2.7
import csv
import sys

_table = '-=\~!@#$%^&*()_+|¹;:? <>,./AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÀàÁáÂâÃãÄäÅå¨¸ÆæÇçÈèÉéÊêËëÌìÍíÎîÏïĞğÑñÒòÓóÔôÕõÖö×÷ØøÙùÛûİıŞşßÿ`1234567890'
_ex = 'üúÜÚ'

def decode(symbol, position):
    # Position is offset.
    return symbol if symbol in _ex else _table[_table.index(symbol) - position]

def decode_str(string):
    return ''.join([decode(sym, pos + 1) for pos, sym in enumerate(string)])

if  __name__ ==  "__main__" :
    if len(sys.argv) != 3:
        print 'Usage: decode.py <input> <output>'
        print sys.argv[1]
    else:
        with open(sys.argv[1], 'r') as inputfile:
            with open(sys.argv[2], 'w+b') as outputfile:
                reader = csv.reader(inputfile, delimiter=',', quotechar='"')
                writer = csv.writer(outputfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    #print row[0], row[1], decode_str(row[2]), row[3] # Uncomment for output to stdout
                    writer.writerow([row[0], row[1], decode_str(row[2]), row[3]])

