''' *********** TEST CODE YOU CAN IGNORE THIS ********* '''

import re

def analyze( expr ):
    strbuild: int = ''

    for i in range( len( expr ) ):
        if expr[i] == '-':
            if i == 0:
                strbuild = strbuild + '-'
                # for j in range( i + 1, len( expr ) ):
                #     if expr[j].isdigit():
                #         strbuild = strbuild + expr[j]
                #     else:
                #         strbuild = strbuild + ' '
                #         i = i + j
                #         break
        elif expr[i].isdigit():
            strbuild = strbuild + expr[i]
            count: int = 0
            for j in range( i + 1, len( expr ) ):
                if expr[j].isdigit():
                    strbuild = strbuild + expr[j]
                else:
                    count = j
                    strbuild = strbuild + ' '
                    break
                i = i + count
        elif( expr[i] == ' '):
            strbuild = strbuild + ' '

        elif ( isOperator( expr[i] ) ):
            strbuild = strbuild + expr[i] + ' '
    return strbuild

def isOperator( ch: str ):
    ops = [ '+', '-', '/', '*', '^' ]
    # return re.match( "([*+-\/\^])", ch )
    return ch in ops

if __name__ == "__main__":
    expr = '-22457+22*2'
    res = analyze( expr )
    print( "Input:: ", expr )
    print( "Result:: ", res )
