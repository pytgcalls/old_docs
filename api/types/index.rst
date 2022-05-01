Available Types
=================

This page is about PyTgCalls Types. All types listed here are available through the ``pytgcalls.types`` package.
Unless required as argument to a client method, most of the types don't need to be manually instantiated because they
are only returned by other methods. You also don't need to import them, unless you want to type-hint your variables.

.. code-block:: python
    :emphasize-lines: 1

    from pytgcalls.types import Update, AudioImagePiped, ErrorDuringJoin, ...

.. note::

    Optional fields always exist inside the object, but they could be empty and contain the value of ``None``.
    Empty fields aren't shown when, for example, using ``print(update)`` and this means that
    ``hasattr(update, "participant")`` always returns ``True``.

    To tell whether a field is set or not, do a simple boolean check: ``if update.participant: ...``.

-----

.. currentmodule:: pytgcalls.types

Raw Types
----------

.. autosummary::
    :nosignatures:

    GroupCall
    GroupCallParticipant
    Update

.. toctree::
    :hidden:

    GroupCall
    GroupCallParticipant
    Update


.. currentmodule:: pytgcalls.types

Group Calls Event Types (Raw)
-----------------------------

.. autosummary::
    :nosignatures:

    ErrorDuringJoin
    LeftVoiceChat

.. toctree::
    :hidden:

    ErrorDuringJoin
    LeftVoiceChat

.. currentmodule:: pytgcalls.types

.. currentmodule:: pytgcalls.types

Stream Event Types (Raw)
-----------------------------

.. autosummary::
    :nosignatures:

    ChangedStream
    MutedStream
    PausedStream
    ResumedStream
    StreamAudioEnded
    StreamDeleted
    StreamVideoEnded
    UnMutedStream

.. toctree::
    :hidden:

    ChangedStream
    MutedStream
    PausedStream
    ResumedStream
    StreamAudioEnded
    StreamDeleted
    StreamVideoEnded
    UnMutedStream

Group Calls Event Types
-----------------------

.. autosummary::
    :nosignatures:

    JoinedGroupCallParticipant
    UpdatedGroupCallParticipant
    LeftGroupCallParticipant

.. toctree::
    :hidden:

    JoinedGroupCallParticipant
    UpdatedGroupCallParticipant
    LeftGroupCallParticipant

.. currentmodule:: pytgcalls.types

Input Stream Types (Raw)
------------------------

.. autosummary::
    :nosignatures:

    InputStream
    InputAudioStream
    InputVideoStream

.. toctree::
    :hidden:

    InputStream
    InputAudioStream
    InputVideoStream

Piped Input Stream Types (With FFMpeg)
--------------------------------------

.. autosummary::
    :nosignatures:

    CaptureAudioDevice
    CaptureAVDesktop
    CaptureAVDeviceDesktop
    CaptureVideoDesktop
    AudioImagePiped
    AudioPiped
    AudioVideoPiped
    VideoPiped

.. toctree::
    :hidden:

    AudioImagePiped
    AudioPiped
    AudioVideoPiped
    VideoPiped

.. currentmodule:: pytgcalls.types

Input Stream Parameters Types (Raw)
-----------------------------------

.. autosummary::
    :nosignatures:

    AudioParameters
    VideoParameters

.. toctree::
    :hidden:

    AudioParameters
    VideoParameters

.. currentmodule:: pytgcalls.types

Input Stream Parameters Types (Pre-Made)
----------------------------------------

.. autosummary::
    :nosignatures:

    HighQualityAudio
    MediumQualityAudio
    LowQualityAudio
    HighQualityVideo
    MediumQualityVideo
    LowQualityVideo

.. toctree::
    :hidden:

    HighQualityAudio
    MediumQualityAudio
    LowQualityAudio
    HighQualityVideo
    MediumQualityVideo
    LowQualityVideo
