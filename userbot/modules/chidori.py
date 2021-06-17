from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.chidori(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("Hello")
    sleep(5)
    await typew.edit("Gua Kakashi Lu Mungkin Mengenal Gua Sebagai Copy Ninja")
    sleep(10)
    await typew.edit("Lu Akan Membayar Untuk Apa yang Lu Lakukan Pada Rekan-Rekan Gua")
    sleep(2)
    await typew.edit("( ◗_ ╂ ) ☞✹)Chidori ")
    await typew.edit("You:(✖﹏✖)")

# Create by myself @PashaDIE
