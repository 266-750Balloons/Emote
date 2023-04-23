# <span><img width="24" height="24" src="https://github.com/tom-james-watson/Emote/blob/master/static/logo.svg"></span> Emote

Emote is a modern emoji picker for Linux 🚀. Written in GTK3, Emote is lightweight and stays out of your way.

Launch the emoji picker with the configurable keyboard shortcut `Ctrl+Alt+E`, and select one or more emojis to have them be automatically pasted into your currently focused app.

- 🍾 Built as a popup: quick invocation, and disappears when not needed, does not stay as a standalone window
- 🫠 Provide a large and up-to-date list of emojis retrieved from [openmoji.org](https://openmoji.org/)
- 🧠 Shows the last used emojis by default
- 🔎 Search text box automatically focused and ready to type when invoked
- ⌨️ Can use shortcuts to navigates and select emojis
- ✒️ Selected emoji automatically pasted to your currently focused app (on X11 only)

ℹ️ Note:

- ⚡️ Emote [shows up faster](https://github.com/tom-james-watson/Emote/issues/54) when invoked using the built-in keyboard shortcut (`Ctrl+Alt+E` by default), than when using a manually registered keyboard shortcut.
- 🪟 Emote under Wayland cannot automatically paste the emoji into other apps, and also requires manual registering of a global keyboard shortcut - [Hotkey In Wayland](https://github.com/tom-james-watson/Emote/wiki/Hotkey-In-Wayland). This is due to intentional restrictions in the design of Wayland itself.

<p align="center">
  <img width="500" src="https://raw.githubusercontent.com/tom-james-watson/Emote/master/images/screenshot.png">
</p>

## 📥️ Installation

TODO - add flathub link

An unofficial build of Emote is also available in the AUR : https://aur.archlinux.org/packages/emote.

Enable autostart:

```bash
cp -L "/var/lib/flatpak/exports/share/applications/com.tomjwatson.Emote.desktop" ~/.config/autostart/
# Or if it was installed locally:
cp -L "cp ~/.local/share/flatpak/exports/share/applications/com.tomjwatson.Emote.desktop" ~/.config/autostart/
```

## 📖 Guide

### 🚀 Launching

Emote runs in the background and automatically starts when you log in.

The emoji picker can be opened with either the keyboard shortcut, or by clicking the app icon again.

### ℹ️ Usage

Select an emoji to and have it be pasted to your currently focused app. The emoji will also be copied to your clipboard, so you can then paste the emoji wherever you need.

You can select multiple emojis by selecting them with right click.

### ⌨️ Keyboard Shortcuts

Open Emoji Picker: `Ctrl+Alt+E` (configurable)

Select Emoji: `Enter`

Add Emoji to Selection: `Shift+Enter`

Focus Search: `Ctrl+F`

Next Emoji Category: `Ctrl+Tab`

Previous Emoji Category: `Ctrl+Shift+Tab`

## 🧑‍💻 Development

### 📥️ Requirements

Install development libraries:

```bash
sudo apt install xdotool libgtk-3-dev libgirepository1.0-dev python3-venv gir1.2-keybinder-3.0 libkeybinder-dev desktop-file-utils
# or with dnf
sudo dnf install xdotool gtk3-devel keybinder3-devel libgirepository1.0-dev desktop-file-utils gobject-introspection-devel flatpak-builder

sudo dnf install libffi-devel
```

Install pipenv:

```bash
sudo pip3 install pipenv
```

Install dependencies:

```bash
make install
```

### 🛩️ Running

Run the development version:

```bash
make dev
```

### 🔄 Update emojis

To update the list of emojis to the latest available on [openmoji.org](https://openmoji.org), run:

```bash
make update-emojis
```

### 🐞 Debugging GTK3 with GtkInspector

Enable debug keybinding:

```bash
gsettings set org.gtk.Settings.Debug enable-inspector-keybinding true
```

Launch app in debug mode with interactive inspector:

```bash
make dev-debug
```

### 📦️ Packaging

You will need to have [`flatpak`](https://flatpak.org/setup/) installed.

Install `flatpak-builder`, the GNOME SDK, and `flatpak-pip-generator`:

```bash
make flatpak-install
```

Optionally re-generate the `flatpak/python3-requirements.json` if the dependencies in the `Pipfile` have been changed:

```bash
make flatpak-requirements
```

Build the flatpak package and install it locally:

```bash
make flatpak
```

Run Emote with flatpak (can also be done from the desktop entry):

```bash
flatpak run com.tomjwatson.Emote
```

**Build and publish to Flathub**:

```bash
make flathub
```

In case you are facing issues with the cache not properly updating, you can clean the cache with:

```bash
make flatpak-clean
```

Use `journalctl -f` to see the app logs, run the command below if you want to access inside the containerized flatpak app to debug.

```bash
flatpak run --command=sh --devel com.tomjwatson.Emote
```

### 🤝 Attribution

Emoji data is sourced from https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/data/openmoji.csv which is compiled by the lovely people at https://openmoji.org.🫠
