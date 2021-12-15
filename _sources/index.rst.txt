Welcome to PyTgCalls!
=====================

.. raw:: html

    <div align="center">
        <a href="/">
            <div><img src="https://user-images.githubusercontent.com/32808683/111091141-62473b00-8508-11eb-9c05-3e0fd4a21af3.png" alt="PyTgCalls Logo" width="420"></div>
        </a>
    </div>

    <p align="center">
        <b>A simple and elegant client that allows you to make group voice calls quickly and easily.</b>
        <br>
        <a href="https://github.com/pytgcalls/pytgcalls/tree/master/example">
        Examples
    </a>
    •
    <a href="https://pytgcalls.github.io/">
        Documentation
    </a>
    •
    <a href="https://pypi.org/project/py-tgcalls/">
        PyPi
    </a>
    •
    <a href="https://t.me/pytgcallsnews">
        Channel
    </a>
    •
    <a href="https://t.me/pytgcallschat">
        Chat
    </a>
    </p>

.. code-block:: python

    from pytgcalls import PyTgCalls
    from pytgcalls import idle
    from pytgcalls.types import AudioPiped
    ...
    client = # Here Your MtProto Client
    app = PyTgCalls(client)
    app.start()
    app.join_group_call(
        -1001185324811,
        AudioPiped(
            'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4',
        )
    )
    idle()

This project allows to make Telegram group call using MtProto and WebRTC, this is possible thanks to the power of NodeJS's WebRTC library and `@evgeny-nadymov <https://github.com/evgeny-nadymov/>`_

First Steps
=============

.. hlist::
    :columns: 2

    - :doc:`Quick Start <intro/quickstart>`: Overview to get you started quickly.
    - :doc:`Calling Methods <start/invoking>`: How to call PyTgCalls’s methods.
    - :doc:`Handling Updates <start/updates>`: How to handle PyTgCalls updates.

.. toctree::
    :hidden:
    :caption: Introduction

    intro/quickstart
    intro/install

.. toctree::
    :hidden:
    :caption: Getting Started

    start/invoking
    start/updates
    start/examples

.. toctree::
    :hidden:
    :caption: API Reference

    api/client
    api/custom_api
    api/stream_type
    api/methods/index
    api/types/index
    api/decorators
    api/exceptions

.. toctree::
    :hidden:
    :caption: Meta

    releases/index
