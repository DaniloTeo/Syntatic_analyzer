/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    PROGRAM = 258,
    BEGIN_P = 259,
    END_P = 260,
    CONST = 261,
    VAR = 262,
    FLOAT = 263,
    INT = 264,
    PROC = 265,
    IF = 266,
    THEN = 267,
    ELSE = 268,
    READ = 269,
    WRITE = 270,
    WHILE = 271,
    DO = 272,
    FOR = 273,
    TO = 274,
    GREAT_EQ = 275,
    LESS_EQ = 276,
    DIFF = 277,
    ATT = 278,
    EQ = 279,
    GREATER = 280,
    LESSER = 281,
    PLUS = 282,
    MINUS = 283,
    STAR = 284,
    DASH = 285,
    CLOSE_PAR = 286,
    OPEN_PAR = 287,
    COLON = 288,
    DOT = 289,
    SEMICOLON = 290,
    COMMA = 291,
    NUM_INT = 292,
    NUM_REAL = 293,
    ID = 294,
    ERRO_ID = 295,
    ERRO_FLOAT = 296,
    ERRO_G = 297
  };
#endif
/* Tokens.  */
#define PROGRAM 258
#define BEGIN_P 259
#define END_P 260
#define CONST 261
#define VAR 262
#define FLOAT 263
#define INT 264
#define PROC 265
#define IF 266
#define THEN 267
#define ELSE 268
#define READ 269
#define WRITE 270
#define WHILE 271
#define DO 272
#define FOR 273
#define TO 274
#define GREAT_EQ 275
#define LESS_EQ 276
#define DIFF 277
#define ATT 278
#define EQ 279
#define GREATER 280
#define LESSER 281
#define PLUS 282
#define MINUS 283
#define STAR 284
#define DASH 285
#define CLOSE_PAR 286
#define OPEN_PAR 287
#define COLON 288
#define DOT 289
#define SEMICOLON 290
#define COMMA 291
#define NUM_INT 292
#define NUM_REAL 293
#define ID 294
#define ERRO_ID 295
#define ERRO_FLOAT 296
#define ERRO_G 297

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
