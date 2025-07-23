# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.sts import STS
from database import db
from script import Script
import asyncio

@Client.on_message(filters.command("private_forward") & filters.private)
async def private_forward_cmd(client, message: Message):
    user_id = message.from_user.id

    # Check for userbot session
    userbot = await db.get_userbot(user_id)
    if not userbot:
        return await message.reply("❌ You have not added a user session yet.\n\nGo to /settings → Bots → ✚ Add User bot ✚")

    # Must be replying to a forwarded message from private chat
    if not message.reply_to_message or not message.reply_to_message.forward_from_chat:
        return await message.reply("❌ Please reply to a forwarded message from a private source chat.")

    source_chat = message.reply_to_message.forward_from_chat.id

    # Get target channels
    targets = await db.get_user_channels(user_id)
    if not targets:
        return await message.reply("❌ No target channels added. Go to /settings → Channels → ✚ Add Channel ✚")

    # Use STS to store status
    sts = STS(user_id)
    sts.store(From=source_chat, to=targets, skip=0, limit=0)

    status_msg = await message.reply(Script.PROCESSING_TEXT)

    try:
        async for msg in client.iter_messages(source_chat, reverse=True):
            if not msg.media:
                continue

            for target in targets:
                try:
                    await client.copy_message(
                        chat_id=target['chat_id'],
                        from_chat_id=source_chat,
                        message_id=msg.id
                    )
                    await asyncio.sleep(0.5)
                except Exception as e:
                    print(f"Forward error to {target['chat_id']}: {e}")
                    continue

    except Exception as e:
        return await status_msg.edit(f"❌ Failed while forwarding: {e}")

    await status_msg.edit(Script.DONE_TEXT)
