class script(object):
    START_TXT = """● ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ "ꜱᴇᴀʀᴄʜ" ᴛᴏ ꜱᴇᴀʀᴄʜ ᴍᴏᴠɪᴇꜱ.
"""
    HELP_TXT = """ᴍᴏᴠɪᴇ & ꜱᴇʀɪᴇꜱ ꜱᴇᴀʀᴄʜ ᴄʟɪᴄᴋ <a href=https://t.me/team_silent_king>/ʜᴇʟᴘ</a> ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ʙᴏᴛ"""
    ABOUT_TXT = """✯
✯ ʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴍᴇ: <a href=https://t.me/off_chats > ꜱᴜᴘᴘᴏʀᴛ</a>
✯ ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ: ᴠ1.0.2 [🤧 ᴠ1.0.1 ☞ ᴠ1.0.2 🤧]"""
    SOURCE_TXT = """
- Source - Ask Here @off_chats

<b>DEVS:</b>
- <a href=https://t.me/off_chats>ɢʀᴏᴜᴘ ꜱᴜᴘᴘᴏʀᴛ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. 𝑀𝑅 MÖVÌÈS WÄLÄ's should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- 𝑀𝑅 MÖVÌÈS WÄLÄ's Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/team_silent_king)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.
@team_silent_king """
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
@team_silent_king

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code> 
@team_silent_king """
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code> 
@team_silent_king"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code> 
@team_silent_king """
    STATUS_TXT = """★ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ : <code>{}</code>
★ ᴜꜱᴇʀꜱ : <code>{}</code>
★ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ : <code>{}</code>
★ ᴜꜱᴇᴅ : <code>{}</code> 𝙼𝚒𝙱
★ ᴜꜱᴇ : <code>{}</code> 𝙼𝚒𝙱 
@team_silent_king """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀꜱ = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser 👥
ID - <code>{}</code>
Name - {}
"""
