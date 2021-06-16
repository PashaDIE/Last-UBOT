"""
tgvc-userbot, Telegram Voice Chat Userbot
Copyright (C) 2021  Dash Eclipse

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Record Audio from Telegram Voice Chat

Dependencies:
- ffmpeg
- opus-tools
- bpm-tools

Requirements (pip):
- ffmpeg-python

Start the userbot and send !record to a voice chat
enabled group chat to start recording for 30 seconds
"""
import asyncio
import os
import subprocess
from datetime import datetime

# noinspection PyPackageRequirements
import ffmpeg
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import GroupCall, GroupCallAction

group_call = GroupCall(None, path_to_log_file='')


@Client.on_message(filters.group
                   & filters.text
                   & filters.outgoing
                   & ~filters.edited
                   & filters.regex("^!record$"))
async def record_from_voice_chat(client, m: Message):
    group_call.client = client
    await group_call.start(m.chat.id)
    group_call.add_handler(
        network_status_changed_handler,
        GroupCallAction.NETWORK_STATUS_CHANGED
    )
    await m.delete()


async def network_status_changed_handler(gc: GroupCall, is_connected: bool):
    if is_connected:
        print("- JOINED VC")
        await record_and_send_opus()
        await gc.stop()
    else:
        print("- LEFT VC")


async def record_and_send_opus():
    client = group_call.client
    chat_id = int("-100" + str(group_call.full_chat.id))
    chat = await client.get_chat(chat_id)
    status = await client.send_message(chat_id, "1/3 Recording...")
    utcnow_unix, utcnow_readable = await get_utcnow()
    record_raw, record_opus = f"{utcnow_unix}.raw", f"{utcnow_unix}.opus"
    group_call.output_filename = record_raw
    await asyncio.sleep(30)
    group_call.output_filename = ''
    await status.edit_text("2/3 Transcoding...")
    ffmpeg.input(
        record_raw,
        format='s16le',
        acodec='pcm_s16le',
        ac=2,
        ar='48k',
        loglevel='error'
    ).output(record_opus).overwrite_output().run()
    duration = int(float(ffmpeg.probe(record_opus)['format']['duration']))
    bpm = subprocess.getoutput(
        f"opusdec --quiet --rate 48000 --float {record_opus} - "
        "| bpm -f '%0.0f'"
    )
    probe = ffmpeg.probe(record_opus, pretty=None)
    caption = (
        f"- BPM: `{bpm}`\n"
        f"- Format: `{probe['streams'][0]['codec_name']}`\n"
        f"- Channel(s): `{str(probe['streams'][0]['channels'])}`\n"
        f"- Sampling rate: `{probe['streams'][0]['sample_rate']}`\n"
        f"- Bit rate: `{probe['format']['bit_rate']}`\n"
        f"- File size: `{probe['format']['size']}`"
    )
    performer = (
        f"@{chat.username}" if chat.username
        else chat.title
    )
    title = f"[VCREC] {utcnow_readable}"
    thumb = await client.download_media(chat.photo.big_file_id)
    await status.edit_text("3/3 Uploading...")
    await client.send_audio(
        chat_id,
        record_opus,
        caption=caption,
        duration=duration,
        performer=performer,
        title=title,
        thumb=thumb)
    await status.delete()
    for f in (record_raw, record_opus, thumb):
        os.remove(f)


async def get_utcnow():
    utcnow = datetime.utcnow()
    utcnow_unix = utcnow.strftime('%s')
    utcnow_readable = utcnow.strftime('%Y-%m-%d %H:%M:%S')
    return utcnow_unix, utcnow_readable
