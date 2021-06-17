from time import sleep
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern='^.pagi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("▄▀▀──▄▀▀▄─▄▀▀▄─█▀▄")
    sleep(1)
    await typew.edit("█─▀█─█──█─█──█─█─█")
    sleep(1)
    await typew.edit("─▀▀───▀▀───▀▀──▀▀─")
    sleep(1)
    await typew.edit("█▄─▄█─▄▀▀▄─█▀▄─█▄─█─█─█▄─█─▄▀▀─")
    sleep(1)
    await typew.edit("█─▀─█─█──█─██▀─█─▀█─█─█─▀█─█─▀█")
    sleep(1)
    await typew.edit("▀───▀──▀▀──▀─▀─▀──▀─▀─▀──▀──▀▀─")
    sleep(1)
    await typew.edit("𝐆𝐨𝐨𝐝 𝐦𝐨𝐫𝐧𝐢𝐧𝐠.🌄")

    CMD_HELP.update({
        'Good morning':
        '🐣CMD🐣`.pagi`\
        \nUsage: Coba aja:).'
    })
