import re
from nltk.tokenizer import RegexpTokenizer

raw = "program	lalg;\n{teste}\nvar a: integer;\nbegin\na := 42\nread(a, @, 1)\nend."

tok = RegexpTokenizer('')