import os

server_command_args = [
  "java",
  "-Xms512M",
  "-Xmx2G",
  "-jar",
  "Launcher.jar",
  "nogui"
]

os.execvp("java", server_command_args)
