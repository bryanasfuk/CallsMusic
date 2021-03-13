from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Halo Ganteng, {message.from_user.first_name}!</b>
Saya adalah bot music voice call group!
Mari kita ramaikan hasanah permusikan duniawi telegram. 
Cara pake nya tinggal add bot ini ke gc mu jangan lupa chat dulu @fckyouasshole hehehe
Klik tombol di bawah ini.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Cara Pakai", url="https://telegra.ph/Cara-menggunakan-Bot-Music-03-12"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Buat nyari lagu ini bukan buat nyari bokep",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Tidak ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
