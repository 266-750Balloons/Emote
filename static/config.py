import os
from pathlib import Path

version = open("/usr/share/emote/version", "r").read()

is_snap = False
is_flatpak = False
is_wayland = os.environ.get("XDG_SESSION_TYPE", "").lower() == "wayland"
is_debug = os.environ.get("GTK_DEBUG") == "interactive"
is_dev = os.environ.get("ENV") == "dev"

css_path = "/usr/share/emote/style.css"
emoji_path = "/usr/share/emote/emojis.csv"
logo_path = "/usr/share/icons/emote.svg"

data_dir = os.path.join(Path.home(), ".local/share/Emote")