# FunkyPy - Enjoy FP in Python

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
with the module we can make it look like this:
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
## Composing

With this module we can also greatly reduce the effort of composing functions in python, there are 3 ways of composing functions with this module. You can choose which one you find most preferable.

### funcomp function

The first method uses the `funcomp` function and will compose your functions in the order you give them.

```py
add8 = funcomp(add2, add4, add2)

Data(4) >> add8 >> print
# 12
```

### Compose Class

The second method will make use of the Compose class, first you have to initiate the class with the function you would want to compose and then you can keep composing using the `>>` operator.

```py
add8 = Compose(add2) >> add4 >> add2

Data(4) >> add8 >> print
# 12
```

### Flow Keyword

The third and final method in this module will use the Flow keyword to compose functions. this will also make use of the `>>` operator. 

```py
add8 = Flow >> add2 >> add4 >> add2

Data(4) >> add8 >> print
# 12
```

## Bind

This module has implemented bind very similar to how you would use it in f#, here is an example of how you would use it in this module.

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

The way you would indicate if a function can use bind is with the `@Binded` decorator, example below.
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
