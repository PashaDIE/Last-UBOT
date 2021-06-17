from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.chidori(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("Hello")
    sleep(3)
    await typew.edit("Gua Kakashi Lu Mungkin Mengenal Gua Sebagai Copy Ninja")
    sleep(2)
    await typew.edit("Anda Akan Membayar Untuk Apa yang Anda Lakukan Pada Rekan-Rekan Saya")
    sleep(1)
    await typew.edit("( ◗_ ╂ ) ☞✹)Chidori ")
    await typew.edit("You:(✖﹏✖)")

# Create by myself @PashaDIE
