# PyTgCalls API
> PyTgCalls is based on PyServerCall and [TgCallsJS](https://github.com/tgcallsjs/tgcalls)
> to work with Telegram group calls.

# Recent changes

> ## Update of 10/11/2021 - 0.8.1
> - Added all proportion video support
> - Fixed stderr overflow (Added reader)
> - PyTgCalls logging named
> - Added internal ffmpeg conversion (AudioPiped, AudioVideoPiped, AudioImagePiped)
> - Added remote stream support
> - Added Multi-Core support (Beta)
> - Added possibility to stream image with audio (AudioImagePiped)
> - Added GetParticipants and OnParticipantChange
> - Added support of \_\_str__ also for Python List
> - Added retry if WRTC connection fail
> - Added Browser Constants
> - Buffer Reader now is lighter
> - Added Python3.10 Support
> - Now support multi ping request

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
overload_quiet_mode (Optional) | Boolean | Disable the overload warning messages
multi_thread (Optional) | Boolean | Enable multi thread (Beta) for pytgcalls

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
stream | types.input_stream.InputStream | Streams Descriptor
invite_hash (Optional) | String | Telegram invite voice chat hash
join_as (Optional) | pyrogram.raw.base.InputPeer or telethon.tl.types.InputTypePeer | InputPeer of join as channel or profile
stream_type (Optional) | pytgcalls.StreamType | The type of Stream

### _Example_
``` python
...
# AVAILABLE ASYNC AND SYNC

# Legacy Audio support only Raw Format
pytgcalls.join_group_call(
    -1001185324811,
    InputStream(
        InputAudioStream(
            '/home/user/Laky64/annoying_dog.raw',
            AudioParameters(
                48000,
            ),
        ),
    ),
    pytgcalls.cache_peer,
    StreamType().pulse_stream,
)

# High Level Audio support all format supported by ffmpeg
pytgcalls.join_group_call(
    -1001185324811,
    AudioPiped(
        '/home/user/Laky64/annoying_dog.mp3',
        AudioParameters(
            48000,
        ),
    ),
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

# Legacy Audio support only Raw Format
pytgcalls.change_stream(
    -1001185324811,
    InputStream(
        InputAudioStream(
            '/home/user/Laky64/annoying_dog.raw',
        ),
    ),
)

# High Level Audio support all format supported by ffmpeg
pytgcalls.change_stream(
    -1001185324811,
    AudioPiped(
        '/home/user/Laky64/annoying_dog.mp3',
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

## get_participants
Get GroupCall of joined voice chat

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

### _Example_
``` python
...
print(pytgcalls.get_participants(-1001185324811))
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

> ### Warning!
> This decorator can be called twice (if you are using audio and video), 
> because it will be raised when the video ends and the audio too

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

# AVAILABLE ASYNC AND SYNC
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

## on_participants_change
Decorator handling when participants list was changed

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

### _Example_
``` python
...
@pytgcalls.on_participants_change()
async def handler(client: PyTgCalls, update: Update):
    print(update)
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
status | String | Status of streaming
is_playing | Boolean | Status of playing

## types.groups.GroupCallParticipant
GroupCallParticipant from get_participants and on_participants_change

Field | Type | Description
--- | --- | ---
user_id | Integer | User ID
muted | Boolean | If is muted
muted_by_admin | Boolean | If was muted by admin
video | Boolean | If is sharing a video
screen_sharing | Boolean | If is sharing the screen
video_camera | Boolean | If is sharing the camera
raised_hand | Boolean | If have raised the hand
volume | Integer | User volume by admin

## types.input_stream.InputStream
Input Stream Descriptor of JoinGroupCall and ChangeStream

Field | Type | Description
--- | --- | ---
path | String | Raw Audio File Path
stream_audio (Optional) | types.input_stream.InputAudioStream | Audio File Descriptor
stream_video (Optional) | types.input_stream.InputVideoStream | Video File Descriptor
lip_sync (Optional) | Boolean | Enable/Disable the Lip Sync

## types.input_stream.InputAudioStream
Input Audio Stream Descriptor of InputStream

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

## exceptions.TooManyCustomApiDecorators
Too Many Custom Api Decorators, raised from on_update_custom_api

## exceptions.GroupCallNotFound
Group call not found, raised from get_active_call and get_call

[how to use it]: https://github.com/pytgcalls/pytgcalls/tree/master/example/custom_api