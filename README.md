TextTeaser
=============

TextTeaser is an automatic summarization algorithm.

This is now the official version of TextTeaser. Future developments of TextTeaser will be in this repository.

The original Scala TextTeaser can still be accessed [here](https://github.com/MojoJolo/textteaser).

### Installation

    >>> git clone https://github.com/DataTeaser/textteaser.git
    >>> pip install -r textteaser/requirements.txt

### How to Use

    >>> from textteaser import TextTeaser
    >>> tt = TextTeaser()
    >>> tt.summarize(title, text)

You can also test TextTeaser by running `python test.py`.

### Commercial Support

Commercial support for TextTeaser or custom summarizers can be provided by [DataTeaser](http://www.datateaser.com/?textteaser).