from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from BADMUSIC import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
                    text="🔙",
                    callback_data="settingsback_helper",
                ),
        InlineKeyboardButton(
                    text="🗑",
                    callback_data="close",
                ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴀᴅᴍɪɴ",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="ᴀᴜᴛʜ",
                    callback_data="help_callback hb2",
                ),
            
            ],
            [
                InlineKeyboardButton(
                    text="ʙʟᴏᴄᴋ",
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text="ɢᴄᴀsᴛ",
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ɢʙᴀɴ",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="ʟʏʀɪᴄs",
                    callback_data="help_callback hb5",
                ),
            ],
                        
            [
                InlineKeyboardButton(
                    text="ᴘʟᴀʏʟɪsᴛ",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="ᴠᴏɪᴄᴇ-ᴄʜᴀᴛ ",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="ᴘʟᴀʏ",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="sᴜᴅᴏ",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
          InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
    
    
    
