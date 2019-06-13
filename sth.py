import re

'''
TO DO:
	substituir todos os 'simb' pela lista de simbolos de sincronizacao
	de cada chamada, seja la como definir isso (qualquer coisa apelamos pro ';')
	
	arrumar os parametros para a funcao de erro e as chamadas dela tb
'''


LAMBDA = '%$'
ID = '[a-zA-Z][a-zA-Z0-9]*'
NUM_INT = '\d+'
NUM_REAL = "\d+[.]\d+"


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

def programa(simb):
	if simb == 'program':
		obter_simbolo()
	else:
		erro('program', ID) #seguidor de program?
	
	if simb == ID: #comparacao de regex???
		obter_simbolo()
	else:
		erro('identificador', ';')
	
	if(simb == ';'):
		obter_simbolo()
	else:
		erro(';', p_corpo)
	
	corpo('.')

	if(simb == '.'):
		obter_simbolo()
	else:
		erro('.')

# <corpo> -> <dc> begin <comandos> end
def corpo(simb):
	dc('begin')
	
	if simb == 'begin':
		obter_simbolo()
	else:
		erro('begin', )
	
	comandos('end')
	
	if simb == 'end':
		obter_simbolo();
	else:
		erro('end', )


# <dc> -> <dc_c> <dc_v> <dc_p>
def dc(simb):
	dc_c(simb)
	dc_v(simb)
	dc_p(simb)

# dc_v> -> var <variaveis> : <tipo_var> ; <dc_v> | λ

def dc_v(simb):
	if simb == 'var':
		obter_simbolo()
	else:
		erro('var', )

	variaveis(':')

	if simb == ':':
		obter_simbolo()
	else:
		erro(':', )

	tipo_var(';')

	if simb == ';':
		obter_simbolo()
	else:
		erro(';', )

	dc_v()