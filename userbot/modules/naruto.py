from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.chidori(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Hello")
    sleep(2)
    await typew.edit("Gua Kakashi Lu Mungkin Mengenal Gua Sebagai Copy Ninja")
    sleep(5)
    await typew.edit("Lu Akan Membayar Untuk Apa yang Lu Lakukan Pada Rekan-Rekan Gua")
    sleep(6)
    await typew.edit("( ◗_ ╂ ) ☞✹)Chidori ")
    sleep(2)
    await typew.edit("You:(✖﹏✖)")

# Create by myself @PashaDIE


@register(outgoing=True, pattern='^.rasengan(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Hello")
    sleep(2)
    await typew.edit("Im Naruto Uzumaki And Im The Hokage Of Hidden Leaf Village!")
    sleep(5)
    await typew.edit("You Are Gonna Pay For What You Did!")
    sleep(6)
    await typew.edit("(Ξ｀Д´)🌀)))Rasengan！！")
    sleep(2)
    await typew.edit("You: ( ✖╭╮✖ )")

# Create by myself @PashaDIE
