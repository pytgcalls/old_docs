PyTgCalls Client
=================

You have entered the API Reference section where you can find detailed information about PyTgCalls API. The main Client
class, all available methods, types, attributes, decorators detailed descriptions can be
found starting from this page.

This page is about the Client class, which exposes high-level methods for an easy access to the API.

.. code-block:: python
    :emphasize-lines: 1-3

    from pytgcalls import PyTgCalls

    app = PyTgCalls(client)
    app.start()

-----

Details
-------
.. autoclass:: pytgcalls.PyTgCalls()

.. _Client: https://docs.pyrogram.org/api/client
.. _TelegramClient: https://docs.telethon.dev/en/latest/modules/client.html
.. _InputPeer (P): https://docs.pyrogram.org/telegram/base/input-peer
.. _InputPeer (T): https://tl.telethon.dev/types/input_peer.html
