# (PART) Introduction



<style>
.float-right {
float:right;
padding:10px;
margin-left:10px;
}
</style>



# Hello

## What topics will we discuss

The Python Universe is **enormous**! We want to share the **minimum** necessary for you to do useful things with Python (while still having fun). So the material on this website is not exhaustive, nor do we want them to be. There are more complete resources elsewhere that you should use for reference. Please refer to [this section](#sec:resources) on resources for more details.

Often there are many ways to use Python to achieve the same result. We will usually share the way that allows you to do the most. We just want to get you started; once you are comfortable, you can explore other more advanced methods of using Python.

## Some Tips



-   **Remember as little as possible!**<br>Instead have a few good websites (or notes) that you can access easily.
-   **Don't try to remember syntax**<br>Instead try to _understand_ how the syntax is structured^[For example, Python defines *scope* using a tab.].
-   **Experiment! Experiment! Experiment!**<br>Playing with the code does not cost anything. So, be curious. Go with your intuition and try things out. Things won't work so well at te start but it **will**<br>get better.
-   **Keyboard Shortcuts**^[For example use `Tab` for command completion.]<br>Using the keyboard makes life _easy_ and more _efficient_. Learn as many as you can.
-   **Don't work alone**<br>Learning is more fun and faster if you discuss and clarify things with a colleague^[The best way to learn is to teach!].
-   **Just learn what you need**<br>When starting programming it is better to learn the basics and just what you need to solve your problem.

## Python?

### What is Python? {.unnumbered}

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/500px-Python-logo-notext.svg.png" class="float-right" width="110px"/>Python is a free and friendly programming language. The 'brain' of Python is called an **interpreter**. The newest version of the Python interpreter is **Python 3**.

### How do I use Python? {.unnumbered}

The Python interpreter can only understand one instruction at a time. Therefore, we usually write many instructions in a single file (code) and then 'pass' it onto the interpreter. These files typically have the extension `.py.` However, Python can also be used interactively using an environment called **Jupyter notebook**.

### How do I use Python? {.unnumbered}

One of the best (and easiest) ways to get started with Python is to use an online environment like Colab. However, if want you can also install it on your computer using the **Anaconda distribution**.

## Ways to access Python?

### Jupyter Notebooks

<div class="figure" style="text-align: center">
<img src="https://jupyter.org/assets/jupyterpreview.png" alt="Examples of Jupyter Notebooks (from [jupyter.org](https://jupyter.org))" width="75%" />
<p class="caption">(\#fig:fig-jupyter-example)Examples of Jupyter Notebooks (from [jupyter.org](https://jupyter.org))</p>
</div>

<img src="http://bollwyvl.github.io/jupyter.github.io/images/jupyter-sq-text.svg" class="float-right" width="110px"/> There are many ways to issue commands to the Python interpreter. A **Jupyter notebook** is one very easy (and very popular) environment to write Python^[or R or Julia] code. **Jupyter notebook** also allows you to combine  [Markdown](https://en.wikipedia.org/wiki/Markdown) and Python in the same document to produce rich content that can be easily converted into reports or even interactive presentation slides!

**Jupyter notebook** files have the extension `.ipynb`^[`ipynb` stands for *i-python-notebook*].

### Colab

<img src="https://miro.medium.com/max/1940/1*ddtqWGkJz1TUCg1WM9qKeQ.jpeg" class="float-right" width="110px"/> **Colab** is a (free) platform offered by Google for coding in Python (and some other languages). Colab offers an environment (almost) identical to **Jupyter notebook**.

Some advantages of using Colab are:

-   Colab will allow us to use Python without having to install it on our computers.
-   Colab will enable us to share our code with others (just like any other Google document)
-   Colab does all the processing on their servers. So, it won't tax your computer^[Of course you pay the price of computations being slightly slower].

Let's see what Colab can do by watching their introductory video.<br>

<iframe width="100%" height="450px" src="https://www.youtube.com/embed/inN8seMm7UI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Installing Python with Anaconda

You **do not** have to install Python locally on your machine for this workshop. However, if you like to have Python on your computer we recommend that you use the Anaconda distribution called **miniconda**.

**Step 1.** Visit the <a href="https://www.anaconda.com/products/individual" target="_blank" />download page</a> at Anaconda.<br>
**Step 2.** Download and install the 64-bit _Python 3_ distribution suitable for your operating system.<br>(**Windows** users should run Anaconda as **Administrator**)

#### Updating packages with Anaconda

#### Using Anaconda-Navigator

## Markdown

### What is Markdown?

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/128px-Markdown-mark.svg.png" class="float-right" width="110px"/>**Markdown** is a simple, but powerful language for 'word processing'. Markdown is a simple and efficient way to write. Like $\LaTeX$ it tries to separate content from style. You can convert the content of Markdown (`.md`) files directly into PDF or HTML formats. Markdown can be used in **Jupyter notebook** to add text. You can read more about it at the [Wikipedia](https://en.wikipedia.org/wiki/Markdown).

One of our favorite free, cross-platform Markdown editors is  [Typora](https://typora.io). There are also web based editors ([StackEdit](https://stackedit.io), [Dillinger](http://dillinger.io), [Madoko](https://www.madoko.net), [Markdown & LaTeX Editor](https://upmath.me)).

## Conventions

Python code is shown in a grey box like this:


```python
print('Code is shown in a box like this')
```

A `#` will be used to show the result (or output) of the code. This will appear immediately after the code, like this:


```python
print('Code is shown in a box like this')
#> Code is shown in a box like this
```

## Resources {#sec:resources}

### Jupyter Notebooks

1.  Take a look at [this site](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/) for some cool tricks and optimisations for these notebooks.
