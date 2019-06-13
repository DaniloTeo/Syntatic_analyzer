%{
	#include "y.tab.h"

%}

digito	[0-9]
real {digito}+"."{digito}+

real_err "."{digito}+|{digito}+"."."."{digito}+|{digito}+"."[a-zA-Z]+{digito}+
ident_err [a-zA-Z][a-zA-Z0-9_$#@&]*

ident	[a-zA-Z][a-zA-Z0-9]*

comment	"{".*"}"
erro (@|_|&|$|!|%)*

%%
"program"	{return PROGRAM;}
"begin"		{return BEGIN_P;}
"end"		{return END_P;}
"const"		{return CONST;}
"var"		{return VAR;}
"real"		{return FLOAT;}
"integer"	{return INT;}
"procedure"	{return PROC;}
"if"		{return IF;}
"then"		{return THEN;}
"else"		{return ELSE;}
"read"		{return READ;}
"write"		{return WRITE;}
"while"		{return WHILE;}
"do"		{return DO;}
"for"		{return FOR;}
"to"		{return TO;}

">="		{return GREAT_EQ;}
"<="		{return LESS_EQ;}
"<>"		{return DIFF;}
":="		{return ATT;}
"="		{return EQ;}
">"		{return GREATER;}
"<"		{return LESSER;}
"+"		{return PLUS;}
"-"		{return MINUS;}
"*"		{return STAR;}
"/"		{return DASH;}
")"		{return CLOSE_PAR;}
"("		{return OPEN_PAR;}
","		{return COLON;}
"."		{return DOT;}
";"		{return SEMICOLON;}
":"		{return COMMA;}

{digito}+	{return NUM_INT;}
{real}		{return NUM_REAL;}
{ident}		{return ID;}
{ident_err}	{return ERRO_ID;}
{real_err}	{return ERRO_FLOAT;}
{erro}		{return ERRO_G;}
{comment} ;
[ \t\n]	;
.	;



%%

int init(void){
	yylex();
	
	return 0;
}


