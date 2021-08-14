# PyTgCalls API
> PyTgCalls is based on PyServerCall, [TgCallsJS](https://github.com/tgcallsjs/tgcalls),
> [SocketIO](https://socket.io/) and [WebRTC](https://webrtc.org/)
> to work with Telegram group calls.

# Recent changes
> ## Update of 10/08/2021 - 0.6.1
> - Added self to handlers
> - Some fix

> ## Update of 10/08/2021 - 0.6.0
> - Added multiple instance support
> - Added possibility to call functions without waiting for NodeJS Core
> - Added remote check version available
> - CustomAPI 2.0
> - Security Fix
> - Code Cleaned

> ## Update of 30/03/2021 - 0.4.6
> - Added type pulse_stream beta 
> - Added the possibility to get max voice chat can start your server

> ## Update of 25/03/2021 - 0.4.2
> - Added support for JoinGroupCall with invite hash

> ## Update of 21/03/2021 - 0.4.1
> - Customizable cache time of get_full_chat
> - Updated all libs to the latest version


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
client | pyrogram.Client | A Pyrogram client
port (Optional) | Integer | Port to run local server 
log_mode (Optional) | PyLogs | Debug mode
flood_wait_cache (Optional) | Integer | Cache anti-floodwait duration(In seconds)

### _Example_
``` python
client = Client("My_Session")
pytgcalls = PyTgCalls(client, log_mode=PyLogs.verbose)
```

## PyLogs.verbose
Set the logging to normal mode

### _Example_
``` python
PyLogs.verbose
```

## PyLogs.ultra_verbose
Set the logging to normal mode

### _Example_
``` python
PyLogs.ultra_verbose
```


## join_group_call
Join a group call to stream a file

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
file_path | String | Path of a RAW audio file
invite_hash (Optional) | String | Telegram invite voice chat hash
bitrate (Optional) | Integer | Audio stream bitrate (maximum amount allowed by Telegram: 48K)
join_as (Optional) | pyrogram.raw.base.InputPeer | InputPeer of join as channel or profile
stream_type (Optional) | pytgcalls.StreamType | The type of Stream

### _Example_
``` python
pytgcalls.join_group_call(
    -1001234567890,
    '/home/PyTgCalls/PyTgCalls/input.raw',
    48000,
    pytgcalls.get_cache_peer(),
    StreamType().pulse_stream,
)
```

## leave_group_call
Leave a group call

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
pytgcalls.leave_group_call(-1001234567890)
```

## change_volume_call
Set the audio stream volume

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
volume | Integer | Volume of stream (0-200)

### _Example_
``` python
pytgcalls.change_volume_call(-1001234567890, 100)
```

> ### Warning!
> This function have some Telegram bugs

## pause_stream
Pause the audio stream 

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
pytgcalls.pause_stream(-1001234567890)
```

## resume_stream
Resume the audio stream

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
pytgcalls.resume_stream(-1001234567890)
```

## change_stream
Change audio stream without reconnection

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
file_path | String | Path of a RAW audio file

### _Example_
``` python
pytgcalls.change_stream(-1001234567890, '/home/PyTgCalls/PyTgCalls/input.raw')
```

## calls
Get list of all joined voice chat

### _Example_
``` python
print(pytgcalls.calls)
```

## active_calls
Get dict of all playing voice chat

### _Example_
``` python
print(pytgcalls.active_calls)
```

## get_cache_id
Return current UserID

### _Example_
``` python
print(pytgcalls.get_cache_id())
```

## get_cache_peer
Return current InputPeer

### _Example_
``` python
print(pytgcalls.get_cache_peer())
```

## get_port_server
Get the current internal local port

### _Example_
``` python
print(pytgcalls.get_port_server())
```

## run
Start PyTgCalls with the provided Pyrogram Client

Field | Type | Description
--- | --- | ---
before_start_callable | Callable | Callable decorator

### _Example_
``` python
pytgcalls.run(handler)

def handler(my_id: int):
   print(my_id)
```

## live_stream
Set the stream mode to live stream, use this for livestream or ffmpeg live conversion

### _Example_
``` python
StreamType().live_stream
```

## local_stream
Set the stream mode to local stream, use this for local converted file 

### _Example_
``` python
StreamType().local_stream
```

## pulse_stream
Set the stream mode to pulse stream but is very 
different between the other streaming mode

### Example of other streaming mode

111011100110100100<br>
111011100110100100<br>
111011100110100100<br>
111011100110100100<br>
111011100110100100<br>
111011100110100100<br>


### Pulse Stream Mode:
111011100110100100<br>
111011100110100100<br>
111011100110100100<br>

111011100110100100<br>
111011100110100100<br>
111011100110100100<br>

### Supported streams:
- Live Streams
- Local Stream

### _Example_
``` python
StreamType().pulse_stream
```

## get_max_voice_chat
Get the max voice chat can start your server

Field | Type | Description
--- | --- | ---
consumption | Integer | Estimated Cpu Consumption(Optional)

### _Example_
``` python
PyTgCalls.get_max_voice_chat()
```

## on_raw_update
Decorator handling all information about status of calls and stream

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
@pytgcalls.on_raw_update()
async def handler(client: PyTgCalls, update: dict):
    print(update)
```

## on_stream_end
Decorator handling when stream ends

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
@pytgcalls.on_stream_end()
async def handler(client: PyTgCalls, chat_id: int):
    print(chat_id)
```

## on_group_call_invite
Decorator handling when receive invite to Group Call

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
@pytgcalls.on_group_call_invite()
async def handler(client: PyTgCalls, client: Client, update: MessageService):
    print(update)
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
custom_api = CustomAPI()
@custom_api.on_update_custom_api()
async def handler(request: dict):
    if "action" in request:
        if request["action"] == "JOIN_CALL":
            call.join_group_call(
                chat_id=request["CHAT_ID"],
                file_path=request["INPUT_FILE"],
                bitrate=48000,
                stream_type=StreamType().pulse_stream,
            )
    return request
```
> ### More Information
> There is a more detailed example about [how to use it]


## on_kicked
Decorator handling when kicked from group

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
@pytgcalls.on_kicked()
async def handler(client: PyTgCalls, chat_id: int):
    print(chat_id)
```

## on_closed_voice_chat
Decorator handling when closed voice chat

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
@pytgcalls.on_closed_voice_chat()
async def handler(client: PyTgCalls, chat_id: int):
    print(chat_id)
```

# Exceptions

## JS_CORE_NOT_RUNNING (DEPRECATED)
This error occurs when trying to execute a function before JS Core starts

## PYROGRAM_CLIENT_IS_NOT_RUNNING
This error occurs when trying to execute a function without initializing Pyrogram Client

## JOIN_ERROR
This error occurs when trying to execute a join_group_call without active group call

## NOT_IN_GROUP
This error occurs when trying to execute is_playing without an active group call

## NEED_PYROGRAM_CLIENT
This error occurs when trying to execute run without Pyrogram Client

## JOIN_VOICE_CALL_ERROR
This error occurs when trying to join and pyrogram error occurs

## INVALID_STREAM_MODE
This error occurs when trying to set an invalid StreamType

## FILE_NOT_FOUND
This error occurs when trying play not existing file

## INVALID_FILE_STREAM
This error occurs when trying play 0 byte length file

[how to use it]: https://github.com/pytgcalls/pytgcalls/tree/master/example/custom_api
