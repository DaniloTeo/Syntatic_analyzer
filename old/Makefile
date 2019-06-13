all:
	yacc -d test.y
	lex test.l
	cc -o t lex.yy.c y.tab.c -ly
clean:
	rm y.tab.*
	rm lex.yy.c
	rm t
run:
	./t
	