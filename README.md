# python class


Will be used for sharing code and learning python


## An outline for the course

1. [Class 1 ( Scratch and setting up python )](#class-1)
2. [Class 2 ( variables, input and output )](#class-2)
3. [Class 3 ( if logic and loops )](#class-3)
4. [Class 4 ( loops/functions and FizzBuzz )](#class-4)
5. [Class 5 ( tower of hanoi )](#class-5)
6. [Class 6](#class-6)
	* [Fifteen](#fifteen)
	* [Minesweeper](#minesweeper)
7. [Class 7 ( sorting )](#class-7)
8. [Class 8 ( data structures and intro to classes )](#class-8)
9. [Class 9 ( classes continued )](#class-9)
10. [Class 10](#class-10)
	* [Final Project](#final-project)
	* [Alternate class on backtracking](#alternate-class-on-backtracking)
11. [Python References](#python-references)
12. [Text editors](#text-editors)

### Class 1
1. [Scratch](#scratch)
2. [Setting up python](setting-up-python-and-package-managers)
	- [Linux, Unix or Mac OSX](#nix-operating-systems-such-as-linux-unix-mac-osx)
	- [Windows](#windows)
3. [Homework](#homework-class-1)
4. [Text editor](#text-editor)
5. [First program](#first-program)

#### Scratch 
To start getting our heads to think more programmatically, we will start with scratch, a free software built to learn the ideas behind coding from the great people at MIT. linked [here](https://scratch.mit.edu/).

To start, I would advise you to create a project and play around.

If you get stuck, MIT put out a couple tutorial videos [here](https://scratch.mit.edu/help/videos/#)

While playing around, it is advised to use blocks from the control section, this will help you create more powerful animations.

#### Setting up python and package managers

For all systems this [tutorial](http://www.tutorialspoint.com/python/python_environment.htm) should come in handy if you get stuck.

##### *nix operating systems such as linux, unix, mac osx
Before you start, you may want to read up on a bash primer, or just learn the basic commands.

here is a [bash reference](http://ss64.com/bash/). Of course you do not have to know all of them, but some of them you will use more then others, such as: cd, ls, mkdir, find.

Python usually comes installed on these operating systems. To check, open your applications and search for terminal. Once it is opened type

```sh
python --version
```
You should see something like: 2.7.11

If not, you can download python [here](https://www.python.org/downloads/)


Google has put out a setup page for python also, linked [here](https://developers.google.com/edu/python/set-up?hl=en)

For mac, a great package manager to have is [homebrew](http://brew.sh/), download and instalation is advised.
##### Windows
Before you start, we will be using the command line, so reading up on a command line [reference](http://ss64.com/nt/) is advised. You don't need to learn all the commands, just some of the more useful ones (such as cd, dir, find, help, md, move, path)

You can test to see if python is install on your machine opening the cmd application and typing: python --version 

if you dont get back a version such as: 2.7.11, then you need to download and install it [here](https://www.python.org/downloads/)


Google has put out a setup page for python also, linked [here](https://developers.google.com/edu/python/set-up?hl=en)

##### Text editor

A text editor is a program that will allow a user to edit text. When you program, you will usually want to use a text editor with a certain text format. For example, when you use microsoft word, the document ends with .doc, you might have seen .pdf, .jpg, .gif or various others, for python we use .py. 

Sublime text is a great editor that uses colors and auto complete to make coding easier for the user and better overall experience. You can download it [here](http://www.sublimetext.com/).

##### First program

After you download sublime (or you can use any text editor) open a new file and save it as: helloworld.py in the documents

On the first line write:

```python
print("Hello World!")
```

Save the file and open your terminal/command line. Using your appropriate commands (for windows and *unix use: cd ),
change into the directory where your file is saved. 

This: 

```sh
cd documents 
```

Should work, but you might need to use ls/dir to help find the documents folder. Once you changed into the documents directory write:

```sh
python helloworld.py
```

Which if you have done everything correctly, should write to the screen: Hello World!

#### Homework Class 1

1. For homework this class, create a scratch project that involves at least three different control blocks, two motion blocks, two event blocks, and two operators blocks.
2. Set up python on your machine

### Class 2

1. [Reading](#reading-class-2)
2. [Basics of programming](#basics-of-programming)
	- [Variables](#variables)
	- [Input and output](#input and output)
	- [If statements](#if-statements)
3. [Homework](#homework-class-2)

#### Reading Class 2

To be familar with the upcoming section, skim through [this on basic syntax](http://www.tutorialspoint.com/python/python_basic_syntax.htm).

Read through [this on variable types](http://www.tutorialspoint.com/python/python_variable_types.htm).

Skim through [this on basic operations](http://www.tutorialspoint.com/python/python_basic_operators.htm).

Read through [this on decision making](http://www.tutorialspoint.com/python/python_decision_making.htm) carefully.

When we say carefully, we really mean, try to really understand, the better you understand what is going on, the better you will code, and the less you will debug later.

Optional:
[Math and numbers](http://www.tutorialspoint.com/python/python_numbers.htm)
[Strings](http://www.tutorialspoint.com/python/python_strings.htm)
[Boolean Logic](http://www.i-programmer.info/babbages-bag/235-logic-logic-everything-is-logic.html)

#### Basics of programming

##### variables
In python you can create a variable easily as long as you don't name it one of the keywords. You can read about them [here](http://zetcode.com/lang/python/keywords/).

If you wanted to put a mathematical expression or a sentence or a mixed list you would do it like this:

```python
x = 5 + 12 + 24 + 36
sentence = "I love coding in python"
mixedList = [5 + 23, 0, "Coding is fun", 10.5, "Hello world!"]
```

To play around with this, open the interpreter (by typing python in your terminal/command line or using an online one [here](https://www.pythonanywhere.com/try-ipython/)) and try it out.

##### input and output

If we want to output what the user just gave us, we use 'print', it does not matter about the internals here at this point, for our sake lets use it as a function like so:

```python
print("Hello World")
```

You may want to skim through [this](http://www.python-course.eu/input.php) before you continue.

Input in python is simple but is different depending on your version. If you are using python 2.7 or less than you want to use raw_input() if your using python 3 or above, you want to use input(). In the class folder there is a helpFunctions.py file, you can read through it if you'd like. To get the users name:

```python
from helperFunctions import *
name = getString("Please enter a name")
```
and to print it

```python
print(name)
```

or

```python
print("Hello " + name)
```

##### If statements
If statements are a logical way to make decisions based on unknown input. We use if statements in our lives all the time. For example, we say "if I am late, leave without me", "If I don't catch the bus, I'll take a cab". 

In programming we use if statements as a form of controlling the flow of the program. The sytanx is pretty straightforward, you can read about it [here](https://docs.python.org/2/tutorial/controlflow.html), only the first section is necessary.

The syntax, taken from the docs:

```python
if x < 0:
	x = 0
	print 'Negative changed to zero'
elif x == 0: #else if
	print 'Zero'
elif x == 1: #else if
	print 'Single'
else:
	print 'More'
```

the if statement checks if x is less than zero, if it is it will set x to zero and print: 'Negative changed to zero', if it is not and if (else if) x is zero then print: 'Zero', if it is not and if x is 1, print: 'Single', else in all other cases, print: 'More'

#### Homework Class 2

Now that you know how to get input from the user, you will do some logic on the users input.

You will do something like this

```
get name from user
if initial of first name is between 'a' and 'm'
	print("your first name starts at the beginning of the alphabet")
else
	print("Your first initial starts at the end of the alphabet")
```

You may use the helperfunctions file. There you can find the functions between(charA, charB) use like:

```python
'c' in between('a','d') # True
'C' in between('a','d') # True even though it is capitalized
'f' in between('a','d') # False
```

[This](#http://www.tutorialspoint.com/python/python_if_else.htm) reading from the reading section may come in handy.

### Class 3

1. [Reading](#reading-class-3)
2. [Loops](#loops)
3. [Homework](#homework-class-3)
	- [Names and ages](#names-and-ages)
	- [Hashtag triangle](#hashtag-triangle)
	
#### Reading Class 3
Read through [this on loops](http://www.tutorialspoint.com/python/python_loops.htm) carefully as well.
Skim through [this on Lists](http://www.tutorialspoint.com/python/python_lists.htm).
Skim through [this on tuples](http://www.tutorialspoint.com/python/python_tuples.htm).
Skim through [this on python dictionaries](http://www.tutorialspoint.com/python/python_dictionary.htm)
Skim through [Control Flow Python](https://docs.python.org/2/tutorial/controlflow.html), as a general rule on this particular page, the closer the section is to the top of the page, the more important it is at this moment.

#### loops

#### Homework Class 3

##### Names and ages

Get 10 names and their assoceated ages from the user, print to the screen: the oldest persion and their age.

##### Hashtag triangle

Get a height from the user and print a triangle (using hashtags) to the screen using that height as the number of hashtags on the bottom row. 

For example if the user enters: 3, the output should be:
<pre>
   #
  ##
 ###
</pre>
 
If the user enters 5, the output should be:
<pre>
     #
	##
   ###
  ####
 #####
</pre>
and so on.

You may want to print the triangle the other way first, such as:
<pre>
 #
 ##
 ###
 ####
 #####
</pre>
 would be for an output for 5. The challenge is doing it the first way, but doing it this way first may make it easier.
 
### Class 4

1. [Reading](#reading-class-4)
2. [Loops](#loops)
3. [Functions](#functions)
4. [Homework](#Homework-class-4)
	- [FizzBuzz](#fizzbuzz)
	- [Caesar Cipher](#caesar-cipher)
		- [Encription](#encription)
		- [Decription](#decription)

#### Reading Class 4

Read through [this on functions](http://www.tutorialspoint.com/python/python_functions.htm) carefully. This is a very important concept in programming that will really save you a lot of time.

Skim through [this on modules](http://www.tutorialspoint.com/python/python_modules.htm)

Read the first answer [on the modulo operator here](http://stackoverflow.com/questions/4432208/how-does-work-in-python) and the syntax in python.

#### Loops
#### Functions 
#### Homework Class 4

##### FizzBuzz

Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

It will be useful to understand the modulo operator, if statements, and looping.

##### Caesar Cipher


For this homework we will write a program for the [caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher). 

###### Encription

In the cipher, you will increment each letter by fixed amount (with wrapping so that 'z' + 1 = 'a').

For example if the increment is 5 then 'abcde' becomes 'fghij', if the increment is 3 then 'wxyz' becomes 'zabc'

###### Decription

In this assignment you will print out all the possible values that our encripted value could be.

For example if our encripted code is 'a' then that code could have come from the entire alphabet.

'ab' could have come from 'ab','bc','cd','de', etc.

For a slightly harder problem, try implemt an algorithm that does not have to check every possibility. 

For example, if our encripted code is 'z lzm hr z gtlzm' then since we are dealing with the english language, we know that there are only a limited amount of one letter words, decreasing our possibilities to only handful.

### Class 5

1. [Reading](#reading-class-5)
2. [Recursion](#recursion)
3. [Homework](#homework-class-5)
	- [Tower of Hanoi](#tower-of-hanoi)
	- [Vigenere Cipher](#vigenere-cipher) 

#### Reading Class 5

Skim through [this on exceptions](http://www.tutorialspoint.com/python/python_exceptions.htm)
Read through [wiki on tower of hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) as we will be using it a lot this class.

#### Recursion

Recursion is the act of a function calling itself. A great example of this is the factorial function in mathematics.

In mathematics, n! (pronounced n factorial) is written as n * (n-1)! where 0! = 1! = 1, so 
5! = 5 * 4! = 5 * 4 * 3! = 5 * 4 * 3 * 2! = 5 * 4 * 3 * 2 * 1! = 5 * 4 * 2 * 1 = 120

When we write recursive functions, we usually have a base case of when we should stop, and we want to move towards that base case on every interation of the function.

If we wanted to write a function to compute a factorial, we would write:

```python
def factorial(n):
	if n == 1: # our base case
		return 1 # return 1 since 1! = 1
	else:
		return n * factorial(n - 1) # n! = n * (n-1)!
```

As we see here, we have a base case when we stop (when n = 1) and on each interation n gets closer to the base case, assuming the user enters a positive integer.

#### Homework Class 5

##### Tower of Hanoi

In the tower of hanoi there are three towers with N rings on the first one (in ascending order). The goal of the game is to move all the rings to the middle tower. The rules are simple, you may only move one ring at a time and a ring can only be placed on a ring that is larger than itself.

Open up the file for this class and play the game on your terminal/command line to get a feel for the game.

Then try to implement solve, an algorithm that will win the game automatically for you.

##### Vigenere Cipher

In this cipher our key is not a single number, but rather a word or series of numbers. The code is encripted with by cycling through each letter of the code and key at the same time, using a mini caesar cypher on each letter.

For example if our code is 'abc' and our key is '123' then 'a' gets shifted one place, 'b' two and 'c' three, so we get as an output 'bdf'. If our key is shorter than our code we just wrap around and start again. Again 'z' + 1 = 'a'.

Decripting this algorithm is a bit harder, but not impossible. This problem is a bit more advanced and uses frequency analysis and can be implemented with machine learning.

### Class 6

1. [Reading](#reading-class-6)
2. [Fifteen](#fifteen)
3. [Minesweeper](#minesweeper)
4. [Homework](#homework-class-6)

#### Reading Class 6
Play [this](http://migo.sixbit.org/puzzles/fifteen/) game, and get ready to build it.
Read up on [this](https://en.wikipedia.org/wiki/Microsoft_Minesweeper) classic game, get ready to build a similar version as well.

#### Fifteen

#### Minesweeper

#### Homework Class 6

### Class 7

1. [Reading](#reading-class-7)
2. [Sorting](#sorting)
	- [Bubble Sort](#bubble-sort)
	- [Merge Sort](#merge-sort)
	- [Insertion sort](#insertion-sort)
3. [Homework](#homework-class-7)
	
#### Reading Class 7
Read through these sorting alogrithms: 
	[bubblesort](https://en.wikipedia.org/wiki/Bubble_sort)
	[merge sort](https://en.wikipedia.org/wiki/Merge_sort)
	[insertion sort](https://en.wikipedia.org/wiki/Insertion_sort) and some others [here](https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms)

#### Sorting

##### Bubble sort
You can watch a clip [here](https://www.youtube.com/watch?v=Ui97-_n5xjo) explaining bubble sort.
##### Merge sort
You can watch a clip [here](https://www.youtube.com/watch?v=sWtYJv_YXbo) explaining Merge sort.
##### Insertion sort
You can watch a clip [here](https://www.youtube.com/watch?v=TwGb6ohsvUU) explaining Insertion sort.

#### Homework Class 7

### Class 8
1. [Reading](#reading-class-8)
	- [Data Structes](#data-structures-reading)
	- [Classes](#reading-on-classes)
2. [Data Structures](#data-structure)
3. [Intro to classes](#intro-to-classes)
4. [Homework](##homework-class-8)

#### Reading Class 8

###### Data Structures reading
You may want to go back and get a better understanding of [Lists](http://www.tutorialspoint.com/python/python_lists.htm),
[tuples](http://www.tutorialspoint.com/python/python_tuples.htm), [dictionaries](http://www.tutorialspoint.com/python/python_dictionary.htm) in python.

Furthermore, you should skim through [Linked Lists](https://en.wikipedia.org/wiki/Linked_list) and take a look at some of the data structures [here](https://en.wikipedia.org/wiki/List_of_data_structures) (some are less important than others). In general the most important ones are [arrays](https://en.wikipedia.org/wiki/Array_programming) (in python lists), [hashtables](https://en.wikipedia.org/wiki/Hash_table) (in python dictionaries), [tuples](https://en.wikipedia.org/wiki/Tuple), [linked lists](https://en.wikipedia.org/wiki/Linked_list), [trees](https://en.wikipedia.org/wiki/Tree_(data_structure)) (we will cover in class 9), [Graphs](<https://en.wikipedia.org/wiki/Graph_(abstract_data_type)>), [Stacks](<https://en.wikipedia.org/wiki/Stack_(abstract_data_type)>) (Cover in class 10 in sudoku), and [Heaps](<https://en.wikipedia.org/wiki/Heap_(data_structure)>).

###### Reading on classes

The readings here are more for you to skim, there will be more for next week, this is really a primer.
Classes overview: [tutorialspoint](http://www.tutorialspoint.com/python/python_classes_objects.htm) and [python-course](http://www.python-course.eu/python3_magic_methods.php)

magic methods: [rafekettler](http://www.rafekettler.com/magicmethods.html) or [python-course](http://www.python-course.eu/python3_magic_methods.php) works fine.

#### Data Structures

#### Intro to classes

#### Homework Class 8

### Class 9

1. [Reading](#reading-class-10)
2. [Classes Continued](#classes-continued)
3. [Homework](#homework-class-9)

#### Reading Class 9
#### Classes continued
#### Homework Class 9
### Class 10

1. [Reading](#reading-class-10)
2. [Final Project](#final-project)
3. [Sudoku](#sudoku)
4. [Homework](#homework-class-10)

#### Reading Class 10
#### Final Project
#### Sudoku
#### Homework Class 10

### Python References

- [Code Like a Pythonista: Idiomatic Python](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)
- [Python documentation 3.5.1](https://docs.python.org/3/)
- [Python documentation 2.7.11](https://docs.python.org/2.7/)
- [tutorialspoint](http://www.tutorialspoint.com/python/)
- [Free Python Books](https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md#python)

### Text editors and misc.

- [Sublime Text](http://www.sublimetext.com/)
- [Vim](http://www.vim.org/)
	- [Vim Tutorial](http://www.openvim.com/sandbox.html)
- [Markdown](https://daringfireball.net/projects/markdown/)
	- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)