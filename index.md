---
title: PyTgCalls documentation
description: Async client API for the Telegram Group Calls
image: https://avatars.githubusercontent.com/u/75855609
---
# PyTgCalls API
> PyTgCalls is based on PyServerCall, [TgCallsJS](https://github.com/tgcallsjs/tgcalls),
> [SocketIO](https://socket.io/) and [WebRTC](https://webrtc.org/)
> to work with Telegram group calls.

# Recent changes
> ## Update of 10/03/2021 - 0.1.0 (Beta 5)
> - Added kick listener
> - Added new parameters!
> - Fix some bugs

> ## Update of 04/03/2021 - 0.1.0 (Beta 4)
> - Now is async!

> ## Update of 24/02/2021- 0.1.0 (Beta 3)
> - Added debug mode

# Audio Needed
The following is the required audio type

Field | Value
--- | ---
acodec | pcm_s16le
bitrate | Your bitrate preference

# Methods
These are the currently available PyTgCalls methods

## PyTgCalls
Class initialization

Field | Type | Description
--- | --- | ---
app | pyrogram.Client | A Pyrogram client
port | Integer | Port to run local server
log_mode | Boolean | Debug mode

### _Example_
``` python
...
app = Client(...)
pytgcalls = PyTgCalls(app)
...
```


## join_group_call
Join a group call to stream a file

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
file_path | String | Path of a RAW audio file
bitrate | Integer | Audio stream bitrate (maximum amount allowed by Telegram: 48K)

### _Example_
``` python
...
pytgcalls.join_group_call(-1001185324811, '/home/user/Laky64/annoying_dog.raw', 48000)
...
```
> ### Warning!
> Use this function after initializing the NodeJS core

## leave_group_call
Leave a group call

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
...
pytgcalls.leave_group_call(-1001185324811)
...
```
> ### Warning!
> Use this function after initializing the NodeJS core

## change_volume_call
Set the audio stream volume

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
volume | Integer | Volume of stream (0-200)

### _Example_
``` python
...
pytgcalls.change_volume_call(-1001185324811, 100)
...
```

> ### Warning!
> Use this function after initializing the NodeJS core and this function have some bugs

## pause_stream
Pause the audio stream 

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
...
pytgcalls.pause_stream(-1001185324811)
...
```

> ### Warning!
> Use this function after initializing the NodeJS core

## resume_stream
Resume the audio stream

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
...
pytgcalls.resume_stream(-1001185324811)
...
```

> ### Warning!
> Use this function after initializing the NodeJS core

## change_stream
Change audio stream without reconnection

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
file_path | String | Path of a RAW audio file

### _Example_
``` python
...
pytgcalls.change_stream(-1001185324811, '/home/user/Laky64/annoying_dog.raw')
...
```
> ### Warning!
> Use this function after initializing the NodeJS core

## calls
Get list of all joined voice chat

### _Example_
``` python
...
print(pytgcalls.calls)
...
```

## active_calls
Get dict of all playing voice chat

### _Example_
``` python
...
print(pytgcalls.active_calls)
...
```

## get_cache_id
Return current UserID

### _Example_
``` python
...
print(pytgcalls.get_cache_id())
...
```

## get_port_server
Get the current internal local port

### _Example_
``` python
...
print(pytgcalls.get_port_server())
...
```

## run
Start PyTgCalls with the provided Pyrogram Client

Field | Type | Description
--- | --- | ---
before_start_callable | Callable | Callable decorator

### _Example_
``` python
...
pytgcalls.run(handler)

def handler(my_id: int):
   print(my_id)
...
```

## on_raw_update
Decorator handling all information about status of calls and stream

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
...
@pytgcalls.on_raw_update()
async def handler(update: dict):
    print(update)
...
```

## on_stream_end
Decorator handling when stream ends

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
...
@pytgcalls.on_stream_end()
async def handler(chat_id: int):
    print(chat_id)
...
```

## on_group_call_invite
Decorator handling when receive invite to Group Call

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
...
@pytgcalls.on_group_call_invite()
async def handler(client: Client, update: MessageService):
    print(update)
...
```

## on_custom_api 
Decorator handling custom api, this need a dict return

Call Api with
```
http://127.0.0.1:{YOUR_PORT(Default is 24859)}/api
```
_Need Post request!_

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
...
@pytgcalls.on_custom_api()
async def handler(request: dict):
    return {'result': 'OK'}
...
```

## on_kicked
Decorator handling when kicked from group

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
...
@pytgcalls.on_kicked()
async def handler(chat_id: int):
    print(chat_id)
...
```

# Exceptions

## JS_CORE_NOT_RUNNING
This error occurs when trying to execute a function before JS Core starts

## PYROGRAM_CLIENT_IS_NOT_RUNNING
This error occurs when trying to execute a function without initializing Pyrogram Client

## JOIN_ERROR
This error occurs when trying to execute a join_group_call without active group call

## NOT_IN_GROUP
This error occurs when trying to execute is_playing without an active group call

## NEED_PYROGRAM_CLIENT
This error occurs when trying to execute run without Pyrogram Client
