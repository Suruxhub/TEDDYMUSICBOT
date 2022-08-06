from YukkiMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MUSIC_BOT_NAME as BOT_NAME

BOT_USERNAME = app.username
START_TEXT = f"""
🦋 **Hᴇʟʟᴏ MENTION !**

**Yᴏᴜ ᴄᴀɴ ᴜsᴇ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ᴛᴏ ᴘʟᴀʏ Mᴜsɪᴄ ᴏʀ Vɪᴅᴇᴏs ɪɴ ʏᴏᴜʀ Gʀᴏᴜᴘ Vɪᴅᴇᴏ Cʜᴀᴛ.**

🖤 **Fɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ Bᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ➤ 📚 Cᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ**
"""

COMMANDS_TEXT = f"""
✨ **Hᴇʟʟᴏ MENTION !**

**Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="📚 Cᴏᴍᴍᴀɴᴅs", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔧 Sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="🪄 Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url="https://t.me/Teddy_bot_updates"
            ),
            InlineKeyboardButton(
                text="💬 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url="https://t.me/Teddysupport"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="➕ Aᴅᴅ ᴍᴇ ᴛᴏ Gʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text="📚 Cᴏᴍᴍᴀɴᴅs", callback_data="command_menu"
            ),                       
        ],
        [
            InlineKeyboardButton(
                text="🪄 Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url="https://t.me/Teddy_bot_updates"
            ),
            InlineKeyboardButton(
                text="💬 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url="https://t.me/Teddysupport"
            ),                       
        ],        
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="📍Aᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="🎮Bᴏᴛ Cᴏᴍᴍᴀɴᴅs", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="🎶Pʟᴀʏ Cᴏᴍᴍᴀɴᴅs", callback_data="play_cmd"
            ),            
            InlineKeyboardButton(
                text="🍭Exᴛʀᴀ Cᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/SiestaXMusic-Commands-03-13-2"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="📍Aᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="🎮Bᴏᴛ Cᴏᴍᴍᴀɴᴅs", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="🎶Pʟᴀʏ Cᴏᴍᴍᴀɴᴅs", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="🚩Sᴜᴅᴏ Cᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/SiestaXMusic-Commands-03-13"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="🍭Exᴛʀᴀ Cᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/SiestaXMusic-Commands-03-13-2"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🚩Sᴜᴅᴏ Cᴏᴍᴍᴀɴᴅss", url="https://telegra.ph/SiestaXMusic-Commands-03-13"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
✅--**Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅs:**--

ᴄ sᴛᴀɴᴅs ғᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ.

/pause ᴏʀ /cpause - Pᴀᴜsᴇ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
/resume ᴏʀ /cresume - Rᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ ᴍᴜsɪᴄ.
/mute ᴏʀ /cmute - Mᴜᴛᴇ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
/unmute ᴏʀ /cunmute - Uɴᴍᴜᴛᴇ ᴛʜᴇ ᴍᴜᴛᴇᴅ ᴍᴜsɪᴄ.
/skip ᴏʀ /cskip - Sᴋɪᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
/stop ᴏʀ /cstop - Sᴛᴏᴘ ᴛʜᴇ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ.
/shuffle ᴏʀ /cshuffle - Rᴀɴᴅᴏᴍʟʏ sʜᴜғғʟᴇs ᴛʜᴇ ᴏ̨ᴜᴇᴜᴇᴅ ᴘʟᴀʏʟɪsᴛ.

✅--**Sᴘᴇᴄɪғɪᴄ Sᴋɪᴘ:**--
/skip ᴏʀ /cskip [Nᴜᴍʙᴇʀ(ᴇxᴀᴍᴘʟᴇ: 3)] 
    - Sᴋɪᴘs ᴍᴜsɪᴄ ᴛᴏ ᴀ ᴛʜᴇ sᴘᴇᴄɪғɪᴇᴅ ᴏ̨ᴜᴇᴜᴇᴅ ɴᴜᴍʙᴇʀ. Exᴀᴍᴘʟᴇ: /skip 3 ᴡɪʟʟ sᴋɪᴘ ᴍᴜsɪᴄ ᴛᴏ ᴛʜɪʀᴅ ᴏ̨ᴜᴇᴜᴇᴅ ᴍᴜsɪᴄ ᴀɴᴅ ᴡɪʟʟ ɪɢɴᴏʀᴇ 1 ᴀɴᴅ 2 ᴍᴜsɪᴄ ɪɴ ᴏ̨ᴜᴇᴜᴇ.

✅--**Lᴏᴏᴘ Pʟᴀʏ:**--
/loop ᴏʀ /cloop [ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ] ᴏʀ [Nᴜᴍʙᴇʀs ʙᴇᴛᴡᴇᴇɴ 1-10] 
    - Wʜᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ, ʙᴏᴛ ʟᴏᴏᴘs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ ᴛᴏ 1-10 ᴛɪᴍᴇs ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. Dᴇғᴀᴜʟᴛ ᴛᴏ 10 ᴛɪᴍᴇs.
"""
AUTH_TEXT = """
✅--**Aᴜᴛʜ Usᴇʀs:**--
Aᴜᴛʜ Usᴇʀs ᴄᴀɴ ᴜsᴇ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.

/auth [Usᴇʀɴᴀᴍᴇ] - Aᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
/unauth [Usᴇʀɴᴀᴍᴇ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
/authusers - Cʜᴇᴄᴋ AUTH LIST ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
"""

AUTH_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

BOT_TEXT = """
✅--**Bᴏᴛ Cᴏᴍᴍᴀɴᴅs:**--

/stats - Gᴇᴛ Tᴏᴘ 10 Tʀᴀᴄᴋs Gʟᴏʙᴀʟ Sᴛᴀᴛs, Tᴏᴘ 10 Usᴇʀs ᴏғ ʙᴏᴛ, Tᴏᴘ 10 Cʜᴀᴛs ᴏɴ ʙᴏᴛ, Tᴏᴘ 10 Pʟᴀʏᴇᴅ ɪɴ ᴀ ᴄʜᴀᴛ ᴇᴛᴄ ᴇᴛᴄ.

/sudolist - Cʜᴇᴄᴋ Sᴜᴅᴏ Usᴇʀs ᴏғ Yᴜᴋᴋɪ Mᴜsɪᴄ Bᴏᴛ

/lyrics [Mᴜsɪᴄ Nᴀᴍᴇ] - Sᴇᴀʀᴄʜᴇs Lʏʀɪᴄs ғᴏʀ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ Mᴜsɪᴄ ᴏɴ ᴡᴇʙ.

/song [Tʀᴀᴄᴋ Nᴀᴍᴇ] ᴏʀ [YT Lɪɴᴋ] - Dᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴛʀᴀᴄᴋ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ ɪɴ ᴍᴘ3 ᴏʀ ᴍᴘ4 ғᴏʀᴍᴀᴛs.

ᴄ sᴛᴀɴᴅs ғᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ.
/queue ᴏʀ /cqueue - Cʜᴇᴄᴋ Qᴜᴇᴜᴇ Lɪsᴛ ᴏғ Mᴜsɪᴄ.
"""

PLAY_TEXT = """
✅--**Pʟᴀʏ Cᴏᴍᴍᴀɴᴅs:**--

Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs = ᴘʟᴀʏ , ᴠᴘʟᴀʏ , ᴄᴘʟᴀʏ

FᴏʀᴄᴇPʟᴀʏ Cᴏᴍᴍᴀɴᴅs = ᴘʟᴀʏғᴏʀᴄᴇ , ᴠᴘʟᴀʏғᴏʀᴄᴇ , ᴄᴘʟᴀʏғᴏʀᴄᴇ

ᴄ sᴛᴀɴᴅs ғᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ.
ᴠ sᴛᴀɴᴅs ғᴏʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏ.
ғᴏʀᴄᴇ sᴛᴀɴᴅs ғᴏʀ ғᴏʀᴄᴇ ᴘʟᴀʏ.

/play ᴏʀ /vplay ᴏʀ /cplay  - Bᴏᴛ ᴡɪʟʟ sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ʏᴏᴜʀ ɢɪᴠᴇɴ ᴏ̨ᴜᴇʀʏ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴏʀ Sᴛʀᴇᴀᴍ ʟɪᴠᴇ ʟɪɴᴋs ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs.

/playforce ᴏʀ /vplayforce ᴏʀ /cplayforce -  Fᴏʀᴄᴇ Pʟᴀʏ sᴛᴏᴘs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀɴᴅ sᴛᴀʀᴛs ᴘʟᴀʏɪɴɢ ᴛʜᴇ sᴇᴀʀᴄʜᴇᴅ ᴛʀᴀᴄᴋ ɪɴsᴛᴀɴᴛʟʏ ᴡɪᴛʜᴏᴜᴛ ᴅɪsᴛᴜʀʙɪɴɢ/ᴄʟᴇᴀʀɪɴɢ ᴏ̨ᴜᴇᴜᴇ.

/channelplay [Cʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ] ᴏʀ [Dɪsᴀʙʟᴇ] - Cᴏɴɴᴇᴄᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀ ɢʀᴏᴜᴘ ᴀɴᴅ sᴛʀᴇᴀᴍ ᴍᴜsɪᴄ ᴏɴ ᴄʜᴀɴɴᴇʟ's ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ.


💠 --**Bᴏᴛ's Sᴇʀᴠᴇʀ Pʟᴀʏʟɪsᴛs:**--
/playlist  - Cʜᴇᴄᴋ Yᴏᴜʀ Sᴀᴠᴇᴅ Pʟᴀʏʟɪsᴛ Oɴ Sᴇʀᴠᴇʀs.
/deleteplaylist - Dᴇʟᴇᴛᴇ ᴀɴʏ sᴀᴠᴇᴅ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ᴘʟᴀʏʟɪsᴛ
/play  - Sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ Yᴏᴜʀ Sᴀᴠᴇᴅ Pʟᴀʏʟɪsᴛ ғʀᴏᴍ Sᴇʀᴠᴇʀs.
"""


BASIC_TEXT = """
💠 **Bᴀsɪᴄ Cᴏᴍᴍᴀɴᴅs:**

/start - Sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ

/help - Gᴇᴛ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ

/play - Pʟᴀʏ sᴏɴɢs ᴏʀ ᴠɪᴅᴇᴏs ɪɴ ᴠᴄ

/vplay - Pʟᴀʏ ᴠɪᴅᴇᴏ ɪɴ VC

/settings - Cʜᴇᴄᴋ Sᴇᴛᴛɪɴɢs ᴏғ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

**Sᴏᴍᴇ Usᴇғᴜʟ Cᴏᴍᴍᴀɴᴅs :** 

/pause /resume /skip /end /loop /shuffle
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)

ADMIN_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="📛Aᴜᴛʜ Cᴏᴍᴍᴀɴᴅs", callback_data="auth_cmds"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🔍 Bᴀsɪᴄ Cᴏᴍᴍᴀɴᴅs", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="📚 Aᴅᴠᴀɴᴄᴇᴅ Cᴏᴍᴍᴀɴᴅs", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↪️ Bᴀᴄᴋ", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Cʟᴏsᴇ", callback_data="close_btn"
            ),            
        ],                        
    ]
)
