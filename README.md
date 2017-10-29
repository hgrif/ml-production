# Machine Learning in Production

[![Build Status](https://travis-ci.org/hgrif/ml-production.svg?branch=master)](https://travis-ci.org/hgrif/ml-production)


## Getting started

Start with creating [Github](https://github.com/login) and [Kaggle](https://www.kaggle.com/account/login) accounts if you don't have them yet.

We'll work in Jupyter Notebooks and use a code editor.
Make sure you have an editor set up with linting.
If you're unsure what that means, install [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/#section=mac).

Get this repository to your account and the code on your machine: [fork](https://help.github.com/articles/fork-a-repo/) this repository to your account and [clone](https://help.github.com/articles/cloning-a-repository/) your repository to your machine.

All the Python packages needed for this project are specified in a [virtual environment](https://tdhopper.com/blog/my-python-environment-workflow-with-conda/).
Make sure [conda](https://conda.io/miniconda.html) is installed, `cd` into the project root and create a new virtual environment:

```bash
$ conda env create -f environment.yml
```

This will create a virtual environment called `ml-production` and install the Python packages in it.

Now activate the virtual environment so that we can use it (you might have to use `activate` instead of `source activate` if you're on Windows):

```bash
(ml-production) $ source activate ml-production
```

We have some custom code for you in the folder `shelter`.
Install the `shelter` package located in the project root with development mode:

```bash
(ml-production) $ python setup.py develop
```

Now start the Jupyter Notebook server so that we can start our Machine Learning:

```bash
(ml-production) $ jupyter notebook
```


## Morning

We'll start with building a Machine Learning model.
Open the Notebook `01-machine-learning-model.ipynb` in the folder `notebooks/` and follow the instructions.


## Afternoon

Having made our first steps with building, we'll now focus on same development best practices.
The material can be found in the Notebook `02-machine-learning-in-production.ipynb`.
