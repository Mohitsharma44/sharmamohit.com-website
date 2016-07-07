+++
Categories = ["Development", "Python", "USCL"]
Description = "Installing Python 2.7, Pip, Ipython, Numpy and Matplotlib"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-05-26T01:55:34-04:00"
title = "Python_Installing"

+++


<h1 align='center'>Installing Python and other packages</h1>

We will be using Python 2.7.x throughout our course.
We will be installing following packages along with python 2.7.x:
- [`pip`](https://en.wikipedia.org/wiki/Pip_%28package_manager%29 'About Pip')
- [`Ipython`](http://ipython.org/ 'Ipython Homepage')
- [`Numpy`](http://www.numpy.org/ 'Numpy Homepage')
- [`Matplotlib`](http://matplotlib.org/ 'Matplotlib Homepage')

## On Linux (Debian/ Ubuntu based distro):

- Python is pre-installed on every Debian based linux distributions like Ubuntu since Ubuntu requires various python libraries to run. 


- To install `pip, numpy` and `matplotlib`, open your terminal (`Ctrl + Alt + T`) and type the following commands in it:

>`sudo apt-get install python-pip python-numpy python-matplotlib`

- To install `ipython`, type the following comands in the terminal:

>`sudo pip install ipython`

## On Windows (does not support Windows 10 Build 10074)

- It is recommended that you use `Linux based OS` (if not natively then you can use it in a Virtual Machine)


- The best way of installing `Python 2.7.x` and all the above packages is to download `anaconda` from [`continuum analytics`](continuum.io/downloads#all 'Download Anaconda').


- Install it as any regular program and let the installer finish. (It will take 10 - 15 minutes to complete the installation)


## On Mac

(Follow the same guide as mentioned for Windows or else use the following approach)
- Install [`Xcode for Mac`](https://developer.apple.com/xcode/downloads/ 'Download XCode')


- Install `Xcode` command line tools:
>`xcode-select --install`

- Install `Homebrew`:
>`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

- Install `Python` through `Homebrew`:
>`brew install python`

- Install `numpy`:
>`pip install numpy`

- Install `Matplotlib`:
>`pip install matplotlib`

## Test to confirm the Installation of above packages:

Open Terminal/ Command prompt and type: `ipython`

Next let's try importing `numpy` and `matplotlib` to check their versions. Type:


    import numpy
    print 'Numpy Version: ',numpy.__version__
    import matplotlib
    print 'Matplotlib Version: ',matplotlib.__version__

    Numpy Version:  1.8.2
    Matplotlib Version:  1.4.2

