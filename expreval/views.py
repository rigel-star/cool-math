from django.shortcuts import render
import re

class ShuntingYardAndEvaluation():

    def __init__( self ):
        pass

    def infixToPostfix( self, infix: str ):
        ops: str = '-+*/^'
        strbuild: str = ''
        stack = []

        tokens = re.split( '\\s', infix )
        for token in tokens:
            if token == '':
                continue

            ch = token #[0]
            idx: int = self.indexOf( ops, ch )

            if ( self.isDigit( ch ) ):
                strbuild = strbuild + token + ' '
            elif ( idx != -1 ):
                #print( "op info::: ", ope.op, ope.prec, ope.idx )

                if ( len( stack ) == 0 ):
                    stack.append( idx )
                else:
                    while stack:
                        prec1: int = int( idx / 2 )
                        prec2: int = int( stack.pop() )
                        #i am appending the popped element because python list
                        #does not have peek function...
                        stack.append( prec2 )
                        prec2 = prec2 / 2

                        if ( prec2 > prec1 or ( prec2 == prec1 and ch != '^' ) ):
                            strbuild = strbuild + ops[ stack.pop() ] + ' '
                        else:
                            break
                    stack.append( idx );
            elif( ch == '(' ):
                stack.append( -2 )
            elif( ch == ')' ):
                peek: int = stack.pop()
                stack.append( peek )
                while peek != -2:
                    strbuild = strbuild + ops[ stack.pop() ] + ' '
                    peek = stack.pop()
                    stack.append( peek )
                stack.pop()
            # else:
            #     strbuild = strbuild + token + ' '

        while stack:
            strbuild = strbuild + ops[ stack.pop() ] + ' '
        return strbuild

    #evluate postfix expression
    def evaluate( self, postfix: str ):
        stack = []
        tokens = re.split( "\\s", postfix )
        res: int = 0
        for token in tokens:
            print( "Evaluating token:: ", token )
            print( "Remaining stack:: ", stack )
            if self.isOperator( token ):
                b: int = stack.pop()
                a: int = stack.pop()

                res = self.doOperation( a, b, token )
                stack.append( res )

            elif self.isDigit( token ):
                stack.append( int( float( token ) ) )
        return res

    def doOperation( self, a: int, b: int, op: str ):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        elif op == "^":
            res: int = 1
            for i in range( 0, b ):
                res = res * a
            return res
        else:
            return 0
        return 0;

    #check if string is operator
    def isOperator( self, ch: str ):
        ops = [ '+', '-', '/', '*', '^' ]
        # return re.match( "([*+-\/\^])", ch )
        return ch in ops

    def isDigit( self, ch: str ):
        return re.match( "^[+-]?[1-9]\d*|0$", ch )

    def analyzeExpr( self, expr: str ):
        strbuild: str = ''
        for i in range( 0, len( expr ) ):
            if expr[i] == '-':
                idx: int = i
                if idx == 0:
                    strbuild = strbuild + expr[i]
                    for j in range( i + 1, len( expr ) ):
                        if self.isDigit( expr[j] ):
                            strbuild = strbuild + expr[j]
                        elif self.isOperator( expr[j] ):
                            strbuild = strbuild + ' ' + expr[j] + ' '
                            break
                        i = j - 1
                elif not self.isDigit( expr[i - 1] ):
                    strbuild = strbuild + expr[i]
                    for j in range( i, len( expr ) ):
                        if self.isDigit( expr[j] ):
                            strbuild = strbuild + expr[j]
                        elif self.isOperator( expr[j] ):
                            strbuild = strbuild + ' ' + expr[j] + ' '
                            break
                        i = j
                else:
                    strbuild = strbuild + expr[i] + ' '

            elif self.isDigit( expr[i] ):
                for k in range( i, len( expr ) ):
                    if self.isDigit( expr[k] ):
                        print( expr[k], " -> Concatenating to previous digit..." )
                        strbuild = strbuild + expr[k]
                    elif self.isOperator( expr[k] ):
                        strbuild = strbuild + ' ' + expr[k] + ' '
                        break
                    i = k
            elif self.isOperator( expr[i] ):
                strbuild = strbuild + expr[i] + ' '
        return strbuild

    def indexOf( self, str, find ):
        idx: int = -1
        for i in range( 0, len( str ) ):
            if ( str[i] == find ):
                idx = i
                break
        return idx


def expreval_home( request ):
    #expr: str = ''
    expr = str( request.POST.get( 'expression' ) )
    print( "Infix:: ", expr )

    sye = ShuntingYardAndEvaluation()

    pst = sye.infixToPostfix( expr )
    print( "Postfix:: ", pst )

    res = sye.evaluate( pst )
    print( "Result:: ", res )

    lol: str = sye.analyzeExpr( "-1+22" )
    #lolspl = re.split( "\\s", lol )
    print( "Analyzed expression:: ", lol )

    return render( request, "expreval.html", { "expr": expr, "ans": res } )
