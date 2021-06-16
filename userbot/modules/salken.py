""" Userbot module salken for deafult user"""

import asyncio

from userbot import ALIVE_NAME, CMD_HELP, COUNTRY,
from userbot.events import register


@register(outgoing=True, pattern="^.salken$")
async def salken(salken):
    """ Basically it's .salken command """
    await salken.edit(f"`Heyyo bang Gua {ALIVE_NAME}`")
    await asyncio.sleep(2)
    await salken.edit(f"`Umur gua Tanya Google aja bang`")
    await asyncio.sleep(2)
    await salken.edit(f"`Gua tinggal di {COUNTRY} Salam Kenal ya bang:)`")


CMD_HELP.update({
    "salken":
    "🐣 **Cmd** : `.salken`\
    \n🐣 **Descriptions** : Command Salken Buat lu :)."
})
