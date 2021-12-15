Calling Methods
===============

At this point, we have successfully :doc:`installed PyTgCalls <../intro/install>` and installed an MtProto client; we are now aiming towards the core of the library. It’s time to start playing with the API!

Basic Usage
-----------
Making API method calls with PyTgCalls is very simple. Here's a basic example we are going to examine step by step:

.. code-block:: python

    from pytgcalls import PyTgCalls
    from pytgcalls import idle
    from pytgcalls.types import AudioPiped
    ...
    api_id = 12345
    api_hash = '0123456789abcdef0123456789abcdef'
    ...
    app = PyTgCalls(client)
    app.start()
    app.join_group_call(
        -1001185324811,
        AudioPiped(
            'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4',
        )
    )
    idle()

Basic step-by-step
^^^^^^^^^^^^^^^^^^
#.  Let's begin by importing the Client class, Stream type and idle function:

    .. code-block:: python

        from pytgcalls import PyTgCalls
        from pytgcalls import idle
        from pytgcalls.types import AudioPiped

#.  Now let's to import your MtProto Client:

    If you need Pyrogram:

    .. code-block:: python

        from pyrogram import Client

    If you need Telethon:

    .. code-block:: python

        from telethon import TelegramClient

#.  Set your api_id and api_hash taken from https://my.telegram.org/apps:

    .. code-block:: python

        api_id = 12345
        api_hash = '0123456789abcdef0123456789abcdef'

#.  Initialize the MtProto client:

    If you are using Pyrogram:

    .. code-block:: python

        client = Client('test_session', api_id, api_hash)

    If you are using Telethon:

    .. code-block:: python

        client = TelegramClient('test_session', api_id, api_hash)

#.  Initialize the PyTgCalls client:

    .. code-block:: python

        app = PyTgCalls(client)

#.  Start the PyTgCalls client:

    .. code-block:: python

        app.start()

#.  Now you can call any method you like:

    .. code-block:: python

        app.join_group_call(
            -1001185324811,
            AudioPiped(
                'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4',
            )
        )

#.  Now add idle to block your code (To avoid the closing of script):

    .. code-block:: python

        idle()

Asynchronous Calls
------------------
In case you want PyTgCalls to run asynchronously:

.. code-block:: python

    import asyncio
    from pytgcalls import PyTgCalls
    from pytgcalls import idle
    from pytgcalls.types import AudioPiped
    ...
    app = PyTgCalls(client)

    async def main():
        await app.start()
        await app.join_group_call(
            -1001185324811,
            AudioPiped(
                'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4',
            )
        )
        await idle()

    asyncio.get_event_loop().run_until_complete(main())

Asynchronous step-by-step
^^^^^^^^^^^^^^^^^^^^^^^^^

#.  Import PyTgCalls, AsyncIO and create an instance:

    .. code-block:: python

        import asyncio
        from pytgcalls import PyTgCalls
        from pytgcalls import idle
        ...
        app = PyTgCalls(client)

#.  Async methods can't normally be executed at the top level, because they must be inside an async-defined function;
    here we define one and put our code inside; method calls require the await keyword:

    .. code-block:: python

        async def main():
        await app.start()
        await app.join_group_call(
            -1001185324811,
            AudioPiped(
                'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4',
            )
        )
        await idle()

#.  Then we tell asyncio to call ``main()``, they will call the function in async mode

    .. code-block:: python

        asyncio.get_event_loop().run_until_complete(main())
