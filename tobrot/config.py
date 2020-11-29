import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1438892370:AAF7V-VjuZbSXltr_oIDSBgnZNjNS8UKJXw")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 1046625))
    API_HASH = os.environ.get("c68afc924b92d73ce27708b155f1e5b4")
    OWNER_ID = int(os.environ.get("OWNER_ID", 617426792))
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "-1001455886928").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./YDrive"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 10))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "@YMoviez")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl")
    PYTDL_COMMAND = os.environ.get("PYTDL_COMMAND", "pytdl")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "type = drive\nclient_id = 833850923810-cliasc9ugki633o3v4b4l9avbgbc5pvr.apps.googleusercontent.com\nclient_secret = N1sA4jINJ4yg07NUTZs03Q7Y\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMB_YghsLByBwYikXsdcWJ6FpavGbxfYXW7UlcPE936FZbMyiQ-BV-NMXG4WGc-aS0ADIFvEbfW-Hm1mhbqD24HFKt6A5fAFDNfsuR-mfE9lOVjAt8Jzn0p93M-mhrxK032gIRGpJNjxdO3VWf6IO1CP0dxoYxc","token_type":"Bearer","refresh_token":"1//0g6FeVdL-g8yeCgYIARAAGBASNwF-L9IrRy13QID9XAYy9dXC81ecQaVQbd30qhbjmbTQ_tAUCuzNjJ6pmCTRnUflk7HL0T_yrBw","expiry":"2020-10-09T20:49:30.3276637+07:00"}")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "YDrive")
    INDEX_LINK = os.environ.get("INDEX_LINK", "https://gd.yasir.my.id")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail")
    CLEAR_UNDELETED = os.environ.get("CLEAR_UNDELETED", "clearall")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "getlog") 
