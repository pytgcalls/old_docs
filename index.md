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
> ## Update of 24/02/2021
> Added debug mode

> ## Update of 23/02/2021
> Added kick listener

> ## Update of 22/02/2021
> Added support for bitrate regulation

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
port | Integer | Port to run local server
log_mode | Boolean | Debug mode

## join_group_call
Join a group call to stream a file

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
file_path | String | Path of a RAW audio file
bitrate | Integer | Audio stream bitrate (maximum amount allowed by Telegram: 48K)

## leave_group_call
Leave a group call

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## change_volume_call
Set the audio stream volume

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
volume | Integer | Volume of stream (0-200)


## pause_stream
Pause the audio stream 

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## resume_stream
Resume the audio stream

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup

## change_stream
Change audio stream without reconnection

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of a supergroup
file_path | String | Path of a RAW audio file

## get_cache_id
Return current UserID

## get_active_voice_chats
Get a list of current active voice chat

## get_port_server
Get the current internal local port

## run
Start PyTgCalls with the provided Pyrogram Client

Field | Type | Description
--- | --- | ---
app | pyrogram.Client | A Pyrogram client
before_start_callable | Callable | Callable decorator

## on_event_update
Decorator handling all information about status of calls and stream

Field | Type | Description
--- | --- | ---
update | Dict | Update Result
func | Callable | Callable decorator

## on_stream_end
Decorator handling when stream ends

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

## on_custom_api 
Decorator handling custom api, this need a dict return

Call Api with
```
http://127.0.0.1:{YOUR_PORT(Default is 24859)}/api
```
_Need Post request!_

Field | Type | Description
--- | --- | ---
update | Dict | Update Result
func | Callable | Callable decorator


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
