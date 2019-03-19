Connection
============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

The mooshak2 connection defines how you connect to a mooshak2 instance. The easiest way of getting a client instance
is to call ``mooshak2api.login`` with your instance details.

.. autofunction:: mooshak2api.login

This client should then be passed to any calls you make to other functions.

It should be noted that by default, a mooshak2 session only lasts for 1 hour. As a result, you should check yourself
if the session has expired, and if so, login again.

.. autoclass:: mooshak2api.client.Client

If you want to test that the endpoint is accessible, then you can use test

.. autofunction:: mooshak2api.client.Client.test

If you want to make a connection, you can use headers_with_auth

.. autofunction:: mooshak2api.client.Client.headers_with_auth


