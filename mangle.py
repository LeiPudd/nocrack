
import sys, os

# helper script to mangle the letters

from os.path import expanduser
home = expanduser("~");

class NonTerminal:
    type_is = ''
    length = 0;
    def __init__( self, _type_is, length=1 ):
        self.type_is = _type_is;
        self.length = length

    def add(self, _type_is ):
        if ( self.type_is == _type_is ):
            self.length += 1; 
            return True;
        return False;

    def __str__(self):
        return "%s%d" %(self.type_is, self.length)

class Mangle:
    manglingRule=dict()
    def parseManglingRules ( fl_name ):
        global manglingRule;
        with open(fl_name) as f:
            for line in f.readlines() :
                if not line or line[0] == '#': continue;
                line = [x.strip() for x in line.strip().split('->')]
                try:
                    manglingRule[line[0]].append( line[1] );
                except:
                    manglingRule[line[0]] = [line[1]]

    def __init__ ( self, 
                   fl_name = "/home/rahul/Dropbox/HoneyEncryption/ManglingRule.txt" ):
        # TODO - change this path
        parseManglingRules( fl_name );
    
    def mangle( self, w ):
        ret =''
        M = []
        for i,c in enumerate(w):
            if c in manglingRule: 
                ret += manglingRule[c][0];
                M.append(NonTerminal(c,i)) 
            else: ret += c;
        return [M,ret];


def getCapitalizeInfo( w ):
    info = []
    for i, c in enumerate(w):
        if sys.isalpha(c):
            if c.isupper(): info.append(i);
    return converIntoNumber( info );

def converIntoNumber( arr ):
    """
    converts an array of indexes to a 32 bit number
    (0,2,3,9) = (9,3,2,0) = (0x00 00 02 0d) = 
    """
    a=['0' for i in range(64)];
    for x in arr:
        a[x] = '1';
    return int(a,2)

def convertIntoArray( n ):
    a = reversed(bin(n)[2:])
    arr = [];
    for i in xrange(len(a)):
        if a[i] =='1': arr.append(i);
    return arr;

        
        
