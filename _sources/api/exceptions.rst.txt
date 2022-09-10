Exceptions
==========
All PyTgCalls API errors live inside the ``exceptions`` sub-package: ``pytgcalls.exceptions``.

.. code-block:: python

    from pytgcalls.exceptions import GroupCallNotFound

    try:
        ...
    except GroupCallNotFound as e:
        ...

Missing Library Errors
----------------------
.. autoexception:: pytgcalls.exceptions.NodeJSNotInstalled()


NodeJS Errors
-------------
.. autoexception:: pytgcalls.exceptions.NodeJSNotRunning()

Deprecation Errors
------------------
.. autoexception:: pytgcalls.exceptions.TooOldNodeJSVersion()
.. autoexception:: pytgcalls.exceptions.TooOldPyrogramVersion()
.. autoexception:: pytgcalls.exceptions.TooOldTelethonVersion()

MtProto Errors
--------------
.. autoexception:: pytgcalls.exceptions.InvalidMtProtoClient()
.. autoexception:: pytgcalls.exceptions.NoMtProtoClientSet()
.. autoexception:: pytgcalls.exceptions.TelegramServerError()
.. autoexception:: pytgcalls.exceptions.RTMPStreamNeeded()

PyTgCalls Errors
----------------
.. autoexception:: pytgcalls.exceptions.PyTgCallsAlreadyRunning()
.. autoexception:: pytgcalls.exceptions.GroupCallNotFound()
.. autoexception:: pytgcalls.exceptions.NoActiveGroupCall()
.. autoexception:: pytgcalls.exceptions.NotInGroupCallError()
.. autoexception:: pytgcalls.exceptions.AlreadyJoinedError()
.. autoexception:: pytgcalls.exceptions.UnMuteNeeded()

Stream Errors
-------------
.. autoexception:: pytgcalls.exceptions.InvalidStreamMode()
.. autoexception:: pytgcalls.exceptions.NoVideoSourceFound()
.. autoexception:: pytgcalls.exceptions.InvalidVideoProportion()
.. autoexception:: pytgcalls.exceptions.NoAudioSourceFound()

CustomApi Errors
----------------
.. autoexception:: pytgcalls.exceptions.TooManyCustomApiDecorators()