Introduction
============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

mooshak2api is a simple API for use with the mooshak2 REST API. It was built as a need to get around the
somewhat patchy documentation of Mooshak 2's API. It currently supports the following:

* Getting Contests
* Getting Problems
* Evaluating code for a problem

While some additional functionality is also included (such as creating problems), in almost cases, this will be
disabled on the mooshak2 server. This is not (and can't be) tested for obvious reasons.

As a general rule, create and get methods will return a python interpretation of that option. Currently, almost all
properties that are from mooshak are strings (e.g. the number 4 will actually be '4' - true and false are also 'yes'
and 'no').



