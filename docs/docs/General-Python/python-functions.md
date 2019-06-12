---
layout: default
title: Python Common Functions
parent: General Python
nav_order: 2
---

# Python Common Functions
{: .no_toc }

This is a compilation of all python functions I frequently use with the syntax explained and examples.
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## List Functionss

---

### List Comprehension

#### Syntax and Notes

```python
list = [expresion for item in list]
```

- List comprehensions are good way to create lists from data.
- They are generally faster than a loop that would accomplish the same result. 

---

#### Example #1

Create a list containing all of the items inside `list1` that are not also inside `list2`.

```python
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3]
list3 = [x for x in list1 if x not in list2]
print(list3)
#result = [4, 5]
```
---

### Removing List Items

#### Syntax and Notes

```python
list.remove(element)
```

```python
list.pop(element_index)
```

- `pop()` is the faster of the two but requires the index of the element to be  removed.
- if no index is specified for `pop()` it will remove the last item in the list.
- `pop()` also returns the element it is removing.
- `remove()` will only remove the first instance of the specified element that it finds, if you need to remove multile elements you will have to iterate through the list

---

#### Example #1

Remove the string `"dog"` from the list.

```python
animals = ["cat", "dog", "horse"]
animals.pop[1]
print(animals)
# result = ["cat", "horse"]
```
```python
animals = ["cat", "dog", "horse"]
animals.remove["dog"]
print(animals)
# result = ["cat", "horse"]
```
### Adding List Items


