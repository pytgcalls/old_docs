Quick Start
===========

The next few steps serve as a quick start for all new Pythoneer that want to see PyTgCalls in
action as fast as possible. Let's go!

Get PyTgCalls Real Fast
-----------------------

#. Install PyTgCalls with ``pip3 install -U py-tgcalls``.

#. Choose your MtProto client between `Pyrogram <https://github.com/pyrogram/pyrogram>`_ or `Telethon <https://github.com/LonamiWebs/Telethon>`_

#. Get your own Telegram API key from https://my.telegram.org/apps.

#.  Open your best text editor and use the following:

    .. code-block:: python

        from pytgcalls import PyTgCalls
        from pytgcalls import idle
        from pytgcalls.types import AudioPiped
        ...
        chat_id = -1001185324811
        app = PyTgCalls(client)
        app.start()
        app.join_group_call(
           chat_id,
           AudioPiped(
               'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4',
           )
        )
        idle()

#. Replace *client* and *chat_id* values with your own.

#. Save the file as ``main.py``.

#. Run the script with ``python3 main.py``

#. Follow the instructions on your terminal to login.

#. Watch PyTgCalls playing the audio file.

#. Join our `community`_.

Enjoy the API
-------------

That was just a quick overview that barely scratched the surface!
In the next few pages of the introduction, we'll take a much more in-depth look of what we have just done above.

Feeling eager to continue? You can take a shortcut to :doc:`Calling Methods <../start/invoking>` and come back later to
learn some more details.

.. _community: https://t.me/PyTgCallsChat
