"""
✘ Commands Available
• `{i}scan`
    **How To Use**: Reply To Any File.
    **Function : **Get information from virustotal, scan any telegram file. plugin by @Deonnn.
"""

from telethon.errors.rpcerrorlist import YouBlockedUserError
from . import *

@ultroid_cmd(pattern="scan ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eor(event, "Reply to any user's media message.")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await eor(event, "reply to media file")
        return
    chat = "@VirusTotalAV_bot"
    if reply_message.sender.bot:
        await event.edit("Reply to actual users message.")
        return
    ult = await eor(event, "Scanning this file in private...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=1356559037))
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await ult.edit("unblock @VirusTotalAV_bot and try again")
            return
        if response.text.startswith("🚀 File Initiated"):
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1356559037)
            )
            response = await response
            msg = response.message.message
            await ult.edit(msg)
        else:
            await ult.edit("sorry, something went wrong")

        await event.client.send_read_acknowledge(conv.chat_id)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
