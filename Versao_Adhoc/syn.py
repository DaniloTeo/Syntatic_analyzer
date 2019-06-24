import re
import sys
from nltk.tokenize import RegexpTokenizer

'''
TO DO:
	Implementar a obter_simbolo(); - DONE
	Implementar o parsing neste codigo; - DONE
	Implementar regex_match. - DONE

	Arrumar os parametros para a funcao de erro e as chamadas dela tb - DONE
	Implementar uma main() com mensagem de sucesso ou nao
	Mudar todos os 'simb' para codigo[pos] - DONE
	Mudar todas as comparacoes com 'ID' para b_regex_match - DONE
'''




#------------------------------------------------------------------------------------------------------------------

# Macros de auxilio
ID = '[a-zA-Z][a-zA-Z0-9]*'
NUM_INT = '\d+'
NUM_REAL = "\d+.\d+"

# posicao do leitor do programa sobre o codigo
pos = 0

# Contagem de erros ao longo da execucao
error_count = 0


#LISTA DOS PRIMEIROS DE CADA REGRA

p_program = ["program"]
p_corpo = ["begin", "const", 'procedure', 'var'] #%$ - flag de transicao vazia
p_dc = ['const', 'var', 'procedure']
p_dc_c = ['const']
p_dc_v = ['var']
p_tipo_var = ['real', 'integer']
p_variaveis = [ID]
p_mais_var = [',']
p_dc_p = ['procedure']
p_parametros = ['(']
p_lista_par = [ID]
p_mais_par = [';']
p_corpo_p = ['begin', 'var']
p_dc_loc = ['var']
p_lista_arg = ['(']
p_argumentos = [ID]
p_mais_ident = [';']
p_pfalsa = ['else']
p_comandos = ['read', 'write', 'while', 'if', 'begin', 'for', ID]
p_cmd = ['read', 'write', 'while', 'if', 'begin', 'for', ID]
p_cmd_aux = [':=', '(']
p_condicao = ['+', '-', '(', ID, NUM_REAL, NUM_INT]
p_relacao = ['=', '<>', '>=', '<=', '>', '<']
p_expressao = ['+', '-', '(', ID, NUM_REAL, NUM_INT]
p_op_un = ['+', '-']
p_outros_termos = ['+', '-']
p_op_ad = ['+', '-']
p_termo = ['+', '-', '(', ID, NUM_REAL, NUM_INT]
p_mais_fatores = ['*', '/']
p_op_mul = ['*', '/']
p_fator = ['(', ID, NUM_REAL, NUM_INT]
p_numero = [NUM_INT, NUM_REAL]


# LISTA DE SEGUIDORES DE CADA REGRA

#s_program n existe pois program e inicial
s_corpo = ['.', 'else', ';'] 
s_dc = ['begin']
s_dc_c = ['procedure', 'var', 'begin']
s_dc_v = ['procedure','begin']
s_tipo_var = [';', ')']
s_variaveis = [')', ':']
s_mais_var = [')', ':']
s_dc_p = ['begin']
s_parametros = [';']
s_lista_par = [')']
s_mais_par = [')']
s_corpo_p = ['procedure', 'begin']
s_dc_loc = ['begin']
s_lista_arg = ['else', ';']
s_argumentos = [')']
s_mais_ident = [')']
s_pfalsa = ['else', ';']
s_comandos = ['end']
s_cmd = ['else', ';']
s_cmd_aux = ['else', ';']
s_condicao = [')', 'then']
s_relacao = ['+', '-', '(', ID, NUM_INT, NUM_REAL]
s_expressao = [')', '=', '<>', '>=', '<=', '>', '<', 'to', 'do', 'then', 'else', ';']
s_op_un = ['(', ID, NUM_INT, NUM_REAL]
s_outros_termos = [')', '=', '<>', '>=', '<=', '>', '<', 'to', 'do', 'then', 'else', ';']
s_op_ad = ['+', '-', '(', ID, NUM_INT, NUM_REAL]
s_termo = ['+', '-']
s_mais_fatores = ['+', '-']
s_op_mul = ['(', ID, NUM_INT, NUM_REAL]
s_fator = ['+', '-', '*', '/']
s_numero = [';', '*', '/', '+', '-']

#------------------------------------------------------------------------------------------------------------------

"""
# Codigo para teste
raw = '''program nome1;
{exemplo 1 fdsuafdsaop 3214543254 #$%}
var a, a1, b: integer;
begin
read(a);
a1:= a1*2;
while (a1<0.00) do
begin
write(a1);
a1:= a1-1;
end;
for b:=1 to 10 do
begin
b:=b+2;
a:=a-1;
end;
if a<> b then write(a);
end.'''
"""

raw = input()

# Expressoes regulares para gerar o tokenizador
re_palavras_reservadas = 'program|begin|end|const|var|real|integer|procedure|if|then|else|read|write|while|do|for|to'
re_simbolos = '>=|<=|<>|:=|=|>|<|\+|-|\*|/|\)|\(|,|\.|;|:'
re_num_id = '\d+\.\d+|\d+|[a-zA-Z][a-zA-Z0-9]*'
re_comment = '{.*}'

tok = RegexpTokenizer(re_palavras_reservadas + '|' + re_simbolos + '|' + re_num_id + '|' + re_comment)

# Codigo tokenizado, sobre a qual o programa percorrera
codigo = tok.tokenize(raw)



# INICIO DAS FUNCOES AUXILIARES -------------------------------------------------------------------

def remove_comment():
	global codigo

	for elem in codigo:
		if elem[0] == '{':
			codigo.remove(elem)


# Encapsula o incremento da posicao na leitura do codigo
def obter_simbolo():
	global pos
	if pos < len(codigo):
		pos += 1
		#print(pos)
	else:
		print(f"Error count: {error_count}")
		print("Programa Encerrado.")
		sys.exit()

# Funcao de erro atraves do metodo panico. Recebe uma mensagem a ser imprimida e um conjunto
# de simbolos de sincronização. Incrementa o valor de error_count
def erro(msg, conjunto_sinc): 
	global error_count

	print(f"{pos}: {codigo[pos]}")
	print(f"Erro!!\ttoken '{msg}' esperado!")
	error_count += 1

	for item in conjunto_sinc:
		if item != codigo[pos]:
			obter_simbolo()
		else:
			break

# Realiza um match entre um padrao de expressao regular e uma dada string e retorna True/False
# Ficar atento que isso é um regex match e nao um regex contains
def b_regex_match(pattern, string):
	return re.match(pattern, string) != None
		
# FIM DAS FUNCOES AUXILIARES ------------------------------------------------------------------------

# <programa> -> program ident ; <corpo> .

def programa():
	if codigo[pos] == 'program':
		obter_simbolo()
		if b_regex_match(ID, codigo[pos]):
			obter_simbolo()
			
			if codigo[pos] == ';':
				obter_simbolo()
				corpo()
				if codigo[pos] == '.':
					obter_simbolo()
				else:
					erro('.', [])
			else:
				erro(';', p_corpo + [])
		else:
			erro('identificador', [';'])
	else:
		erro('program', [ID])

# <corpo> -> <dc> begin <comandos> end
def corpo():
	dc()
	
	if codigo[pos] == 'begin':
		obter_simbolo()
		comandos()

		if codigo[pos] == 'end':
			obter_simbolo();
		else:
			erro('end', s_corpo)
	else:
		erro('begin', p_corpo + s_corpo)
	
	
	
	


# <dc> -> <dc_c> <dc_v> <dc_p>
def dc():
	dc_c()
	dc_v()
	dc_p()

#<dc_c> ::= const ident = <numero> ; <dc_c> | λ
def dc_c():
	if codigo[pos] == 'const':
		obter_simbolo()
		
		if b_regex_match(ID, condigo[pos]): 
			obter_simbolo()
		
			if codigo[pos] == '=':
				obter_simbolo()
				dc_c()
			else:
				erro('=', p_numero + s_dc_c)
		else:
			erro('identificador', ['='] + s_dc_c)
	else:
		pass 


# <dc_v> -> var <variaveis> : <tipo_var> ; <dc_v> | λ
def dc_v():
	if codigo[pos] == 'var':
		obter_simbolo()
		variaveis()
		
		if codigo[pos] == ':':
			obter_simbolo()
			tipo_var()
			
			if codigo[pos] == ';':
				obter_simbolo()
				dc_v()
			else:
				erro(';', p_dc_v + s_dc_v)
		else:
			erro(':', p_tipo_var + s_dc_v)
	else:
		pass

# <tipo_var> ::= real | integer
def tipo_var():
	if codigo[pos] == 'float':
		obter_simbolo()
	else:
		if codigo[pos] == 'integer':
			obter_simbolo()
		else:
			erro('tipo invalido', s_tipo_var)

# <variaveis> ::= ident <mais_var>
def variaveis():
	if b_regex_match(ID, codigo[pos]):
		obter_simbolo()
		mais_var()
	
	else:
		erro('identificador', p_mais_var + s_variaveis)

# <mais_var> ::= , <variaveis> | λ
def mais_var():
	if codigo[pos] == ',':
		obter_simbolo()
		variaveis()
	else:
		pass

# <dc_p> ::= procedure ident <parametros> ; <corpo_p> <dc_p> | λ
def dc_p():
	if codigo[pos] == 'procedure':
		obter_simbolo()

		if b_regex_match(ID, codigo[pos]):
			obter_simbolo()

			if codigo[pos] == ';':
				obter_simbolo()
				corpo_p()
				dc_p()
			
			else:
				erro(';', p_corpo_p + s_dc_p)
		else:
			erro('identificador', p_parametros + s_dc_p)
	else:
		pass


# <parametros> ::= ( <lista_par> ) | λ
def parametros():
	if codigo[pos] == '(':
		obter_simbolo()
		lista_par()

		if codigo[pos] == ')':
			obter_simbolo()
		else:
			erro(')', s_parametros)
	else:
		pass

# <lista_par> ::= <variaveis> : <tipo_var> <mais_par>
def lista_par():
	variaveis()
	
	if codigo[pos] == ':':
		obter_simbolo()
		tipo_var()
		mais_par()
	else:
		erro(':', p_tipo_var + s_lista_par)


# <mais_par> ::= ; <lista_par> | λ
def mais_par():
	if codigo[pos] == ';':
		obter_simbolo()
		lista_par()
	else:
		pass


# <corpo_p> ::= <dc_loc> begin <comandos> end ;
def corpo_p():
	dc_loc()

	if codigo[pos] == 'begin':
		obter_simbolo()
		comandos()
		if codigo[pos] == 'end':
			obter_simbolo()
			if codigo[pos] == ';':
				obter_simbolo()
			else:
				erro(';', s_corpo_p)
		else:
			erro('end', [';'] + s_corpo_p)
	else:
		erro('begin', p_comandos + s_corpo_p)

# <dc_loc> ::= <dc_v>
def dc_loc():
	dc_v()

# <lista_arg> ::= ( <argumentos> ) | λ
def lista_arg():
	if codigo[pos] == '(':
		obter_simbolo()
		argumentos()
		
		if codigo[pos] == ')':
			obter_simbolo()
	
		else:
			erro(')', s_lista_arg)
	else:
		pass

# <argumentos> ::= ident <mais_ident>
def argumentos():
	if b_regex_match(ID, codigo[pos]):
		obter_simbolo()
		mais_ident()
	
	else:
		erro('identificador', p_mais_ident + s_argumentos)

# <mais_ident> ::= ; <argumentos> | λ
def mais_ident():
	if codigo[pos] == ';':
		obter_simbolo()
		argumentos()
	else:
		pass

# <pfalsa> ::= else <cmd> | λ
def pfalsa():
	if codigo[pos] == 'else':
		obter_simbolo()
		cmd()
	else:
		pass

# <comandos> ::= <cmd> ; <comandos> | λ
def comandos():
	cmd()
	if codigo[pos] == ';':
		obter_simbolo()

# <cmd> ::= read ( <variaveis> ) |
# write ( <variaveis> ) |
# while ( <condicao> ) do <cmd> |
# if <condicao> then <cmd> <pfalsa> |
# ident := <expressão> |
# ident <lista_arg> |
# begin <comandos> end


def cmd():
	if codigo[pos] == 'read' or codigo[pos] == 'write':
		obter_simbolo()
		
		if codigo[pos] == '(':
			obter_simbolo()
			variaveis()
			
			if codigo[pos] == ')':
				obter_simbolo()
			
			else:
				erro(')', s_cmd)
		else:
			erro('(', p_variaveis + s_cmd)
	
	elif codigo[pos] == 'while':
		obter_simbolo()
		
		if codigo[pos] == '(':
			obter_simbolo()
			condicao()
			
			if codigo[pos] == ')':
				obter_simbolo()
				if codigo[pos] == 'do':
					obter_simbolo()
					cmd()
				else:
					erro('do', p_cmd + s_cmd)
			else:
				erro(')', ['do'] + s_cmd)
		else:
			erro('(', p_condicao + s_cmd)

	elif codigo[pos] == 'if':
		obter_simbolo()
		condicao()
		
		if codigo[pos] == 'then':
			obter_simbolo()
			cmd()
			pfalsa()
		else:
			erro('then', p_cmd + s_cmd)
	
	elif b_regex_match(ID, codigo[pos]):
		obter_simbolo()
		cmd_aux()
	
	elif codigo[pos] == 'begin':
		obter_simbolo()
		comandos()
		
		if codigo[pos] == 'end':
			obter_simbolo()
		else:
			erro('end', s_cmd)
	
	elif codigo[pos] == 'for':
		obter_simbolo()
		
		if b_regex_match(ID, codigo[pos]):
			obter_simbolo()
			
			if codigo[pos] == ':=':
				obter_simbolo()
				expressao()
			
				if codigo[pos] == 'to':
					obter_simbolo()
					expressao()
			
					if codigo[pos] == 'do':
						obter_simbolo()
						corpo()
					else:
						erro('do', p_corpo + s_cmd)
				else:
					erro('to', p_expressao + s_cmd)
			else:
				erro(':=', p_expressao + s_cmd)
		else:
			erro('identificador', [':='] + s_cmd)
	else:
		erro('funcao ou laco esperado', [ID, '('] + p_condicao + p_cmd_aux + p_comandos + s_cmd)



# <cmd_aux> ::= := <expressao> | <lista_arg>
def cmd_aux():
	if codigo[pos] == ':=':
		obter_simbolo()
		expressao()
	
	else:
		lista_arg()

# <condicao> ::= <expressao> <relacao> <expressao>
def condicao():
	expressao()
	relacao()
	expressao()

# <relacao> ::= = | <> | >= | <= | > | <
def relacao():
	if codigo[pos] == '=':
		obter_simbolo()
	
	elif codigo[pos] == '<>':
		obter_simbolo()
	
	elif codigo[pos] == '>=':
		obter_simbolo()
	
	elif codigo[pos] == '<=':
		obter_simbolo()
	
	elif codigo[pos] == '>':
		obter_simbolo()
	
	elif codigo[pos] == '<':
		obter_simbolo()
	
	else:
		erro('comparador esperado', s_relacao)


# <expressao> ::= <termo> <outros_termos>
def expressao():
	termo()
	outros_termos()

# <op_un> ::= + | - | λ
def op_un():
	if codigo[pos] == '+':
		obter_simbolo()
	
	elif codigo[pos] == '-':
		obter_simbolo()
	
	else:
		pass

# <outros_termos> ::= <op_ad> <termo> <outros_termos> | λ
def outros_termos():
	op_ad()
	termo()
	outros_termos()

# <op_ad> ::= + | -
def op_ad():
	if codigo[pos] == '+':
		obter_simbolo()
	
	elif codigo[pos] == '-':
		obter_simbolo()
	
	else:
		erro('soma ou subtracao esperados', s_op_ad)

# <termo>::= <op_un> <fator> <mais_fatores>
def termo():
	op_un()
	fator()
	mais_fatores()

# <mais_fatores> ::= <op_mul> <fator> <mais_fatores> | λ
def mais_fatores():
	op_mul()
	fator()
	mais_fatores()

# <op_mul> ::= * | /
def op_mul():
	if codigo[pos] == '*':
		obter_simbolo()
	
	elif codigo[pos] == '/':
		obter_simbolo()
	
	else:
		erro('multiplicacao ou divisao esperados', s_op_mul)

# <fator> ::= ident | <numero> | ( <expressao> )
def fator():
	if b_regex_match(ID, codigo[pos]):
		obter_simbolo()
	
	elif codigo[pos] == '(':
		obter_simbolo()
		expressao()
	
		if codigo[pos] == ')':
			obter_simbolo()
		else:
			erro(')', s_fator)
	else:
		numero()

# <numero> ::= numero_int | numero_real
def numero():
	if b_regex_match(NUM_INT, simb):
		obter_simbolo()
	
	elif b_regex_match(NUM_REAL, simb):
		obter_simbolo()
	
	else:
		erro('Numero real/inteiro', [], S)


print("Inicio do programa")

remove_comment()
programa()

if error_count == 0:
	print(f"Codigo aceito!!")
else:
	print(f"Codigo possui erros sintáticos!")
print("Programa Encerrado.")



