# Brainstorming: libraries


## Scientific computation

The most important libraries (at least for us) are [NumPy](http://www.numpy.org/) and [SciPy](http://www.scipy.org/). They contain the most important mathematical methods, like: 

* linear algebra
* statistics
* signal processing
* optimization
* Fourier Transforms
* ...

There are many others, specialised for specific fields. For instance [Natural Language Toolkit (NLTK)](http://www.nltk.org/) for linguistic tasks.

And then visualization is important, of course. The most popular library is [matplotlib](http://matplotlib.org/).


## Machine learning

You can find many different ML problems here:

* [Kaggle](https://www.kaggle.com/)
* [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets.html)

Some useful libraries containing different ML methods:

* [scikit-learn](http://scikit-learn.org/stable/)
* [Modular Toolkit for Data Processing (MDP)](http://mdp-toolkit.sourceforge.net/): It's not very actively developed anymore but we still use it a lot in our workgroup.


## (Social) network analysis

There are several Python libraries for (social) network analysis like [NetworkX](http://networkx.github.io/) or [graph-tool](https://graph-tool.skewed.de/). Datasets containing networks can found for instance here:

* [Stanford Large Network Dataset Collection](http://snap.stanford.edu/data/index.html)
* [Gephi Wiki](https://github.com/gephi/gephi/wiki/Datasets)
* [Social Graphs in Movies](http://moviegalaxies.com/)


## IT-Security

There are crypto libraries like [cryptography](https://cryptography.io/en/latest/) and [PyCrypto](https://www.dlitz.net/software/pycrypto/).


## Scraping websites

* [import.io](https://import.io/): Service that extracts data from websites
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/): Convenient access to content of a downloaded website
* [Scrapy](http://scrapy.org/): Framework for scraping websites
* [Selenium](http://www.seleniumhq.org/): Allows complete automation of a browser via script

Think of data sources like concert tickets or products, movies (IMDB)...

Note however, that many websites don't need to be scraped because they offer a proper API to access their content. Here are examples from a [long list](http://www.programmableweb.com/category/all/apis?order=field_popularity) with some of the most popular web APIs:

* Google Maps, Twitter, YouTube, Flickr, Facebook, Amazon Product Advertising, Twillo, Last.fm, eBay, ...


## Web development

There are Python frameworks for developing websites, i.e., organizing all the server-side logic and databases with Python. Two notable framworks are [Django](https://www.djangoproject.com/) (complex) and [WebPy](http://webpy.org/) (light-weight).


# Examples

## Virtual rat hippocampus

![Place cell architecture](http://www.scholarpedia.org/w/images/thumb/9/94/HierarchicalSFAModel.jpg/400px-HierarchicalSFAModel.jpg)
![Plce cell result](http://www.scholarpedia.org/w/images/thumb/9/96/ModelCells.jpg/200px-ModelCells.jpg)

That's something we are doing a lot in our workgroup. If you like to try something like this, ask Fabian!

## Google's dreaming neural networks

Google realeased the Python scripts for it's famous dreaming neural networks ([deepdream](https://github.com/google/deepdream)). Others have build on that, for instance [making *Fear and Loathing in Las Vegas* even more uncanny](https://github.com/graphific/DeepDreamVideo):

![Fear and Loathing example](https://camo.githubusercontent.com/dcf15823a576975a5bd2d1af1696a25a07b7e6aa/687474703a2f2f6d656469612e67697068792e636f6d2f6d656469612f6c34316c537a6a5473474a63497a704b672f67697068792e676966)

Here's another project that created a simple user interface: [bat-country](https://github.com/jrosebr1/bat-country)

## WhatsApp chat bots

Someone wrote [yowsup](https://github.com/tgalal/yowsup), an Python wrapper for the (unoffcial) WhatsApp API. People used this for instance to write chat bots ([yowlayer-cleverbot](https://github.com/tgalal/yowlayer-cleverbot), [WAbot](https://github.com/KaveenR/WAbot)) for WhatsApp.

## Automating Tinder with Eigenfaces

Someone wrote a (Java) script to automatically find matches for him/her using Eigenfaces: [tinderbox](https://github.com/crockpotveggies/tinderbox)

![two eigenfaces](https://raw.githubusercontent.com/crockpotveggies/tinderbox/master/public/img/tinderbox_eigenfaces_models.jpg)

## Cheap ticket notification

A nice example for scraping websites that don't have an API: [LTUR-Notifer](https://github.com/policecar/ltur-notifier) scrapes information from [bahn.ltur.com](bahn.ltur.com) and sends email or push notification to a smartphone when a new cheap ticket appears.

## Packet sniffing and injection

Also people seem to use Python scripts for [packet sniffing and injection](http://suryamattu.com/PACKET-SNIFFING-TUTORIAL), for instance.

## Implementing Machine learning algorithms on your own

Basically all you need is numpy and the corresponding math.

Examples: Feed Forward Neural Networks, Auto encoders, Sparse Coding, Baysian Networks, Restricted Boltzmann machines, ...


## Solving a machine learning problem

Using existing libs like scikit the focus would be on solving a particular task in a good way.
So it would be problem driven and you should have a concrete idea about the problem

Have a look at http://scikit-learn.org/stable/index.html for examples for clustering, resgression, classification, ...

Examples: Object detection (Eye, hand, ...), Spam detection, ...

## Raspberry Pi

Another place to turn your Python skills into fun and usefull projects it the [Raspberry Pi](https://www.raspberrypi.org/). Some random projects include

* [High-altitude photography](http://opensource.com/life/15/9/pi-sky-high-altitude-ballooning-raspberry-pi),
* [Crypto currency trackers](http://makezine.com/projects/make-43/crypto-currency-tracker/),
* [Dirty dish detectors](http://makezine.com/projects/make-43/dirty-dish-detector/), and
* [Pirate Radios](http://makezine.com/projects/raspberry-pirate-radio/).

You can find many more projects for inspiration on [Make](http://makezine.com/?s=raspberry) and [Instructables](http://www.instructables.com/id/Raspberry-Pi-Projects/).
