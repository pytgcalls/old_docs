# PyTgCalls API
> PyTgCalls is based on PyServerCall and [TgCallsJS](https://github.com/tgcallsjs/tgcalls)
> to work with Telegram group calls.

# Recent changes
> ## Update of 07/09/2021 - 0.8.0
> - Fixed AntiFlood cache not working
> - Added Telethon Support
> - Added support for join in groups and channel
> - Added Video Group Calls support
> - Added Audio/Video syncer
> - Added idle function
> - Fixed Binding
> - Some bugs fix
> - Added FIFO support

> ## Update of 26/08/2021 - 0.7.3
> - Custom Api now is Async!
> - Fixed Async Lock problems
> - Now resume_stream and pause_stream return the result of operation with bool
> - JS code cleaned

> ## Update of 23/08/2021 - 0.7.2
> - Added on_left (Called when your userbot left the group)
> - Some bugs fix

> ## Update of 20/08/2021 - 0.7.0
> - PyTgCalls Re-Base
> - Fully Async
> - Removed internal server and replaced with stdin and stdout
> - CustomAPI renewed to 2.1
> - RawUpdate renewed with PyTgCalls Object Update
> - Added custom exceptions
> - .run() is now .start()
> - Now the logs have all gone to Logging
> - Added if the stream is deleted, the userbot will exit the voice call by printing an error in RawUpdate
> - Windows Support
> - macOS support
> - Linux Arm64 support
> - Bug Fix

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
app | pyrogram.Client or telethon.TelegramClient | A MtProto client
cache_duration (Optional) | Integer | The duration of get_full_chat cache (In seconds)

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
stream_audio | types.input_stream.InputAudioStream | Audio File Descriptor
stream_video (Optional) | types.input_stream.InputVideoStream | Video File Descriptor
invite_hash (Optional) | String | Telegram invite voice chat hash
bitrate (Optional) | Integer | Audio stream bitrate (maximum amount allowed by Telegram: 48K)
join_as (Optional) | pyrogram.raw.base.InputPeer or telethon.tl.types.InputTypePeer | InputPeer of join as channel or profile
stream_type (Optional) | pytgcalls.StreamType | The type of Stream

### _Example_
``` python
...
# AVAILABLE ASYNC AND SYNC
pytgcalls.join_group_call(
    -1001185324811,
    InputAudioStream(
        '/home/user/Laky64/annoying_dog.raw',
    ),
    48000,
    pytgcalls.cache_peer,
    StreamType().local_stream,
)
...
```

## leave_group_call
Leave a group call

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
...
# AVAILABLE ASYNC AND SYNC
pytgcalls.leave_group_call(-1001185324811)
...
```

## change_volume_call
Set the audio stream volume

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
volume | Integer | Volume of stream (0-200)

### _Example_
``` python
...
# AVAILABLE ASYNC AND SYNC
pytgcalls.change_volume_call(-1001185324811, 100)
...
```

> ### Warning!
> This function has some Telegram bugs

## pause_stream
Pause the audio stream 

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
...
# AVAILABLE ASYNC AND SYNC
pytgcalls.pause_stream(-1001185324811)
...
```

## resume_stream
Resume the audio stream

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
...
# AVAILABLE ASYNC AND SYNC
pytgcalls.resume_stream(-1001185324811)
...
```

## change_stream
Change audio stream without reconnection

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
stream_audio | types.input_stream.InputAudioStream | Audio File Descriptor
stream_video (Optional) | types.input_stream.InputVideoStream | Video File Descriptor

### _Example_
``` python
...
# AVAILABLE ASYNC AND SYNC
pytgcalls.change_stream(
    -1001185324811,
    InputAudioStream(
        '/home/user/Laky64/annoying_dog.raw',
    ),
)
...
```

## calls
Get GroupCall list of all joined voice chat

### _Example_
``` python
...
print(pytgcalls.calls)
...
```

## active_calls
Get GroupCall list of all playing voice chat

### _Example_
``` python
...
print(pytgcalls.active_calls)
...
```

## get_active_call
Get GroupCall of playing voice chat

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
...
print(pytgcalls.get_active_call(-1001185324811))
...
```

## get_call
Get GroupCall of joined voice chat

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
...
print(pytgcalls.get_call(-1001185324811))
...
```

## cache_peer
Return current InputPeer

### _Example_
``` python
...
print(pytgcalls.cache_peer)
...
```

## start
Start PyTgCalls with the provided MtProto Client

### _Example_
``` python
...
# AVAILABLE ASYNC AND SYNC
pytgcalls.start()
...
```

## is_connected
Check if running py-tgcalls Client

### _Example_
``` python
...
pytgcalls.is_connected
...
```

## idle
Idle your python file in async way

### _Example_
``` python
...
from pytgcalls import idle
...
# AVAILABLE ASYNC AND SYNC
idle()
...
```

## live_stream
Set the stream mode to live stream, use this for livestream or ffmpeg live conversion

### _Example_
``` python
...
StreamType().live_stream
...
```

## local_stream
Set the stream mode to local stream, use this for local converted file 

### _Example_
``` python
...
StreamType().local_stream
...
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
...
StreamType().pulse_stream
...
```

## get_max_voice_chat
Get the max voice chat can start your server

Field | Type | Description
--- | --- | ---
consumption | Integer | Estimated Cpu Consumption(Optional)

### _Example_
``` python
...
PyTgCalls.get_max_voice_chat()
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
from pytgcalls.types import Update
...
@pytgcalls.on_raw_update()
async def handler(client: PyTgCalls, update: Update):
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
async def handler(client: PyTgCalls, update: Update):
    print(update)
...
```

## on_group_call_invite
Decorator handling when receiving an invitation to the group call

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
...
@pytgcalls.on_group_call_invite()
async def handler(client: PyTgCalls, update: MessageService):
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
port | Integer | CustomAPI server port

### _Example_
``` python
...
custom_api = CustomApi()
...
@custom_api.on_update_custom_api()
async def handler(request: dict):
    return {'result': 'OK'}
...
custom_api.start()
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
...
@pytgcalls.on_kicked()
async def handler(client: PyTgCalls, chat_id: int):
    print(chat_id)
...
```

## on_left
Decorator handling when left the group

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
...
@pytgcalls.on_left()
async def handler(client: PyTgCalls, chat_id: int):
    print(chat_id)
...
```

## on_closed_voice_chat
Decorator handling when closed voice chat

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
...
@pytgcalls.on_closed_voice_chat()
async def handler(client: PyTgCalls, chat_id: int):
    print(chat_id)
...
```

# Types
## types.Update
A raw update from on_raw_update

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## types.groups.ErrorDuringJoin
Error during joining to voice chat from on_raw_update

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## types.groups.JoinedVoiceChat
Joined to voice chat from on_raw_update

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## types.groups.LeftVoiceChat
Left to voice chat from on_raw_update

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## types.stream.ChangedStream
Changed stream from on_raw_update

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## types.stream.ChangedStream
Changed stream from on_raw_update

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## types.stream.PausedStream
Paused stream from on_raw_update

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## types.stream.ResumedStream
Paused stream from on_raw_update

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## types.stream.StreamDeleted
Deleted stream during playing from on_raw_update

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## types.stream.StreamAudioEnded
Ended audio stream, raised from on_stream_end

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## types.stream.StreamVideoEnded
Ended video stream, raised from on_stream_end

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## types.groups.GroupCall
GroupCall from active_calls, calls, get_active_call and get_call

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
status | types.groups.Status | Status of streaming

## types.groups.Status
Status from types.groups.GroupCall

## types.groups.PlayingStream
Status from types.groups.GroupCall

## types.groups.PausedStream
Status from types.groups.GroupCall

## types.groups.NotPlayingStream
Status from types.groups.GroupCall

## types.input_stream.InputAudioStream
Input Audio Stream Descriptor of JoinGroupCall and ChangeStream

Field | Type | Description
--- | --- | ---
path | String | Raw Audio File Path
parameters (Optional) | types.input_stream.AudioParameters | Audio parameters

## types.input_stream.InputVideoStream
Input Video Stream Descriptor of JoinGroupCall and ChangeStream

Field | Type | Description
--- | --- | ---
path | String | Raw Video File Path
parameters (Optional) | types.input_stream.VideoParameters | Video parameters

## types.input_stream.AudioParameters
Video parameters of InputAudioStream

Field | Type | Description
--- | --- | ---
bitrate (Optional) | Integer | Audio bitrate

## types.input_stream.VideoParameters
Video parameters of InputVideoStream

Field | Type | Description
--- | --- | ---
width | Integer | Video width
height | Integer | Video height
frame_rate | Integer | Video frame rate


# Exceptions

## exceptions.NodeJSNotInstalled
Node.js isn't installed, raised from start

## exceptions.TooOldNodeJSVersion
Node.js version is too old, raised from start

## exceptions.TooOldPyrogramVersion
Pyrogram version is too old, raised from start

## exceptions.TooOldTelethonVersion
Telethon version is too old, raised from start

## exceptions.InvalidMtProtoClient
You set an invalid MtProto client

## exceptions.PyTgCallsAlreadyRunning
PyTgCalls client is already running, raised from start

## exceptions.InvalidStreamMode
The stream mode is invalid, raised from change_stream and join_group_call

## exceptions.NoMtProtoClientSet
An MtProto client not set, raised from join_group_call, leave_group_call, change_volume_call, change_stream, pause_stream, resume_stream

## exceptions.NodeJSNotRunning
NodeJS core not running, do start before call these methods, raised from join_group_call, leave_group_call, change_volume_call, change_stream, pause_stream, resume_stream

## exceptions.NoActiveGroupCall
No active group call found, raised from join_group_call, leave_group_call, change_volume_call

## exceptions.WaitPreviousPingRequest
Wait previous ping request before new request, raised from ping

## exceptions.TooManyCustomApiDecorators
Too Many Custom Api Decorators, raised from on_update_custom_api

## exceptions.GroupCallNotFound
Group call not found, raised from get_active_call and get_call

[how to use it]: https://github.com/pytgcalls/pytgcalls/tree/master/example/custom_api