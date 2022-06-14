# matplotlib-eval

Evaluating matplotlib by generating a series of random walks.

### Selected Code Explanations

**random_walks.py**

* Contains a class `RandomWalk` which will be imported into the implementation file `rw_visual.py`.
* A constructor defining a default number of points and starting points for the walk.
* The method `fill_walk()` does most of the work.
* Does not include steps that go nowhere (0,0).

<pre>
x_direction = choice([1,-1))    # 1 == right, -1 == left
y_direction = choice([1,-1])    # 1 == up,  -1 == down

# Determines the length of each step
x_step = x_direction * x_distance
y_step = y_direction * y_distance
</pre> 

**rw_visual.py**

* Implements a loop that allows you to continue generating new maps if you choose. You can comment out lines 30-32 if you wish to disable this functionality.
* This a simple `input()` call. The message to generate a new map will be in your CLI.

![](https://assets.codepen.io/2154393/random_walk_example_001.png)
