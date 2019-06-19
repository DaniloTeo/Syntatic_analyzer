import re
from nltk.tokenize

'''
TO DO:
	Implementar a obter_simbolo();
	Implementar o parsing neste codigo;
	Implementar regex_match.
	
	arrumar os parametros para a funcao de erro e as chamadas dela tb
'''


LAMBDA = '%$'
ID = '[a-zA-Z][a-zA-Z0-9]*'
NUM_INT = '\d+'
NUM_REAL = "\d+.\d+"


#------------------------------------------------------------------------------------------------------------------

#LISTA DOS PRIMEIROS DE CADA REGRA

p_program = ["program"]
p_corpo = ["begin", "const", 'procedure', 'var', LAMBDA] #%$ - flag de transicao vazia
p_dc = ['const', 'var', 'procedure', LAMBDA]
p_dc_c = ['const', LAMBDA]
p_dc_v = ['var', LAMBDA]
p_tipo_var = ['real', 'integer']
p_variaveis = [ID]
p_mais_var = [',', LAMBDA]
p_dc_p = ['procedure', LAMBDA]
p_parametros = ['(', LAMBDA]
p_lista_par = [ID]
p_mais_par = [';', LAMBDA]
p_corpo_p = ['begin', 'var', LAMBDA]
p_dc_loc = ['var', LAMBDA]
p_lista_arg = ['(', LAMBDA]
p_argumentos = [ID]
p_mais_ident = [';', LAMBDA]
p_pfalsa = ['else', LAMBDA]
p_comandos = ['read', 'write', 'while', 'if', 'begin', 'for', ID, LAMBDA]
p_cmd = ['read', 'write', 'while', 'if', 'begin', 'for', ID]
p_cmd_aux = [':=', '(', LAMBDA]
p_condicao = ['+', '-', '(', ID, NUM_REAL, NUM_INT, LAMBDA]
p_relacao = ['=', '<>', '>=', '<=', '>', '<']
p_expressao = ['+', '-', '(', ID, NUM_REAL, NUM_INT, LAMBDA]
p_op_un = ['+', '-', LAMBDA]
p_outros_termos = ['+', '-']
p_op_ad = ['+', '-']
p_termo = ['+', '-', '(', ID, NUM_REAL, NUM_INT, LAMBDA]
p_mais_fatores = ['*', '/', LAMBDA]
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

def erro(esp, simb, seguidor): #????
	print('Erro!!\ttoken "{esp}" esperado!')
	aux = simb #copia!!
	while(aux not in seguidor):
		aux = obter_simbolo()


# <programa> -> program ident ; <corpo> .

def programa(S):
	if simb == 'program':
		obter_simbolo()
		if simb == ID:
			obter_simbolo()
			if simb == ';':
				obter_simbolo()
				corpo(S)
				if simb == '.':
					obter_simbolo()
				else:
					erro('.', [], S)
			else:
				erro(';', p_corpo, S)
		else:
			erro('identificador', ';', s)
	else:
		erro('program', [ID], S)

# <corpo> -> <dc> begin <comandos> end
def corpo(S):
	dc(S)
	
	if simb == 'begin':
		obter_simbolo()
		comandos('end')

		if simb == 'end':
			obter_simbolo();
		else:
			erro('end',[],S)
	else:
		erro('begin', p_comandos, S)
	
	
	
	


# <dc> -> <dc_c> <dc_v> <dc_p>
def dc(S):
	dc_c(S)
	dc_v(S)
	dc_p(S)

#<dc_c> ::= const ident = <numero> ; <dc_c> | λ
def dc_c(S):
	if simb == 'const':
		obter_simbolo()
		if simb == ID:
			obter_simbolo()
			if simb == '=':
				obter_simbolo()
				dc_c(S)
			else:
				erro('=', p_numero, S)
		else:
			erro('identificador', '=', S)
	else:
		continue #lambda


# <dc_v> -> var <variaveis> : <tipo_var> ; <dc_v> | λ
def dc_v(S):
	if simb == 'var':
		variaveis(S)
		if simb == ',':
			obter_simbolo()
			tipo_var(S)
			if simb == ';':
				obter_simbolo()
				dc_v(S)
			else:
				erro(';', p_dc_v, S)
		else:
			erro(',', p_tipo_var, S)
	else:
		continue

# <tipo_var> ::= real | integer
def tipo_var(S):
	if simb == 'float':
		obter_simbolo()
	else:
		if simb == 'int':
			obter_simbolo()
			else:
				erro('tipo invalido', [], S)

# <variaveis> ::= ident <mais_var>
def variaveis(S):
	if simb == ID:
		obter_simbolo
	else:
		erro('identificador', p_mais_var, S)

# <mais_var> ::= , <variaveis> | λ
def mais_var(S):
	if simb == ',':
		obter_simbolo()
		variaveis(S)
	else:
		continue

# <dc_p> ::= procedure ident <parametros> ; <corpo_p> <dc_p> | λ
def dc_p(S):
	if simb == 'procedure':
		obter_simbolo()
		if simb == ID:
			obter_simbolo()
			if simb == ';':
				obter_simbolo()
				corpo_p(S)
				dc_p()
			else:
				erro(';', p_corpo_p, S)
		else:
			erro('identificador', p_parametros, S)
	else:
		continue


# <parametros> ::= ( <lista_par> ) | λ
def parametros(S):
	if simb == '(':
		obter_simbolo()
		lista_par(S)
		if simb == ')':
			obter_simbolo()
		else:
			erro(')', [], S)
	else:
		continue

# <lista_par> ::= <variaveis> : <tipo_var> <mais_par>
def lista_par(S):
	variaveis(S)
	
	if simb == ':':
		obter_simbolo()
		tipo_var(S)
		mais_par(S)
	else:
		erro(':', p_tipo_var, S)


# <mais_par> ::= ; <lista_par> | λ
def mais_par(S):
	if simb == ';':
		obter_simbolo()
		lista_par(S)
	else:
		continue


# <corpo_p> ::= <dc_loc> begin <comandos> end ;
def corpo_p(S):
	dc_loc(S)

	if simb == 'begin':
		obter_simbolo()
		comandos(S)
		if simb == 'end':
			obter_simbolo()
			if simb == ';':
				obter_simbolo()
			else:
				erro(';', [], S)
		else:
			erro('end', ';', S)
	else:
		erro('begin', p_comandos, S)

# <dc_loc> ::= <dc_v>
def dc_loc(S):
	dc_v(S)

# <lista_arg> ::= ( <argumentos> ) | λ
def lista_arg(S):
	if simb == '(':
		obter_simbolo()
		argumentos(S)
		if simb == ')':
			obter_simbolo()
		else:
			erro(')', [], S)
	else:
		continue

# <argumentos> ::= ident <mais_ident>
def argumentos(S):
	if simb == ID:
		mais_ident(S)
	else:
		erro('identificador', p_mais_ident, S)

# <mais_ident> ::= ; <argumentos> | λ
def mais_ident(S):
	if simb == ';':
		obter_simbolo()
		argumentos(S)
	else:
		continue

# <pfalsa> ::= else <cmd> | λ
def pfalsa(S):
	if simb == 'else':
		obter_simbolo()
		cmd(S)
	else:
		continue

# <comandos> ::= <cmd> ; <comandos> | λ
def comandos(S):
	cmd(S)
	if simb == ';':
		obter_simbolo()

# <cmd> ::= read ( <variaveis> ) |
# write ( <variaveis> ) |
# while ( <condicao> ) do <cmd> |
# if <condicao> then <cmd> <pfalsa> |
# ident := <expressão> |
# ident <lista_arg> |
# begin <comandos> end


def cmd(S):
	if simb == 'read' or simb == 'write':
		obter_simbolo()
		if simb == '(':
			obter_simbolo()
			variaveis(S)
			if simb == ')':
				obter_simbolo()
			else:
				erro(')', [], S)
		else:
			erro('(', p_variaveis, S)
	elif simb == 'while':
		obter_simbolo()
		if simb == '(':
			obter_simbolo()
			condicao(S)
			if simb == ')':
				if simb == 'do':
					obter_simbolo()
					cmd(S)
				else:
					erro('do', p_cmd, S)
			else:
				erro(')', 'do', S)
		else:
			erro('(', p_condicao, S)

	elif simb == 'if':
		obter_simbolo()
		condicao(S)
		if simb == 'then':
			obter_simbolo()
			cmd(S)
			pfalsa(S)
		else:
			erro('then', p_cmd, S)
	elif simb == ID:
		obter_simbolo()
		cmd_aux(S)
	elif simb == 'begin':
		obter_simbolo()
		comandos(S)
		if simb == 'end':
			obter_simbolo()
		else:
			erro('end', [], S)
	elif simb == 'for':
		obter_simbolo()
		if simb == ID:
			obter_simbolo()
			if simb == ':=':
				obter_simbolo()
				expressao(S)
				if simb == 'to':
					obter_simbolo()
					expressao(S)
					if simb == 'do':
						obter_simbolo()
						corpo(S)
					else:
						erro('do', p_corpo, S)
				else:
					erro('to', p_expressao, S)
			else:
				erro(':=', p_expressao, S)
		else:
			erro('identificador', ':=', S)
	else:
		erro('funcao ou laco esperado', [ID, '('] + p_condicao + p_cmd_aux + p_comandos, S)



# <cmd_aux> ::= := <expressao> | <lista_arg>
def cmd_aux(S):
	if simb == ':=':
		obter_simbolo()
		expressao(S)
	else:
		lista_arg(S)

# <condicao> ::= <expressao> <relacao> <expressao>
def condicao(S):
	expressao(S)
	relacao(S)
	expressao(S)

# <relacao> ::= = | <> | >= | <= | > | <
def relacao(S):
	if simb == '=':
		obter_simbolo()
	elif simb == '<>':
		obter_simbolo()
	elif simb == '>=':
		obter_simbolo()
	elif simb == '<=':
		obter_simbolo()
	elif simb == '>':
		obter_simbolo()
	elif simb == '<':
		obter_simbolo()
	else:
		erro('comparador esperado', [], S)


# <expressao> ::= <termo> <outros_termos>
def expressao(S):
	termo(S)
	outros_termos(S)

# <op_un> ::= + | - | λ
def op_un(S):
	if simb == '+':
		obter_simbolo()
	elif simb == '-':
		obter_simbolo()
	else:
		continue

# <outros_termos> ::= <op_ad> <termo> <outros_termos> | λ
def outros_termos(S):
	op_ad(S)
	termo(S)
	outros_termos(S)

# <op_ad> ::= + | -
def op_ad(S):
	if simb == '+':
		obter_simbolo()
	elif simb == '-':
		obter_simbolo()
	else:
		erro('soma ou subtracao esperados', [], S)

# <termo>::= <op_un> <fator> <mais_fatores>
def termo(S):
	op_un(S)
	fator(S)
	mais_fatores(S)

# <mais_fatores> ::= <op_mul> <fator> <mais_fatores> | λ
def mais_fatores(S):
	op_mul(S)
	fator(S)
	mais_fatores(S)

# <op_mul> ::= * | /
def op_mul(S):
	if simb == '*':
		obter_simbolo()
	elif simb == '/':
		obter_simbolo()
	else:
		erro('multiplicacao ou divisao esperados', [], S)

# <fator> ::= ident | <numero> | ( <expressao> )
def fator(S):
	if simb == ID:
		obter_simbolo()
	elif simb == '(':
		obter_simbolo()
		expressao(S)
		if simb == ')':
			obter_simbolo()
		else:
			erro(')', [], S)
	else:
		numero(S)

# <numero> ::= numero_int | numero_real
def numero(S):
	pass
	# Como usar regex para comparacao?????