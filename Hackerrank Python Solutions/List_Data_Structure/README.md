Problem Statement
==================

When we talk about storing multiple values in a container-like data-structure, the first thing that comes to mind is a list.

You can initialize a list as

> arr = list() <br \>
or simply <br \>
> arr = [] <br \>
or with a few elements as <br \>

> arr = [1,2,3] <br \>
Elements can be accessed easily like you do in most programming languages. <br \>

>print arr[0] <br \>
1 <br \>
> print arr[0] + arr[1] + arr[2] <br \>
6 <br \>
Lists in python are very versatile. If you ask what you can add in a Python List, the answer is practically anything!

In python you can create a list of any object, be it string, integers, or even lists. You can even add multiple types in a single list! Isn't that exciting?

Let's look at some of the methods you can use on List.

####append(x) Adds a single element 'x' to the end of list.

arr.append(9) print arr [1, 2, 3, 9]

####extend(L) 
Merges another list 'L' to the end.

arr.extend([10,11]) print arr [1, 2, 3, 9, 10, 11]

####insert (i,x) 
Inserts element 'x' at position 'i'.

arr.insert(3,7) print arr [1, 2, 3, 7, 9, 10, 11]

####remove(x) 
Removes the first occurrence of element x.

arr.remove(10) 
arr 
[1, 2, 3, 7, 9, 11]

####pop() 
Removes the last element of list. If an argument is passed, that index item is popped out.

temp = arr.pop() print temp 11

####index(x) 
Returns the first index of a value in the list. Throws error if it's not found.

temp = arr.index(3) print temp 2

####count(x) 
Counts the number of occurrences of an element x.

temp = arr.count(1) print temp 1

####sort() 
Sorts the list.

arr.sort() print arr [1, 2, 3, 7, 9]

####reverse() 
Reverses the list.

arr.reverse() print arr [9, 7, 3, 2, 1]

###Task 
You have to initialize your list L = [] and follow the N commands given in N lines.

Commands will be 1 of the 8 commands as given above, other than extend, and each command will have its value separated by space.

Follow this example

###Sample Input

12 <br \>
insert 0 5  <br \>
insert 1 10 <br \>
insert 0 6 <br \>
print  <br \>
remove 6 <br \>
append 9 <br \>
append 1 <br \>
sort  <br \>
print <br \>
pop <br \>
reverse <br \>
print <br \>
###Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
