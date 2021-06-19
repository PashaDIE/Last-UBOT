""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai Bang 《-{DEFAULTUSER}-》 Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n-->>>[Abang²an]<<<--(t.me/PashaDIE)"
        "\n-->>>[Repo]<<<--(https://github.com/PashaDIE/Last-UBOT)"
        "\n-->>>[Instagram Abang²an]<<<--(Instagram.com/pdie.09)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/PashaDIE/Last-UBOT/Last-Userbot/varshelper.txt)")


CMD_HELP.update({
    "lasthelper":
    "🐣CMD🐣`.lhelp`\
\nPenjelasan: Bantuan Untuk saya-Userbot.\
\n🐣CMD🐣`.vars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
