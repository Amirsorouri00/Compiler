from enum import Enum

'''
content 
row
cloumn
type
'''
def show(data):
    print(data)

def IsLetter(c ):
    try :
        c = ord(c)
        return (c >= 65 and c <= 90 ) or (c >= 97 and c <= 122 )
    except Exception :
        return False

def IsDigit(c ):
    try :
        c = ord(c)
        return (c >= 48 and c <= 57 )
    except Exception :
        return False


def IsKeyword(c ):
    return key_words.__contains__(c.replace(' ','') )


key_words = ["False", "None","True", "and", "as", "assert", "", "class", "continue", "def"
    ,"del", "elif","else", "except", "finally", "for", "from", "global", "if", "import"
    ,"in", "is", "lambda","nonlocal", "not", "or", "pass", "raise", "return", "try", "while"
    ,"with", "yield","show"]


class TokenType(Enum ):
    NUMBER = 1
    REAL_NUMBER = 2
    ADD_OPERATOR = 3
    SUBTRACT_OPERATOR = 4
    MULTIPLY_OPERATOR = 5
    MULTIPLY_EQUAL_OPERATOR = 6
    DIVIDE_OPERATOR = 7
    DIVIDE_EQUAL_OPERATOR = 8
    STRING_LITERAL = 9
    MODULUS_OPERATOR = 10
    MODULUS_EQUAL_OPERATOR = 11
    ADD_EQUAL_OPERATOR = 12
    SUBTRACT_EQUAL_OPERATOR = 13
    END_STATEMENT = 14
    COLON = 15
    NOT = 16
    NOT_EQUAL = 17
    COMMA = 18
    ASSIGNMENT = 19
    SEMICOLON = 20
    EQUAL_TO = 21
    EXPONENT = 22
    SMALLER_THAN  = 23
    SMALLER_THAN_EQUAL = 24
    LARGER_THAN = 25
    LARGER_THAN_EQUAL =  26
    IDENTIFIER = 27
    KEYWORD = 28
    BINARY_AND = 29
    BINARY_OR = 30
    BINARY_XOR = 31
    SHIFT_LEFT = 32
    SHIFT_RIGHT = 33
    O_PARENTHESE = 34
    C_PARENTHESE = 35
    FLOOR_DIVISION = 36
    INDENT = 37
    DEDENT = 38


def filereader(address):
    file = open(address,'r' )
    state = 0
    buffer = '' 
    data =''
    lastchar= '\0'
    type = ''
    row = 1
    column =1
    lastcl = 1
    IDpossible = 0
    needed = 2
    while(1):
        if needed > 1:
            data = file.read(1)
      
        # if(data =='\n'):
        #     column = 0
        #     row += 1
        #     IDpossible = 1
        if state == 0:

            if (data == '\r' ):
                pass
            if (data == '\t' ):
                column += 4

            elif (data == '\n' ):
                column = 1
                row +=1
                IDpossible = 1

                
            elif (data == ' ' ):
                column +=1
         



            elif(IsLetter(data )):
                state = 1
                buffer += data
                column +=1
                
            elif (IsDigit(data )):
                state = 2 
                column +=1 
                buffer += data 
                 
            elif (data == ':' ):
                column +=1
                show( [":", TokenType.COLON, row, column])


                buffer = ''     
                data ='' 
            
            elif (data == '=' ):
         
                column += 1 
                state = 17 

            elif (data == '#' ):
                state = 4
         





            elif (data == ',' ):

                column +=1 
                show([",", TokenType.COMMA, row, column]) 
                buffer = ''     
                data =''
            elif (data == '(' ):
            
                column +=1 
                show(["(", TokenType.O_PARENTHESE, row, column])
                buffer = ''
                data =''
            elif (data == ')' ):
            
                column +=1 
                show([")", TokenType.C_PARENTHESE, row, column])
                buffer = ''     
                data =''
            elif (data == '.' ):

                column +=1 
                show([".", TokenType.C_PARENTHESE, row, column])
                buffer = ''     
                data =''
         
            elif (data == '+' ):
                column +=1 
                state = 10
         



            elif (data == '-' ):
                
                column +=1 
                state = 11
         

            elif (data == '%' ):
            
                column +=1 
                state = 12
         


            elif (data == '*' ):
                
                column +=1 
                state = 13
         


            elif (data == '/' ):
                
                column +=1 
                state = 14


            elif (data == '>' ):
                
                column +=1 
                state = 15


            elif (data == '<' ):
                
                column +=1 
                state = 16


            elif (data == '!' ):
                
                column +=1
                state = 18


            elif (data == '&' ):
             
                column +=1 
                show(["&", TokenType.BINARY_AND, row, column])
                buffer = ''     
                data =''
            elif (data == '|' ):
                
                column +=1 
                show(["|", TokenType.BINARY_OR, row, column]) 
                buffer = ''
                data =''
            elif (data == '^' ):
                
                column +=1 
                show(["^", TokenType.BINARY_XOR, row, column])
                buffer = ''     
                data =''
            elif (data=='"'):
                state = 5
            elif (data=="'"):
                state = 6
            elif (data=='`'):
                state = 7   
            buffer += data
        elif state == 1:
            column+=1
            if ((IsLetter(data) or IsDigit(data) or data == '_')==False):
                needed =0
                lastcharacter = data
                buffer = buffer.lstrip()
                if(IsKeyword(buffer[1:])):
                    type = TokenType.KEYWORD
                else:
                    type = TokenType.IDENTIFIER
                state = 0
                tempcl = column - len(buffer)
                if (IDpossible):
                    if (tempcl > lastcl):
                        show(["  ", TokenType.INDENT, row, tempcl])
                    if (tempcl < lastcl):
                        show([" ", TokenType.DEDENT, row, tempcl])
                    lastcl = tempcl
                IDpossible = 0

                show([buffer[1:], type, row, tempcl])

                buffer = ''
            buffer += data
            
        elif state == 2:

            column+=1
            type = TokenType.NUMBER
            if (IsDigit(data)==False):
            
                if (data == '.'):
                    state = 3
                    buffer += data
                else:
                    lastcharacter = data
                    state = 0
                    show([buffer[1:], type, row, column - len(buffer)])
                    # if (IDpossible):
                    #     if (column > lastcl):
                    #         show(["  ", TokenType.INDENT, row, column])
                    #     if (column < lastcl):
                    #         show([" ", TokenType.DEDENT, row, column])
                    # IDpossible = 0
                    if data =='\n':
                        row +=1
                        column= 1
                        IDpossible = 1
                    buffer = ''     
                    data =''

            buffer += data
        elif state == 3:
            type = TokenType.REAL_NUMBER
            column+=1
            if (IsDigit(data)==False):
                lastcharacter = data
                state = 0
                # if (IDpossible):
                #     if (column - len(buffer[1:]) > lastcl):
                #         show(["  ", TokenType.INDENT, row, 1])
                #         lastcl = column - len(buffer[1:])
                #     if (column - len(buffer[1:]) < lastcl):
                #         show([" ", TokenType.DEDENT, row, 1])
                #         lastcl = column - len(buffer[1:])
                # IDpossible = 0

                show([buffer[1:], type, row, column - len(buffer)])
                buffer = ''
                data =''
            buffer += data
        elif state == 4:

            if (data == '\n'):    
                row+=1
                state = 0
                column =1
                # IDpossible = 1
                        
        elif state == 5:
            column+=1
            if (data == '"'):
                buffer += data
                state = 0
                show([buffer[:], TokenType.STRING_LITERAL, row , column - len(buffer)])
                buffer = ''
                data =''
            buffer += data
                
        elif state == 6:
            column+=1
            if (data == "'"):
                buffer += data
                show([buffer[:], TokenType.STRING_LITERAL, row , column - len(buffer)])
                state = 0
                buffer = ''
                data =''
            buffer += data
                    
        elif state == 7:
            column+=1
            if (data == '`'):
                buffer += data
                show([buffer[:], TokenType.STRING_LITERAL, row , column - len(buffer)])
                state = 0
                buffer = ''
                data =''
            buffer += data
                            
        elif state == 10:
            column+=1
            state = 0
            if (data == '='):
            
                show(["+=", TokenType.ADD_EQUAL_OPERATOR, row, column])
                buffer = ''     
                data =''
            else:
            
                lastcharacter = data
                show(["+", TokenType.ADD_OPERATOR, row, column])
                buffer = ''     
                data =''
        elif state == 11:
            column+=1
            state = 0
            if (data == '='):
                show(["-=", TokenType.SUBTRACT_EQUAL_OPERATOR, row, column])
                buffer = ''     
                data =''
            else:
                lastcharacter = data
                show(["-", TokenType.SUBTRACT_OPERATOR, row, column])
                buffer = ''     
                data =''
        elif state == 12:
            column+=1
            state = 0
            if (data == '='):
            
                show(["%=", TokenType.MODULUS_EQUAL_OPERATOR, row, column])
                buffer = ''     
                data =''
            else:
            
                lastcharacter = data
                show(["%", TokenType.MODULUS_OPERATOR, row, column])
                buffer = ''     
                data =''
        elif state == 13:
            column+=1
            state = 0
            if (data == '='):
            
                show(["*=", TokenType.MULTIPLY_EQUAL_OPERATOR, row, column])
                buffer = ''
                data =''
            elif (data == '*'):
            
                show(["**", TokenType.EXPONENT, row, column])
                buffer = ''     
                data =''
            else:
                lastcharacter = data
                show(["*", TokenType.MULTIPLY_OPERATOR, row, column])
                buffer = ''     
                data =''
        elif state == 14:

            column+=1
            state = 0
            if (data == '='):
            
                show(["/=", TokenType.DIVIDE_EQUAL_OPERATOR, row, column])
                buffer = ''     
                data =''
            elif (data == '/'):
            
                show(["#", TokenType.FLOOR_DIVISION, row, column])
                buffer = ''     
                data =''
            else:
                lastcharacter = data
                show(["/", TokenType.DIVIDE_OPERATOR, row, column])
                buffer = ''     
                data =''
        elif state == 15:
                column+=1
                state = 0
                if (data == '='):
                
                    show([">=", TokenType.LARGER_THAN_EQUAL, row, column])
                    buffer = ''     
                    data =''
                elif (data == '>'):
                
                    show([">>", TokenType.SHIFT_RIGHT, row, column])
                    buffer = ''     
                    data =''
                else:
                
                    lastcharacter = data
                    show([">", TokenType.LARGER_THAN, row, column])
                    # if (IDpossible):
                    #     if (column > lastcl):
                    #         show(["  ", TokenType.INDENT, row, column])
                    #         lastcl = column
                    #     if (column < lastcl):
                    #         show([" ", TokenType.DEDENT, row, column])
                    #         lastcl = column
                    # IDpossible = 0
                    buffer = ''
                    data =''
        elif state == 16:

            column+=1
            state = 0
            if (data == '='):
            
                show(["<=", TokenType.SMALLER_THAN_EQUAL, row, column])
                buffer = ''     
                data =''
            elif (data == '<'):
        
                show(["<<", TokenType.SHIFT_LEFT, row, column])
                buffer = ''     
                data =''
            else:
            
                lastcharacter = data
                show(["<", TokenType.SMALLER_THAN, row, column])
                buffer = ''     
                data =''
        
        elif state == 17:
            column+=1
            state = 0
            if (data == '='):
            
                show(["==", TokenType.EQUAL_TO, row, column - 1])
                buffer = ''     
                data =''
            else:
            
                lastcharacter = data
                show(["=", TokenType.ASSIGNMENT, row, column - 1])
                buffer = ''     
                data =''

        elif state == 18:
            column+=1
            state = 0
            if (data == '='):
                show(["!=", TokenType.NOT_EQUAL, row, column])
                buffer = ''     
                data =''
            else:
                lastcharacter = data
                show(["!", TokenType.NOT, row, column])
                buffer = ''     
                data =''
        needed +=1
        if not lastchar:
            print("DONE :))")
            break            

filereader('test1.py')
