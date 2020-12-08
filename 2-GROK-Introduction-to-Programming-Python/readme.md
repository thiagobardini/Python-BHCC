![Image of Yaktocat](https://github.com/thiagobardini/Python-BHCC/blob/master/Imagem/pythonlogo.gif)
![Image of Yaktocat](https://github.com/thiagobardini/Python-BHCC/blob/master/Imagem/grokleanringlogo.png)

<hr>

### Emojis means: 
- :round_pushpin: - Main commands used in this module  
- :checkered_flag: - **CHALLENGE** -> my solution for the problem.
- :shipit: - GROK solution
- :bangbang: - Watch out!
- :mag: - Tips!
- :earth_americas: - Portuguese translation

 <hr>
 
# 3 - Files

## :round_pushpin: Commands Used: 
- 3.1 - Opening and looping over files
   - `open('text.txt')` **Open file**
   - `.read()` or `r` -> **Read** the entire contents of a file.
   - `''.strip()` -> **Strip** elimina as linhas em branco do loop. [Explanation](https://github.com/thiagobardini/Python-BHCC/blob/master/2-GROK-Introduction-to-Programming-Python/3%20–%20Files.md#mag-example-sem-usar-strip-resulta-em-um-output-com-linhas-veja-abaixo-o-exemplo-)
   - `.upper()` -> **Uppercase**
   - `end=""`-> [Explanation](https://github.com/thiagobardini/Python-BHCC/blob/master/2-GROK-Introduction-to-Programming-Python/3%20–%20Files.md#mag-comando-end)
- 3.2 - Writing files   
   - `.write()` or `w`-> **Write**
   
   - `\n` **new line** [Explanation](https://github.com/thiagobardini/Python-BHCC/blob/master/2-GROK-Introduction-to-Programming-Python/3%20–%20Files.md#n-newline---criando-novas-linhas-para-cada-print)
   - `file` -> pode ser usando como `\n` nova linha especificando o arquivo.  Ou usando direto no print de saída, sem a necessidade de repetir. [Explanation](https://github.com/thiagobardini/Python-BHCC/blob/master/2-GROK-Introduction-to-Programming-Python/3%20–%20Files.md#filef---pode-ser-usando-como-n-nova-linha-especificando-o-arquivo)
   - `sep=''` -> The separator between the arguments to print().[Explanation](https://github.com/thiagobardini/Python-BHCC/blob/master/2-GROK-Introduction-to-Programming-Python/3%20–%20Files.md#sep---the-separator-between-the-arguments-to-print)
   
   -  `.close()` ->  Closes the opened file. [Explanation](https://github.com/thiagobardini/Python-BHCC/blob/master/2-GROK-Introduction-to-Programming-Python/3%20–%20Files.md#close----closes-the-opened-file-a-closed-file-cannot-be-read-or-written-any-more-any-operation-which-requires-that-the-file-be-opened-will-raise-a-valueerror-after-the-file-has-been-closed-calling-close-more-than-once-is-allowed)
   
   - `with` -> comando `with` usado para abir o arquivo, deixando o codigo mais limpo, e sem a necessidade de usar o .close(). [Explanation](https://github.com/thiagobardini/Python-BHCC/blob/master/2-GROK-Introduction-to-Programming-Python/3%20–%20Files.md#with---comando-with-usado-para-abir-o-arquivo-deixando-o-codigo-mais-limpo-e-sem-a-necessidade-de-usar-o-close)	
   
   - `.startswith("")` -> method returns a **boolean (true or false)**. 

   - `.replace("oldtxt", "newtxt")`-> method **replaces** a specified phrase with another specified phrase. [Explanation](https://github.com/thiagobardini/Python-BHCC/blob/master/2-GROK-Introduction-to-Programming-Python/3%20%E2%80%93%20Files.md#replaceexamplenewexample--method-returns-a-boolean-true-or-false)

   - `if not`->  The 'not' is a Logical operator in Python that will return True if the expression is False. 
   
<hr>

### Directories and paths
There are two kinds of paths: absolute paths and relative paths.
 - **Relative path -> ../../data.txt**
    - Goes up two levels (to the grandparent directory) to find data.txt
  
 - **Absolute paths ->  e.g. /usr/bin/python3.3**
    - Starts from a fixed (or absolute) location on disk called the root (which on Windows is the drive name, like C:).

<hr>

## 3.1 - Opening and looping over files


  ### 3.1.1 - Opening files

- `open('text.txt')`

File name: **test.txt:**
```
eins
zwei
drei
```
Input:
```python
f = open('test.txt')
print(f)
```
Output:
```
<_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
```
_This angle bracket representation is used for types in Python that it doesn't make sense to print (like the whole contents of the file). But it lets you know that you successfully opened the file.)_

### 3.1.2 - Reading files

- `open('text.txt').read()` -> **read** the entire contents of a file

File name: **haiku.txt:**
```
Whitecaps on the bay:
A broken signboard banging
In the April wind.
- Richard Wright
```

Input:
```python
f = open('haiku.txt').read()
print("===")
print(f)
print("===")
# print a snippet of the file, from character 15 to 35
print("Now print just a slice:")
print(f[15:35])
```
Output
```
===
Whitecaps on the bay:
A broken signboard banging
In the April wind.
- Richard Wright
===
Now print just a slice:
e bay:
A broken sign
```
> :bulb: It is important to note that the read method reads the entire contents of the file into memory.

### 3.1.3 - Looping over files

File name: **words.txt:**
```
eins
zwei
drei
```
- **Solution #1** - Input:
```python
f = open('words.txt')
for line in f:
  print(line.strip())
```
- **Solution #2** - Input:
```python
for line in open('words.txt'):
  print(line.strip())
```
- **Solution #3** - Input:
```python
with open('words.txt') as f:
  for line in f:
    print(line.strip())
```
- **Same output for the solutions above** - Output: 
```
eins
zwei
drei
```

### :mag: Exemplo usando _.STRIP()_ resulta emm um output com linhas, veja abaixo:
```python
for line in open('words.txt'):
  print(line) #without strip command
```
Output:
```
eins
             <-- lines
zwei
             <-- lines
drei
             <-- lines
```

<hr>

## :checkered_flag: - **CHALLENGE**. 

### 3.1.4 - SHOUT your orders!

<p>The kitchen in any café is a noisy place. To make sure the orders which you have carefully written down on your notepad make it to the chef, you'll need to shout them! Write a program to read in lines of input from the file called orders.txt, and print out each line in <b>uppercase</b>.</p>

<p> :earth_americas:  A cozinha de qualquer café é um lugar barulhento. Para garantir que os pedidos que você anotou cuidadosamente em seu bloco de notas cheguem ao chef, você precisará gritá-los! Escreva um programa para ler as linhas de entrada do arquivo orders.txt e <b>imprima cada linha em maiúsculas</b>. </p>

<br>

- File name:  **orders.txt**:
```
Tomato and cheese melt
Pumpkin soup
Chicken and avocado sandwich
```
- :checkered_flag: INPUT: **MY CHALLENGE** -> my solution for the problem:
```python
newfile = 'orders.txt'
file = open( newfile , 'r' )
x = file.read()
print(x.upper(), end = '')
```
- :shipit: INPUT - GROK solution #1:
```python
for line in open('orders.txt'):
  print(line.strip().upper())
```

- Output:
```
TOMATO AND CHEESE MELT
PUMPKIN SOUP
CHICKEN AND AVOCADO SANDWICH
```
 <hr>
 
 ## :mag: Comando end=""
<p>Parâmetro final do Python em print () </p>
Por padrão, a função print () do python termina com uma nova linha. ... A função print () do Python vem com um parâmetro chamado **'end'**. Por padrão, o valor desse parâmetro é '\ n', ou seja, o novo caractere de linha. Você pode finalizar uma declaração de impressão com qualquer caractere / sequência usando este parâmetro.
 
Input:
```python
print('tudo bem', end=' ')
print('tudo')
print('hello')
```
Output:
```
tudo bem tudo #Junta a funcão, ou termina na mesma linha.
hello
```
<hr>

## 3.2 - Writing files


### 3.2.1 Writing files

- `.write()` or `w`
- `.close()`

Input:
```python
f = open('output.txt', 'w')
f.write("Hello, world!")
f.write("Now we're working with files!")
f.close()
```
_Nesse exemplo o OUTPUT será direto no meu arquivo "output.txt"_

Output: _output.txt_
```
Hello, world!Now we're working with files!
```
:bangbang: _Note that the two lines of output were actually written on one line!_
<p>This is because the .write() method on a file object does not add any newline characters.</p>

#### `\n` **newline** -> criando novas linhas para cada print()

Input:
```python
f = open('output.txt', 'w')
f.write("Hello, world!\n") #new line
f.write("Now we're working with files!\n") #new line
f.close()
```
_Nesse exemplo o OUTPUT será direto no meu arquivo "output.txt"_

Output: _output.txt_ (`\n` **newline** )
```
Hello, world!
Now we're working with files!
```

### 3.2.2 Writing to files using print

#### `file=f` -> pode ser usando como `\n` nova linha especificando o arquivo.
Ou invés de criar uma nova linha `\n` em cada linha, é possível usar apenas uma vez só vez o comando `file='text`usando no  print de saida.

Input: usando como `\n` nova linha especificando o arquivo.
```
f = open('output.txt', 'w')
print("Hello, world!", file=f)
print("Now we're working with files!", file=f)
f.close()
```
Output: _output.txt_ (`file` criou nova linha para each print )
```
Hello, world!
Now we're working with files!
```

Input: Usar apenas uma vez só vez o comando `file='text`usando no  print de saida.
```python
sounds = {'dog': 'a barker', 'cat': 'a meower', 'bird': 'a tweeter'}
f = open('output.txt', 'w')
for animal in sorted(sounds):
  sound = sounds[animal]
  print('A', animal, 'is', sound, sep='--', file=f)
f.close()
```

Output: _output.txt_ 
```
A--bird--is--a tweeter
A--cat--is--a meower
A--dog--is--a barker
```
<hr>

#### `sep=''` -> The separator between the arguments to print(). 
This file keyword argument works in conjunction with the other keyword arguments we've seen print take, such as sep. 

Input:
```python
#for formatting a date 
print('09','12','2016', sep='-') 
```
Output:
```
09-12-2016
```

<hr>

### 3.2.3 - Closing files after writing to them

#### `.close()` ->  Closes the opened file. A closed file cannot be read or written any more. Any operation, which requires that the file be opened will raise a ValueError after the file has been closed. Calling close() more than once is allowed.

#### `with` -> comando `with` usado para abir o arquivo, deixando o codigo mais limpo, e sem a necessidade de usar o `.close()`.

```python
sounds = {'dog': 'a barker', 'cat': 'a meower', 'bird': 'a tweeter'}

with open('output.txt', 'w') as f:
  for animal in sorted(sounds):
    sound = sounds[animal]
    print('A', animal, 'is', sound, sep='--', file=f)
```
> Notice that unlike the first two implementations, there is no need to call file.close() when using with statement. 

Output: _output.txt_ 
```
A--bird--is--a tweeter
A--cat--is--a meower
A--dog--is--a barker
```
<hr>

## :checkered_flag: - **CHALLENGE**. 

### 3.2.4 - The dog wrote it!

<p>You were working hard writing a letter to your penpal, only to realise that your dog has been "helping" and contributing to the letter too! You notice that every few lines starts with WOOF! and includes things you simply didn't write!</p>
<p>Write a program to read in lines from the file letter.txt and write out a new file, fixed.txt, which contains the only lines that do not start with WOOF!.</p>

<p>:earth_americas: Você estava trabalhando duro escrevendo uma carta para o seu correspondência, apenas para perceber que seu cão estava "ajudando" e contribuindo para a carta também! Você percebe que todas as linhas começam com WOOF! e inclui coisas que você simplesmente não escreveu!</p>
<p>Escreva um programa para ler as linhas do arquivo letter.txt e escreva um novo arquivo, fixed.txt, que contém as únicas linhas que não iniciam com o WOOF !</p>

<br>

- File name:  **orders.txt**:
```
My vegetable garden is growing really well!
WOOF! Let's play catch!
The tomatoes and cucumbers are nearly ready to eat.
How is your garden going?
WOOF! I better chase that possum!
```

- OUTPUT -> Your program should create the file fixed.txt that contains:
```
My vegetable garden is growing really well!
The tomatoes and cucumbers are nearly ready to eat.
How is your garden going?
```

- :checkered_flag: INPUT: **MY CHALLENGE** -> my solution for the problem:
```python
file = open("letter.txt", 'r')
file_out = open("fixed.txt", 'w')
for line in file:
  if line.startswith("WOOF! "):
      line.replace("WOOF! ","")
  else:
    print(line.strip(), file=file_out)
```
- :shipit: INPUT - GROK solution #1:
```python
f = open('fixed.txt', 'w')
for line in open('letter.txt'):
  if not line.startswith('WOOF!'):
    f.write(line)
f.close()
```

- :shipit: INPUT - GROK solution #2:
```python
with open('letter.txt') as fin, open('fixed.txt', 'w') as fout:
  for line in fin:
    if not line.startswith('WOOF!'):
      fout.write(line)
```

- Output: fixed.txt
```
My vegetable garden is growing really well!
The tomatoes and cucumbers are nearly ready to eat.
How is your garden going?
```

<hr>

### :round_pushpin: EXTRA

#### `.startswith("")` ->  method returns a **boolean (true or false)**. 

<hr>

#### `.replace("example","newexample")`-> method **replaces** a specified phrase with another specified phrase.
 - It returns True if the string starts with the specified prefix. 
 - It returns False if the string doesn't start with the specified prefix.
 
Input:   
```python
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)
```
Output:
```
I like apples
```
<hr>

#### `if not`-> The 'not' is a Logical operator in Python that will return True if the expression is False. The 'not' operator is used in the if statements. 
      - For example: if not x. If x is True, then not will evaluate as false, otherwise, True


<hr>

## :checkered_flag: - **CHALLENGE**. 

### 3.2 - Words in a file: color or colour?

<p>You're reading a book by an unfamiliar author and are curious about which country they might be from. You decide to write a program to help you guess this based on the spelling of the words in the book.</p>

<p>Write a program that reads in a word (e.g. colour or color) and checks if it occurs in the file book.txt, printing out `**word** was found in the book`. or `**word** was not found in the book`.</p>
 
 :earth_americas: Você está lendo um livro de um autor desconhecido e está curioso sobre de que país eles podem ser. Você decide escrever um programa para ajudá-lo a adivinhar isso com base na ortografia das palavras do livro.
 
 <p>Escreva um programa que leia uma palavra (por exemplo, cor ou cor) e verifique se ele ocorre no arquivo book.txt, imprimindo `**word** foi encontrado no livro`. ou `**word** não foi encontrado no livro...`</p>
 
File name:  **book.txt**:
 ````
He looked out from the top of the mountain .
The colour of the sky was amazing .
Reds , oranges and pinks faded into a hazy blue.
 ````
 then your program should work like this:
 ````
 Word to look for: colour
colour was found in the book.
 ````
 - The provided input word will always be in lowercase, but your program should match in a case insensitive manner. For instance, given the following book.txt file:
 - Punctuation will always be provided as a separate word, so you don't have to do anything special to account for it.
 
 - :earth_americas: A palavra de entrada fornecida sempre estará em letras minúsculas, mas seu programa deve corresponder de maneira que não diferencia maiúsculas de minúsculas. Por exemplo, dado o seguinte arquivo book.txt:
 - :earth_americas: A pontuação sempre será fornecida como uma palavra separada, para que você não precise fazer nada de especial para justificá-la.
 
- :checkered_flag: INPUT: **MY CHALLENGE** -> my solution for the problem:
```python
word = input("Word to look for: ")
w = False

with open('book.txt','r') as file:
  for line in file:
    if word in line.lower():
      print(word + " was found in the book.")
      w = True
      break
if w == False:
  print(word + " was not found in the book.")
```
- :shipit: INPUT - GROK solution #1:
```python
word = input('Word to look for: ')
found = False
for line in open('book.txt'):
  line = line.lower()
  if word in line.split():
    found = True
if found:
  print(word, "was found in the book.")
else:
  print(word, "was not found in the book.")
```
- :shipit: INPUT - GROK solution #2:
```python
word = input('Word to look for: ')
if word in open('book.txt').read().lower().split():
  print(word, "was found in the book.")
else:
  print(word, "was not found in the book.")
```
 
 
 
 ## :checkered_flag: - **CHALLENGE**. 

### 3.3 - Waiter! There's an aardvark in my file!
 
<p>There are aardvarks on the loose! We need you to check whether there are any aardvarks hidden in a text file.</p>

<p>To start, your program should read in a file input.txt, one line at a time, numbering the lines from 1. You should check each line to see whether the letters in the line can be used to make the word "aardvark". Uppercase letters can be used as well. So, if the file input.txt contains this:</p>

<p> :earth_americas: Existem Aardvarks à solta! Precisamos que você verifique se há algum Aardvarks oculto em um arquivo de texto. </p>

<p> :earth_americas: Para iniciar, seu programa deve ler um arquivo input.txt, uma linha de cada vez, numerando as linhas de 1. Você deve verificar cada linha para ver se as letras da linha podem ser usadas para formar a palavra " aardvark ". Letras maiúsculas também podem ser usadas. Portanto, se o arquivo input.txt contiver isso: </p>

- File name:  **input.txt**:
```
No aardv*rks here!
Only armadillos and anteaters.
Animals are run down: very awful road kill.
I prefer a quick guacamole made from avocados.
```
- Output: then your program should work like this:
 ```
Aardvark on line 3
Aardvark on line 4
```
- :checkered_flag: INPUT: **MY CHALLENGE** -> my solution for the problem:
````python
li = 0
for line in open('input.txt'):
  li += 1
  line = line.lower()
  if line.count('a') >= 3 and line.count('r') >= 2 and line.count('d') >=1 and line.count('k') >= 1:
    print('Aardvark on line', li)
````

- :shipit: INPUT - GROK solution #1:
```python
for n, line in enumerate(open('input.txt')):
  letters = list('aardvark')
  for c in line.lower():
    if c in letters:
      letters.remove(c)
  if not letters:
    print('Aardvark on line', n + 1)
```
- :shipit: INPUT - GROK solution #2:
```python
linenum = 0
for line in open('input.txt'):
  linenum += 1
  line = line.lower()
  if line.count('a') >= 3 and line.count('r') >= 2 and line.count('d') >= 1 and line.count('v') >= 1 and line.count('k') >= 1:
    print('Aardvark on line', linenum)
```
- :shipit: INPUT - GROK solution #3:
```python
from collections import Counter

target = Counter('aardvark')
for i, line in enumerate(open('input.txt')):
  current = Counter(line.lower())
  for c in target:
    if current[c] < target[c]:
      break
  else:
    print('Aardvark on line', i + 1)
```    














