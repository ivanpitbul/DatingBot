from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_profile_keyboard(verification):
    markup = InlineKeyboardMarkup(row_width=2)
    turn_off = InlineKeyboardButton(text="❌ Удалить анкету", callback_data="disable")
    if not verification:
        verification_btn = InlineKeyboardButton(text="✅ Верификация", callback_data="verification")
        markup.row(verification_btn)
    edit_profile = InlineKeyboardButton(text="⬆ Изменить анкету", callback_data="change_profile")
    instagram = InlineKeyboardButton(text="📸 Instagram", callback_data="add_inst")
    back = InlineKeyboardButton(text="⏪ Назад", callback_data="back_with_delete")
    markup.add(edit_profile, instagram)
    markup.add(turn_off)
    markup.add(back)
    return markup
