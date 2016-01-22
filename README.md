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

### Class 1
1. [Scratch](#scratch)
2. [Setting up python](setting-up-python-and-package-managers)
	- [Linux, Unix or Mac OSX](#nix-operating-systems-such-as-linux-unix-mac-osx)
	- [Windows](#windows)
3. [Homework](#homework)
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

#### Homework

1. For homework this class, create a scratch project that involves at least three different control blocks, two motion blocks, two event blocks, and two operators blocks.
2. Set up python on your machine

### Class 2

1. [Reading](#reading)
2. [Variables, input and output](#variables-and-input-and-output)
	- [Variables](#variables)
	- [Input and output](#input and output)
3. [Homework](#homework)

#### Reading

To be familar with the upcoming section, skim through [this basic syntax](http://www.tutorialspoint.com/python/python_basic_syntax.htm).

Read through [this variable types](http://www.tutorialspoint.com/python/python_variable_types.htm).

Skim through [this basic operations](http://www.tutorialspoint.com/python/python_basic_operators.htm).

Read through [this on decision making](http://www.tutorialspoint.com/python/python_decision_making.htm) carefully.

When we say carefully, we really mean, try to really understand, the better you understand what is going on, the better you will code, and the less you will debug later.

Optional:
[Math and numbers](http://www.tutorialspoint.com/python/python_numbers.htm)
[Strings](http://www.tutorialspoint.com/python/python_strings.htm)

#### variables and input and output

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

You may want to read [this](http://www.python-course.eu/input.php) before you continue.

#### Homework



### Class 3
#### Reading
Read through [this on loops](http://www.tutorialspoint.com/python/python_loops.htm) carefully as well.
Skim through [this on Lists](http://www.tutorialspoint.com/python/python_lists.htm).
Skim through [this on tuples](http://www.tutorialspoint.com/python/python_tuples.htm).
Skim through [this on python dictionaries](http://www.tutorialspoint.com/python/python_dictionary.htm)
#### if logic
#### loops
##### Homework

###### Names and ages

Get 10 names and their assoceated ages from the user, print to the screen: the oldest persion and their age.

###### Hashtag triangle

Get a height from the user and print a triangle (using hashtags) to the screen using that height as the number of hashtags on the bottom row. 

For example if the user enters: 3, the output should be:

   #
  ##
 ###
 
If the user enters 5, the output should be:
     #
	##
   ###
  ####
 #####
 
and so on.

You may want to print the triangle the other way first, such as:

 #
 ##
 ###
 ####
 #####
 
 would be for an input of 5. The challenge is doing it the first way, but doing it this way first may make it easier.
 
### Class 4

1. [Reading](#reading)
2. [Loops](#loops)
3. [Functions](#functions)
4. [Homework](#Homework)
	- [FizzBuzz](#fizzbuzz)

#### Reading

Read through [this on functions](http://www.tutorialspoint.com/python/python_functions.htm) carefully. This is a very important concept in programming that will really save you a lot of time.

Skim through [this on modules](http://www.tutorialspoint.com/python/python_modules.htm)

Read the first answer [on the modulo operator here](http://stackoverflow.com/questions/4432208/how-does-work-in-python) and the syntax in python.

#### Loops
#### Functions 
#### Homework

##### FizzBuzz

Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

It will be useful to understand the modulo operator, if statements, and looping.

### Class 5
#### Reading

Skim through [this on exceptions](http://www.tutorialspoint.com/python/python_exceptions.htm)
Read through [wiki on tower of hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) as we will be using it a lot this class.

#### tower of hanoi

### Class 6

1. [Reading](#reading)
2. [Fifteen](#fifteen)
3. [Minesweeper](#minesweeper)

#### Reading
Play [this](http://migo.sixbit.org/puzzles/fifteen/) game, and get ready to build it.
Read up on [this](https://en.wikipedia.org/wiki/Microsoft_Minesweeper) classic game, get ready to build a similar version as well.

#### Fifteen

#### Minesweeper

### Class 7

1. [Reading](#reading)
2. [Sorting](#sorting)
	- [Bubble Sort](#bubble-sort)
	- [Merge Sort](#merge-sort)
	- [Insertion sort](#insertion-sort)
	
#### Reading
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

### Class 8
1. [Reading](#reading)

#### Reading

###### Data Structures reading
You may want to go back and get a better understanding of [Lists](http://www.tutorialspoint.com/python/python_lists.htm),
[tuples](http://www.tutorialspoint.com/python/python_tuples.htm), [dictionaries](http://www.tutorialspoint.com/python/python_dictionary.htm) in python.

Furthermore, you should skim through [Linked Lists](https://en.wikipedia.org/wiki/Linked_list) and take a look at some of the data structures [here](https://en.wikipedia.org/wiki/List_of_data_structures)(some are less important than others). In general the most important ones are [arrays](https://en.wikipedia.org/wiki/Array_programming) (in python lists), [hashtables](https://en.wikipedia.org/wiki/Hash_table) (in python dictionaries), [tuples](https://en.wikipedia.org/wiki/Tuple), [linked lists](https://en.wikipedia.org/wiki/Linked_list), [trees](https://en.wikipedia.org/wiki/Tree_(data_structure)) (we will cover in class 9), [Graphs](<https://en.wikipedia.org/wiki/Graph_(abstract_data_type)>), [Stacks](<https://en.wikipedia.org/wiki/Stack_(abstract_data_type)>) (Cover in class 10 in sudoku), and [Heaps](<https://en.wikipedia.org/wiki/Heap_(data_structure)>).

###### Reading on classes

#### Data Structures

#### Intro to classes
### Class 9
####  classes continued
### Class 10
#### Final Project
#### Alternate class on backtracking