# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) 
# Made by @REBEL_IS_OP...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in rebel Userbot by @REBEL_IS_OP

import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, rebelversion
from REBELBOT.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins

# ๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "๐๐ธ๐ฝ๐๐ธ๐น๐๐"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for รรลฎ$HรณpBรศ

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

rebel = bot.uid

edit_time = 10
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/528425227d8763cedee29.mp4"
file2 = "https://telegra.ph/file/6700325671af519dd3fd8.mp4"
file3 = "https://telegra.ph/file/a3090425421917fd339ee.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "  __**๐ฅ๐ฅโ๐ผ๐น๐ผ๐๐น๐๐ ๐๐ ๐ธ๐๐๐๐ผ๐ฅ๐ฅ**__\n\n"

pm_caption += (
    f"                 ๐๐๐ธ๐๐๐ผโ๐\n**  ใ๐[{DEFAULTUSER}](tg://user?id={rebel})๐ใ**\n\n"
)

pm_caption += "๐ก๏ธ๐ง๐๐๐๐ง๐๐ข๐ก๐ก๏ธ : `1.15.0` \n\n"

pm_caption += f"๐๐ฅ๐๐๐๐๐๐ข๐ง๐ : `{rebelversion}`\n\n"

pm_caption += f"๐ฑ๐ฆ๐จ๐๐ข๐ฑ            : `{sudou}`\n\n"

pm_caption += "๐๐๐๐๐ก๐ก๐๐๐๏ธ   : [แดแดษชษด](https://t.me/REBELBOT_SUPPORT)\n\n"

pm_caption += "๐๐๐ฅ๐๐๐ง๐ข๐ฅ๐    : [เผผ๐ทร๐งร๐ฑ](https://t.me/REBEL_IS_OP)\n\n"

pm_caption += "๐คฉ๐ฆ๐จ๐ฃ๐ฃ๐ข๐ฅ๐ง๐๐ฅ๐คฉ    :[โโพโโฝโ](https://t.me/Baapisbacknishujibolmotherchod)\n\n"

pm_caption += "      [๐ฅ๐ฅ๐๐ฃ๐ข๐ฅ]() ๐น [๐๐๐ถ๐ฐ๐ฒ๐ป๐๐ฒ๐](https://github.com/H1M4N5HU0P/rebel-BOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
