from ply import lex
import codecs
import os
import sys


print("Funcionando")

# Obtenemos el directorio actual
directory = os.getcwd()

# Obtenemos el archivo a leer, deberia ser de los argumentos del programa
file = 'prueba1.gcl'

# Realizamos un join para obtener el path completo del archivo
correct_path = os.path.join(directory, file)

print(correct_path)

# Verificar palabras claves de GCL
keywords = ['TkDeclare','TkIf','TkFi','TkDo','TkOd','TkFor','TkRof']

# Lista de tokens mas palabras reservadas
tokens = keywords + ['TkId','TkNum','TkString','TkTrue','TkFalse','TkOBlock',
                    'TkCBlock','TkSoForth','TkComma','TkOpenPar','TkClosePar',
                    'TkAsig','TkSemicolon','TkArrow', 'TkGuard','TkPlus','TkMinus',
                    'TkMult','TkOr','TkAnd','TkNot','TkLess','TkLeq','TkGeq','TkGreater',
                    'TkEqual','TkNEqual','TkOBracket','TkCBraquet','TkTwoPoints','TkConcat'
                    ]

# Declaracion de tokens en forma de expresiones regulares

t_ignore = '\t'
t_TkOBlock = r'(\x7C \x5B)'
t_TkCBlock = r'(\x5D \x7C)'
t_TkComma = r','
t_TkOpenPar = r'\('
t_TkClosePar = r'\)'
t_TkAsig = r':='
t_TkSemicolon = r';'
t_TkArrow = r'-->'
t_TkGuard = r'\[]'
t_TkPlus = r'\+'
t_TkMinus = r'\-'
t_TkMult = r'\*'
t_TkOr = r'\/'
#Verificar el TkAnd
t_TkAnd = r'/"\"'
t_TkNot = r'!'
t_TkLess = r'<'
t_TkLeq = r'<='
t_TkGeq = r'>='
t_TkGreater = r'>'
t_TkEqual = r'=='
t_TkNEqual = r'!='
t_TkOBracket = r'\['
t_TkCBraquet = r']'
t_TkTwoPoints = r':'
t_TkConcat = r'\.'


def t_TkId(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in keywords:
        t.type = t.value
    return t

def T_TkComment(t):
    r'\#.*'
    pass

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
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

filePointer = codecs.open(correct_path, "r", "utf-8")
data = filePointer.read()
filePointer.close()

lexer.input(data)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)