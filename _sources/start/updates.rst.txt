Handling Updates
================

Calling API methods sequentially is cool, but how to react when, for example, changed list of participants?
This page deals with updates and how to handle such events in PyTgCalls. Let’s have a look at how they work.

Defining Updates
----------------
First, let's define what are these updates. As hinted already, updates are simply events that happen in PyTgCalls
(joining group call, changed participants list, stream ended and etc.), which are meant to notify you about a new
specific state that has changed. These updates are handled by registering one or more callback functions in your app
using :doc:`Decorators <../api/decorators>`.

Each handler deals with a specific event and once a matching update arrives from Telegram or NodeJS, your registered callback
function will be called back by the framework and its body executed.

Registering a Handler
---------------------
To explain how handlers work let's examine the one which will be in charge for handling :class:`~pytgcalls.types.stream.StreamVideoEnded`
updates when a stream of type video is ended. Every other kind of handler shares the same setup logic and you should not
have troubles settings them up once you learn from this section.

Using Decorators
^^^^^^^^^^^^^^^^
The most elegant way to register a stream end handler is by using the :meth:`~pytgcalls.PyTgCalls.on_stream_end` decorator:

.. code-block:: python

    from pytgcalls import PyTgCalls
    from pytgcalls.types import Update
    from pytgcalls.types import StreamVideoEnded
    ...
    app = PyTgCalls(client)

    @app.on_stream_end()
    async def my_handler(client: PyTgCalls, update: Update):
        if isinstance(update, StreamVideoEnded):
            await pytgcalls.change_stream(
                -1001185324811,
                stream=AudioVideoPiped(
                    'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4',
                )
            )

    app.run()

The defined function ``my_handler``, which accepts the two arguments *(client, update)*, will be the function that gets
executed every time a new update arrives.

.. note::

    You can mix ``def`` and ``async def`` handlers as much as you need, PyTgCalls will still work concurrently and
    efficiently regardless of what you choose.
