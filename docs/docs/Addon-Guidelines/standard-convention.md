---
layout: default
title: Standard Convention
parent: Addon Guidelines
nav_order: 1
---

# Standard Convention
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Code Conventions

Generally all code should conform to [pep8](https://www.python.org/dev/peps/pep-0008/) standards, the one exception is line length which can be up to 120 characters long rather than the 80 characters defined in pep8. 

I also have some personal conventions that I try to adhere to in order to keep consistency across all my projects, more on this [HERE]({{ site.baseurl }}{% link docs/General-Python/personal-conventions.md %}#aux-nav).

Blender scripts are periodically checked for pep8 compliance, to be included in this check add this comment to the top of the script:

`# <pep8 compliant>`

If you want to adhere to the 80 character line limit you can use the comment:

`# <pep8-80 compliant>`

---

## Layout Variable Names

When writing user interfaces you should stick to the following variable names whenever you declare a layout.

Layout Type | Variable Name | Example
------------  | ------------- | ------------
`row()` | row | `row = layout.row()`
`column()` | col  | `col = layout.column()`
`split()` | split  | `split = layout.split()`
`menu_pie()` | pie | `pie = layout.menu_pie()`

---

