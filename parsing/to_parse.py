import re
from nltk.tokenize import RegexpTokenizer

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
re_palavras_reservadas = 'program|begin|end|const|var|real|integer|procedure|if|then|else|read|write|while|do|for|to'
re_simbolos = '>=|<=|<>|:=|=|>|<|\+|-|\*|/|\)|\(|,|\.|;|:'
re_num_id = '\d+\.\d+|\d+|[a-zA-Z][a-zA-Z0-9]*'
re_comment = '{.*}'
tok = RegexpTokenizer(re_palavras_reservadas + '|' + re_simbolos + '|' + re_num_id + '|' + re_comment)
print(tok.tokenize(raw))