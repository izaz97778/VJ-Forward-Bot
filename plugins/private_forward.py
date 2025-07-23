# plugins/private_forward.py

from pyrogram import Client, filters
from pyrogram.types import Message
from database import db
from utils import STS, get_configs, check_filters, progress_for_pyrogram
from script import Script
from . import CLIENT  # Userbot client

import asyncio

@Client.on_message(filters.command("private_forward") & filters.private)
async def private_forward_cmd(bot: Client, msg: Message):
    user_id = msg.from_user.id
    sts = STS(user_id)

    # ask for source chat
    ask_src = await msg.reply_text("<b>🔍 Send source chat ID or forward a message from it</b>\n/cancel to stop")
    try:
        src = await bot.ask(user_id, timeout=60)
    except:
        return await ask_src.edit("⏰ Timed out.")
    if src.text == "/cancel":
        return await ask_src.edit("❌ Process canceled.")

    if src.forward_from_chat:
        from_chat = src.forward_from_chat.id
    elif src.text.lstrip("-").isdigit():
        from_chat = int(src.text)
    else:
        return await ask_src.edit("❌ Invalid source chat ID.")

    # ask for destination
    ask_dest = await msg.reply_text("<b>📤 Send target chat ID or forward from destination</b>\n/cancel to stop")
    try:
        dst = await bot.ask(user_id, timeout=60)
    except:
        return await ask_dest.edit("⏰ Timed out.")
    if dst.text == "/cancel":
        return await ask_dest.edit("❌ Process canceled.")

    if dst.forward_from_chat:
        to_chat = dst.forward_from_chat.id
    elif dst.text.lstrip("-").isdigit():
        to_chat = int(dst.text)
    else:
        return await ask_dest.edit("❌ Invalid destination chat ID.")

    # ask for limit (optional)
    await msg.reply("➕ Send how many messages to forward (default 1000)\n/cancel to stop")
    try:
        limit_msg = await bot.ask(user_id, timeout=60)
    except:
        return await msg.reply("⏰ Timed out.")
    if limit_msg.text == "/cancel":
        return await msg.reply("❌ Process canceled.")
    try:
        limit = int(limit_msg.text)
    except:
        limit = 1000

    skip = 0
    await msg.reply("✅ Starting... Use /cancel to stop anytime.")

    # Store session
    sts.store(from_chat, to_chat, skip, limit)
    configs = await get_configs(user_id)

    total, done = 0, 0
    async for message in CLIENT.iter_messages(from_chat, limit=limit):
        if not sts.verify():
            return await msg.reply("⛔ Forward canceled.")

        total += 1
        if skip and total <= skip:
            continue

        # Apply filters
        if not await check_filters(message, configs):
            continue

        try:
            await CLIENT.copy_message(
                chat_id=to_chat,
                from_chat_id=from_chat,
                message_id=message.id
            )
            done += 1
            await progress_for_pyrogram(f"✅ Forwarding...\nTotal: {total}\nDone: {done}",
                                        msg)
        except Exception as e:
            await msg.reply(f"❌ Error forwarding message ID {message.id}\n{e}")

    await msg.reply(f"✅ Done!\nTotal: {total}\nForwarded: {done}")
    sts.clear()
