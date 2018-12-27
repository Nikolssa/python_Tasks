from collections import Counter

text = "Python is an interpreted high-level programming language for general-purpose programming. " \
       "Created by Guido van Rossum and first released in 1991," \
       "Python has a design philosophy that emphasizes code readability, notably" \
       "using significant whitespace. It provides constructs that enable clear programming " \
       "on both small and large scales. In July 2018, the creator Guido Rossum" \
       "stepped down as the leader in the language community after 30 years." \
       "Python features a dynamic type system and automatic memory management. " \
       "It supports multiple programming paradigms, including object-oriented, " \
       "imperative, functional and procedural, and has a large and comprehensive standard library." \
       "Python interpreters are available for many operating systems. " \
       "CPython, the reference implementation of Python, is open " \
       "source software and has a community-based development model, " \
       "as do nearly all of Python's other implementations." \
       "Python and CPython are managed by the non-profit Python Software Foundation."

chars = []
for char in text:
       chars.append(char)


splittedText = text.split()
item = "Python"
count = 0
for word in splittedText:
       if item in word:
              count+=1

print("The word \"Python\" is repeated {count} times inside the text".format(count=count))


cnt = Counter(chars)
mostFrqLetter = cnt.most_common(2)
for k, v in mostFrqLetter:
       if k == " ":
              continue
       else:
              print("Most frequent letter in text is: \"{key}\", repeated => {val} times.".format(key=k, val=v))