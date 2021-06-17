from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.pasha(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Kenalin Nama gua pasha`")
    sleep(3)
    await typew.edit("`15 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Bekasi, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^ilyu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Gua mao Bilang`")
    sleep(3)
    await typew.edit("`Gua Sayang Lu`")
    sleep(1)
    await typew.edit("`I LOVE YOU NENG 🐣`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.pe(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Bapaknya Udin Di Makan Udang`")
    sleep(2)
    await typew.edit("`Cuma Sendiri nih Senggol Dong`")


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Awali perkataan dengan dengan salam`")
    sleep(1)
    await typew.edit("`Assalamualaikum Sayang`")


CMD_HELP.update({
    "animasi3":
    "🐣CMD🐣`.pe`\
\nPenjelasan: Cek lah asw.\
\n\n🐣CMD🐣`.pasha`\
\nPenjelasan: Cek lah asw.\
\n\n🐣CMD🐣`.ilyu`\
\nPenjelasan: Cek lah asw.\
\n\n🐣CMD🐣`p`\
\nPenjelasan: Cek lah asw.\
\n\n🐣CMD🐣`.semangat`\
\nPenjelasan: Cek lah asw."
})
