---
title: PyTgCalls documentation
description: Async client API for the Telegram Group Calls
image: https://avatars.githubusercontent.com/u/75855609
---
# PyTgCalls API
> PyTgCalls is based on PyServerCall, [TgCallsJS](https://github.com/tgcallsjs/tgcalls),
> [SocketIO](https://socket.io/) and [WebRTC](https://webrtc.org/)
> for developers keen on building bots for Telegram.

# Recent changes
> ## Update of 22/02/2021
> Added support for bitrate regulation

> ## Update of 13/02/2021
> Added support to Layer 123

# Audio Needed
This is audio type needed

Field | Value
--- | ---
acodec | pcm_s16le
bitrate | Your bitrate preference

# Methods
Here are all the methods available to make requests to PyTgCalls

## join_group_call
Join to group call with audio source

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of Group
file_path | String | File path of RAW Stream Audio
bitrate | Integer | Audio stream bitrate (Max 48K Allowed by Telegram)

## leave_group_call
Leave group call

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of Group

## change_volume_call
Change volume of audio stream by changing personal volume

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of Group
volume | Integer | Volume of stream (0-200)


## pause_stream
Set pause mode audio stream by sending void packets

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of Group

## resume_stream
Set resume mode audio stream by resuming stream reading

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of Group

## change_stream
Change audio stream without reconnection

Field | Type | Description
--- | --- | ---
chat_id | Integer | Chat ID of Group
file_path | String | File path of RAW Stream Audio

## get_cache_id
Return current UserID

## run
Start running Pyrogram and PyTgCalls Session

Field | Type | Description
--- | --- | ---
app | pyrogram.Client | Pyrogram Client Class initialized

## on_event_update
Decorator handling all information about status of calls and stream

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator

## on_stream_end
Decorator handling when stream ends

Field | Type | Description
--- | --- | ---
func | Callable | Callable decorator