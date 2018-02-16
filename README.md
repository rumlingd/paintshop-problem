
# Paintshop Problem

My attempt at solving the Paintshop Problem in Python.
[See the assignment](paint_shop.pdf)

## Getting Started

Python 3.5 was used for this project

### Approach
1. In the Format Input Class, I sort each customer's preference such that it is arranged small to high number and 'G' is before 'M'
   e.g [[1,'G']['5','G'],[3,'M'],[4,'M']]. This indexing ensures the cheaper gloss colour types are favoured.

2. I then used the Python function product from the itertools library to produce all possible candidate solutions 
   given the observed customer preferences. I inserted picky customers i.e customers that only want one colour
   into all candidate solutions.

3. I filled all remaining empty entries in the candidate solutions with the cheaper 'G'

4. Finally I checked if all customers had at least one colour satisfied. Solutions closer to the top were preferred.
   If not all customers were given at least one preferred paint, I return 'No solution exists'


### How to run

Run at the top of the directory

```
python main.py text-files/example1.txt
G G G G M

```


## Running the tests

Simple tests to verify we are getting the correct output

```
python -m unittest discover
```

### Coding style guide

Link to coding style guide which I hope I adhered to :D

```
https://google.github.io/styleguide/pyguide.html
```

