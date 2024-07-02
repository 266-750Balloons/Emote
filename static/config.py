import os
from pathlib import Path

version = open("/usr/share/emote/version", "r").read()

css_path = "/usr/share/emote/style.css"
emoji_path = "/usr/share/emote/emojis.csv"
logo_path = "/usr/share/icons/emote.svg"

data_dir = os.path.join(Path.home(), ".local/share/Emote")