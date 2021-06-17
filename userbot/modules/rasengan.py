from time import sleep
from userbot.events import register
from userbot import CMD_HELP


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


CMD_HELP.update({
    "rasengan":
    "🐣CMD🐣`.rasengan`\
\nPenjelasan: Cek lah asw.\
