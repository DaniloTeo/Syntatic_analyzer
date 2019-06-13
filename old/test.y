%{
	#include<stdio.h>	
%}
%token PROGRAM BEGIN_P END_P CONST VAR FLOAT INT
%token PROC IF THEN ELSE READ WRITE WHILE DO FOR TO
%token GREAT_EQ LESS_EQ DIFF ATT EQ GREATER LESSER
%token PLUS MINUS STAR DASH CLOSE_PAR OPEN_PAR COLON DOT SEMICOLON COMMA 
%token NUM_INT NUM_REAL ID
%token ERRO_ID ERRO_FLOAT ERRO_G



%%
program: PROGRAM ID SEMICOLON corpo DOT;
corpo: dc BEGIN_P comandos END_P;
dc: dc_c dc_v dc_p;
dc_c: CONST ID EQ numero SEMICOLON dc_c | /*empty*/;
dc_v: VAR variaveis COLON tipo_var SEMICOLON dc_v | /*empty*/;
tipo_var: FLOAT | INT;
variaveis: ID mais_var;
mais_var: COMMA variaveis | /*empty*/;
dc_p: PROC ID parametros SEMICOLON corpo_p dc_p| /*empty*/;
parametros: OPEN_PAR lista_par CLOSE_PAR | /*empty*/;
lista_par: variaveis COLON tipo_var mais_par;
mais_par: SEMICOLON lista_par | /*empty*/;
corpo_p: dc_loc BEGIN_P comandos END_P SEMICOLON;
dc_loc: dc_v;
lista_arg: OPEN_PAR argumentos CLOSE_PAR | /*empty*/;
argumentos: ID mais_ident;
mais_ident: SEMICOLON argumentos| /*empty*/;
pfalsa: ELSE cmd | /*empty*/;
comandos: cmd SEMICOLON | /*empty*/;
cmd: READ OPEN_PAR variaveis CLOSE_PAR
	| WRITE OPEN_PAR variaveis CLOSE_PAR
	| WHILE OPEN_PAR condicao CLOSE_PAR DO cmd
	| IF condicao THEN cmd pfalsa
	| ID cmd_aux
	| BEGIN_P comandos END_P
	| FOR ID ATT expressao TO expressao DO corpo;
cmd_aux: ATT expressao | lista_arg;
condicao: expressao relacao expressao;
relacao: EQ | DIFF | GREAT_EQ | LESS_EQ | GREATER | LESSER;
expressao: termo outros_termos;
op_un: PLUS | MINUS | /*empty*/;
outros_termos: op_ad termo outros_termos;
op_ad: PLUS | MINUS;
termo: op_un fator mais_fatores;
mais_fatores: op_mul fator mais_fatores | /*empty*/;
op_mul: STAR | DASH;
fator: ID | numero | OPEN_PAR expressao CLOSE_PAR;
numero: NUM_INT | NUM_REAL;


%%
void main()
{
	printf("digite expr : \n");
	if(yyparse() == 0) printf("expr válida \n");
}
yywrap(){}
yyerror()
{
	printf("Error\n");
}
