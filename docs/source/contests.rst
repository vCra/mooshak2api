Contests
============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

In order to get a Contest object, use mooshak2api.contests.get

.. autofunction:: mooshak2api.contests.get

Or, if you want all Contests, you can use mooshak2api.contests.get_all

.. autofunction:: mooshak2api.contests.get_all

You will be returned an array of Contests

Contest Objects are the python interpretation of mooshak2 Contests. The properties of it depend on what is returned, but
should contain at least an ID.

.. autoclass:: mooshak2api.contests.Contest

You can also create a new Contest in mooshak2, by creating a new Contest Object, and then calling .create

.. autofunction:: mooshak2api.contests.Contest.create

You can also update and delete contests!

.. autofunction:: mooshak2api.contests.Contest.update

.. autofunction:: mooshak2api.contests.Contest.delete

