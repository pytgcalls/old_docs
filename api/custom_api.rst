Custom Api
===============

You have entered the API Reference section where you can find detailed information about Custom API. The Front-end API
class, all available methods, types, attributes, decorators detailed descriptions can be
found starting from this page.

This page is about the CustomAPI class, which exposes high-level methods for an easy access to the API.

.. code-block:: python
    :emphasize-lines: 1-3

    from pytgcalls import CustomApi

    app = CustomApi(client)
    app.start()

-----

Details
-------
.. autoclass:: pytgcalls.CustomApi()

.. _Client: https://docs.pyrogram.org/api/client
.. _TelegramClient: https://docs.telethon.dev/en/latest/modules/client.html
