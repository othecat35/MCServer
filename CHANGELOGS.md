# v1.0.0 - First release
Added:
 - `init` command
 - `search` command
 - `start` command
 - Config system

# v1.0.1 - Update log messages
Changes:
 - `Searching mods` message now includes search filters
 - Remove the word `file` in  is some configuration error messages

# v1.1.0 - Show command
Added:
 - `show` command

# 1.1.1
- Replace textwrap.shorten to .wrap in `search` mod description

# 1.2.0
- Move java command options to a seperate launcher.json configuration

# 1.2.1
- Renamed function color_string to color_text
- Replace all raise error to Exception
- Update "Showing ... out of ... mods ..." message to have pages count
- Update mod_environment_color to use color_text