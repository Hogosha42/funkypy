# FunkyPy - Python

A python module that allows for easier functional programming in python

Some of the things this module contains are:

- better funcion composition
- easier to use and clearer maps on lists
- prettier function chaining with pipe operator
- a bind function

---

## Piping

Functional programming is all about functions and passing data through them, python makes this looks kind of ugly. This module tries to solve this by a class called Data.

without this module it would look like the example below

```py
print(times2(add4(add2(4))))
# 20
```
with the package we can make it look like this:
```py
Data(4) >> add2 >> add4 >> times2 >> print
# 20

### line breaks do have an effect on the expression but you can mitigate this by parentheses

(Data(4)
>> add2
>> add4
>> times2
>> print)
# 20
```

## Bind

This package has implemented bind very similar to how you would use it in f#, here is an example of how you would use it in this module.

```py
(Data(4) 
>> add2.bind()
>> add4.bind()
>> print)
# 10

(Data(None) 
>> add2.bind()
>> add4.bind()
>> print)
# None
```
add2 and add4 both have no ways of dealing with `None`, however you can still pass it along the pipeline because of the bind. 

The way you would indicate if a function can use bind is with a decorator, example below.
```py
@Binded
def add2(x):
    return x+2

@Binded
def add4(x):
    return x+4
```
After the use of the decorator the function can still be used normally and you don't have to call bind on it, but you can now freely use the function with the `.bind()` suffix.

---

# Contribution

Feedback is welcome, create an issue, PR or write a comment on one to give some feedback, you are also welcome to send me an email with ideas.
