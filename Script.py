class script(object):
    START_TXT = """<b>HELLO {},
MY NAME IS <a href=https://t.me/{}>{}</a>, I PROVIDE SERIES. JUST ADD ME TO YOUR GROUP AND ENJOY!😍</b>"""
    HELP_TXT = """{},
<b>HERE IS THE HELP FOR MY COMMANDS</b>"""
    ABOUT_TXT = """<b>♠️ MY NAME: {}</b>
<b>♣️ OWNED BY:</b> <a href=https://t.me/JiC54_SERIES_Bot>Click Here!</a>
<b>♣️ LANGUAGE:</b> 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
<b>♣️ DATABASE:</b> 𝙼𝙾𝙽𝙶𝙾
<b>♣️ BOT SERVER:</b> 𝙷𝙴𝚁𝙾𝙺𝚄
<b>♣️ 𝙱OT VERSION:</b> <code>5.1.0</code></b>"""
    SOURCE_TXT = """<b>JiC54 CHANNELS:</b> 
    
[Movies and Series 2022](https://t.me/+H_6j47erCp44YjY0)
[House of Movies](https://t.me/+uQBJ5JaaLpgyMWI0)
[Dax songs](https://t.me/+EHBqUrMHnglmZWY8)
[DC Series](https://t.me/+8eC2YwzHZtUwZDg0)
[Marvel Movies](https://t.me/+GvVfP9p-YAsyMTY0)
[African Movies](https://t.me/+6QrMOpOVtKAxOGQ0)
[WWE wrestling](https://t.me/+LhZuWiqE21NiYzY0)

<b>JiC54 GROUPS:</b>
[Request Movies](https://t.me/+dFGzJDTQWow2ZGY8)
[Request Series](https://t.me/+bCTNQn4-5TtkZmZk)
[Request Dax Songs](https://t.me/+gTYFpj1ZBIIxZTQ0)

<b>JiC54 BOTS:</b>
[Movies Bot](http://t.me/JiC54_MOVIES_Bot)
[Series Bot](http://t.me/JiC54SeriesBot)
[Filter Bot](http://t.me/JiC54filterBot)
[File to Links Bot](http://t.me/filestolinks1_bot)"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and this bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allow you to send buttons without any content, so content is mandatory.
2. <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/JiC54_MOVIES_Bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> the admin of your channel if it's private.
2. make sure that your channel does not contains CAMRips, porn and fake files.
3. Forward the last message to <a href=https://t.me/JiC54_MOVIES_Bot>me</a> with quotes.
 I'll add all the files in that channel to my database."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting <a href=https://t.me/JiC54_MOVIES_Bot>me</a> to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 MOVIES Bot</a>

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
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
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ TOTAL FILES <code>{}000</code>
★ USED RAM: <code>{}</code> 
★ FREE RAM: <code>{}</code>
★ TOTAL RAM: <code>512MB</code>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
STATUS_TTXXTT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code>
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code>"""
