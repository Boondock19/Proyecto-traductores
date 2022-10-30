from ply import lex
import codecs
import os


print("Funcionando")

# Obtenemos el directorio actual
directory = os.getcwd()

# Obtenemos el archivo a leer, deberia ser de los argumentos del programa
file = 'prueba1.gcl'

# Realizamos un join para obtener el path completo del archivo
correct_path = os.path.join(directory, file)

# Verificar palabras claves de GCL
keywords = ['TkDeclare','TkIf','TkFi','TkDo','TkOd','TkFor','TkRof','TkInt',
            'TkBool'
            ]

# Lista de tokens mas palabras reservadas
tokens = keywords + ['TkId','TkNum','TkString','TkTrue','TkFalse','TkOBlock',
                    'TkCBlock','TkSoForth','TkComma','TkOpenPar','TkClosePar',
                    'TkAsig','TkSemicolon','TkArrow', 'TkGuard','TkPlus','TkMinus',
                    'TkMult','TkOr','TkAnd','TkNot','TkLess','TkLeq','TkGeq','TkGreater',
                    'TkEqual','TkNEqual','TkOBracket','TkCBraquet','TkTwoPoints','TkConcat'
                    ]

# Declaracion de tokens en forma de expresiones regulares

t_ignore = ' [\r\t\f\v ]'
t_TkBool = r'bool'
t_TkTrue = r'true'
t_TkFalse = r'false'
t_TkOBlock = r'\x7C\x5B'
# t_TkCBlock = r'\x5D\x7C'
t_TkComma = r','
t_TkOpenPar = r'\('
t_TkClosePar = r'\)'
t_TkAsig = r':='
t_TkSemicolon = r';'
t_TkArrow = r'-->'
t_TkGuard = r'\x5B\x5D'
t_TkPlus = r'\+'
t_TkMinus = r'\-'
t_TkMult = r'\*'
t_TkOr = r'\x5C\x2F'
#Verificar el TkAnd
t_TkAnd = r'\x2F\x5C'
t_TkNot = r'!'
t_TkLess = r'<'
t_TkLeq = r'<='
t_TkGeq = r'>='
t_TkGreater = r'>'
t_TkEqual = r'=='
t_TkNEqual = r'!='
t_TkOBracket = r'\x5B'
t_TkCBraquet = r'\x5D'
t_TkTwoPoints = r':'
t_TkConcat = r'\.'


def t_TkDeclare(t):
    r'declare'
    return t

def t_TkCBlock(t):
    r']\|'
    return t

def t_TkIf(t):
    r'if'
    return t

def t_TkFi(t):
    r'fi'
    return t

def t_TkDo(t):
    r'do'
    return t

def t_TkOd(t):
    r'od'
    return t

def t_TkFor(t):
    r'for'
    return t

def t_TkRof(t):
    r'rof'
    return t

def t_TkInt(t):
    r'int'
    return t


def T_COMMENT(t):
    r'\/.*'
    pass

def t_TkId(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in keywords:
        t.type = t.value
    return t



def t_TkNum(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TkString(t):
    r'\".*\"'
    t.value = t.value[1:-1]
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    print('El codigo ASCII es: ', ord(t.value[0]))
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

lexer = lex.lex()

filePointer = codecs.open(correct_path, "r", "utf-8")
data = filePointer.read()
filePointer.close()

lexer.input(data)

while True:
    token = lexer.token()
    if not token:
        break
    # print(token)
    print(token.type, token.value, token.lineno, find_column(data,token))