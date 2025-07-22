import os
from config import Config

class Script(object):
    START_TXT = """<b>ʜɪ {}

ɪ'ᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ
ɪ ᴄᴀɴ ꜰᴏʀᴡᴀʀᴅ ᴀʟʟ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟ</b>

**ᴄʟɪᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ**"""
    
    HELP_TXT = """<b><u>🔆 Help</u></b>

<b><u>📚 Available commands:</u></b>
⏣ /start - check I'm alive
⏣ /forward - forward messages
⏣ /settings - configure your settings
⏣ /unequify - delete duplicate media messages in chats
⏣ /stop - stop your ongoing tasks
⏣ /reset - reset your settings

<b><u>💢 Features:</u></b>
► Forward message from public channel to your channel without admin permission. 
If the channel is private, admin permission is needed. 
If you can't give admin permission, then use userbot, but in userbot there is a chance to get your account banned, so use a fake account.
► Custom caption
► Custom button
► Skip duplicate messages
► Filter type of messages
"""
    
    HOW_USE_TXT = """<b><u>⚠️ Before Forwarding:</u></b>
► Add a bot or userbot
► Add at least one to channel (your bot/userbot must be admin there)
► You can add chats or bots by using /settings
► If the **From Channel** is private, your userbot must be a member there or your bot must have admin permission
► Then use /forward to forward messages

► ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ [ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ]()"""
    
    ABOUT_TXT = """<b>
╔════❰ ғᴏʀᴡᴀʀᴅ ʙᴏᴛ ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃 ʙᴏᴛ : [Forward Bot]()
║┣⪼👦 Cʀᴇᴀᴛᴏʀ : [King VJ 👑]()
║┣⪼🤖 Uᴘᴅᴀᴛᴇ : [VJ Botz]()
║┣⪼📡 Hᴏsᴛᴇᴅ ᴏɴ : Super Fast
║┣⪼🗣️ Lᴀɴɢᴜᴀɢᴇ : Python 3
║┣⪼📚 Lɪʙʀᴀʀʏ : Pyrogram Gather 2.11.0 
║┣⪼🗒️ Vᴇʀsɪᴏɴ : 0.18.3
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
</b>"""
    
    STATUS_TXT = """
╔════❰ ʙᴏᴛ sᴛᴀᴛᴜs ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼⏳ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ: `{}`
║┃
║┣⪼👱 Tᴏᴛᴀʟ Usᴇʀs: `{}`
║┃
║┣⪼🤖 Tᴏᴛᴀʟ Bᴏᴛs: `{}`
║┃
║┣⪼🔃 Fᴏʀᴡᴀʀᴅɪɴɢs: `{}`
║┃
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
"""
    
    FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"
    TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"
    SKIP_MSG = """<b>❪ SET MESSAGE SKIPPING NUMBER ❫</b>

<b>Skip the number of messages you enter and forward the rest.</b>
Default Skip Number = <code>0</code>
<code>eg: You enter 0 = 0 messages skipped
You enter 5 = 5 messages skipped</code>
/cancel - cancel this process"""
    
    CANCEL = "<b>Process Cancelled Successfully!</b>"
    
    BOT_DETAILS = "<b><u>📄 BOT DETAILS</u></b>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"
    USER_DETAILS = "<b><u>📄 USERBOT DETAILS</u></b>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"
    
    TEXT = """
╔════❰ ғᴏʀᴡᴀʀᴅ sᴛᴀᴛᴜs ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼🕵 ғᴇᴛᴄʜᴇᴅ Msɢ: <code>{}</code>
║┃
║┣⪼✅ sᴜᴄᴄᴇssғᴜʟʟʏ Fᴡᴅ: <code>{}</code>
║┃
║┣⪼👥 ᴅᴜᴘʟɪᴄᴀᴛᴇ Msɢ: <code>{}</code>
║┃
║┣⪼🗑 ᴅᴇʟᴇᴛᴇᴅ Msɢ: <code>{}</code>
║┃
║┣⪼🪆 Sᴋɪᴘᴘᴇᴅ Msɢ: <code>{}</code>
║┃
║┣⪼🔁 Fɪʟᴛᴇʀᴇᴅ Msɢ: <code>{}</code>
║┃
║┣⪼📊 Cᴜʀʀᴇɴᴛ Sᴛᴀᴛᴜs: <code>{}</code>
║┃
║┣⪼𖨠 Pᴇʀᴄᴇɴᴛᴀɢᴇ: <code>{}</code> %
║╰━━━━━━━━━━━━━━━➣ 
╚════❰ {} ❱══❍⊱❁۪۪
"""
    
    DUPLICATE_TEXT = """
╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ғᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
║┃
║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ {} ❱══❍⊱❁۪۪
"""
    
    DOUBLE_CHECK = """<b><u>DOUBLE CHECKING ⚠️</u></b>
<code>Before forwarding the messages Click the Yes button only after checking the following</code>

<b>★ YOUR BOT:</b> [{botname}](t.me/{botuname})
<b>★ FROM CHANNEL:</b> `{from_chat}`
<b>★ TO CHANNEL:</b> `{to_chat}`
<b>★ SKIP MESSAGES:</b> `{skip}`

<i>° [{botname}](t.me/{botuname}) must be admin in <b>TARGET CHAT</b></i> (`{to_chat}`)
<i>° If the <b>SOURCE CHAT</b> is private, your userbot must be member or your bot must be admin there also</i>

<b>If the above is checked then the yes button can be clicked</b>"""
    
    SETTINGS_TXT = """<b>Change your settings as you wish</b>"""
