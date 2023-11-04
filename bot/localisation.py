#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config

class Localisation:
    START_TEXT = "Hello,\n\nThis is a Telegram *Video Encoder Bot*. Please send me any Telegram big video file, and I will compress it as a small video file. Use `/help` for more details.\nOwner: @chammak_challoo"
   
    ABS_TEXT = "Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: [file size might be approximate]({})\nIf you want to set a custom thumbnail, send a photo before or quickly after tapping on any of the below buttons. You can use `/deletethumbnail` to delete the auto-generated thumbnail."
    
    DOWNLOAD_START = "⚡ Downloading..."
    
    UPLOAD_START = "⚡ Uploading..."
    
    COMPRESS_START = "⚡ Trying to encode..."
    
    RCHD_BOT_API_LIMIT = "Size greater than the maximum allowed size (50MB). Nevertheless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds. Detected File Size: {}. Sorry, but I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "@Anime_DownLord"

    CUSTOM_CAPTION_UL_FILE = " "

    COMPRESS_PROGRESS = "🕛 ETA: {} ♻️ Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video/file thumbnail saved. This image will be used in the video/file."
    
    DELETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared successfully."
    
    FF_MPEG_DELETED_CUSTOM_MEDIA = "✅ Media cleared successfully."
    
    SAVED_RECEIVED_DOC_FILE = "✅ Downloaded Successfully."
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom Thumbnail found."
    
    NO_VIDEO_FORMAT_FOUND = "No one's gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User [{}](tg://user?id={}) added to {} till {}."
    
    FF_MPEG_RO_BOT_STORAGE_ALREADY_EXISTS = "⚠️ Already one process going on! ⚠️\n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot.\n\n1. Send me your Telegram big video file.\n2. Reply to the file with: `/compress 50`\n\nSupport Group: @"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "Current CHAT ID: `<code>{CHAT_ID}</code>`"
    )
