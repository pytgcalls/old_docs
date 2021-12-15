Decorators
==========

While still being methods bound to the :class:`~pytgcalls.PyTgCalls` class, decorators are of a special kind and thus
deserve a dedicated page.

Decorators are able to register callback functions for handling updates in a much easier and cleaner way;
All you need to do is adding the decorators on top of your
functions.

.. code-block:: python
    :emphasize-lines: 7

    from pytgcalls import PyTgCalls
    from pytgcalls.types import Update
    ...
    client = # Here Your MtProto Client
    app = PyTgCalls(client)

    @app.on_raw_update()
    async def my_handler(client: PyTgCalls, update: Update):
        print(message)

    app.run()

-----

PyTgCalls Decorators
--------------------

.. Decorators
.. autodecorator:: pytgcalls.PyTgCalls.on_closed_voice_chat()
.. autodecorator:: pytgcalls.PyTgCalls.on_group_call_invite()
.. autodecorator:: pytgcalls.PyTgCalls.on_kicked()
.. autodecorator:: pytgcalls.PyTgCalls.on_left()
.. autodecorator:: pytgcalls.PyTgCalls.on_participants_change()
.. autodecorator:: pytgcalls.PyTgCalls.on_raw_update()
.. autodecorator:: pytgcalls.PyTgCalls.on_stream_end()

CustomApi Decorators
--------------------

.. Decorators
.. autodecorator:: pytgcalls.CustomApi.on_update_custom_api()
