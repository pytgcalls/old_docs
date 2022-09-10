Available Methods
=================

This page is about PyTgCalls methods. All the methods listed here are bound to a :class:`~pytgcalls.PyTgCalls` instance,
except for :meth:`~pyrogram.idle()`, which is a special function that can be found in the main package directly.

.. code-block:: python
    :emphasize-lines: 4

    from pytgcalls import PyTgCalls

    app = PyTgCalls(client)
    app.start()

-----

.. currentmodule:: pytgcalls.PyTgCalls

Utilities
---------

.. autosummary::
    :nosignatures:

    get_max_voice_chat <get_max_voice_chat>
    start <start>
    run <run>

.. toctree::
    :hidden:

    get_max_voice_chat <get_max_voice_chat>
    start <start>
    run <run>

.. currentmodule:: pytgcalls

.. autosummary::
    :nosignatures:

    idle <idle>

.. toctree::
    :hidden:

    idle <idle>

.. currentmodule:: pytgcalls.PyTgCalls

Group Calls
-----------

.. autosummary::
    :nosignatures:

        change_volume_call <change_volume_call>
        get_active_call <get_active_call>
        get_call <get_call>
        get_participants <get_participants>
        join_group_call <join_group_call>
        leave_group_call <leave_group_call>

.. toctree::
    :hidden:

        change_volume_call <change_volume_call>
        get_active_call <get_active_call>
        get_call <get_call>
        get_participants <get_participants>
        join_group_call <join_group_call>
        leave_group_call <leave_group_call>

.. currentmodule:: pytgcalls.PyTgCalls

Audio/Video Stream
-------------------

.. autosummary::
    :nosignatures:

        change_stream <change_stream>
        mute_stream <mute_stream>
        unmute_stream <unmute_stream>
        pause_stream <pause_stream>
        resume_stream <resume_stream>
        played_time <played_time>


.. toctree::
    :hidden:

        change_stream <change_stream>
        mute_stream <mute_stream>
        unmute_stream <unmute_stream>
        pause_stream <pause_stream>
        resume_stream <resume_stream>
        played_time <played_time>

.. currentmodule:: pytgcalls.CustomApi

Custom Api
----------

.. autosummary::
    :nosignatures:

        start <start_custom_api>


.. toctree::
    :hidden:

        start <start_custom_api>
