#!/usr/bin/env python3
import os
import sys

config = {
  "server": {
    "jarfile": "Launcher.jar",
    "ram": {
      "min": "512M",
      "max": "2G"
    },
    "hide_gui": True
  }
}

def start_server():
  server_config = config["server"]
  server_ram = server_config["ram"]

  server_command_args = [
    "java",
    f"-Xms{server_ram['min']}",
    f"-Xmx{server_ram['max']}",
    "-jar",
    server_config["jarfile"]
  ]

  if server_config["hide_gui"]:
    server_command_args.append("nogui")

  print(f"[INFO]: Running command: {' '.join(server_command_args)}")
  os.execvp("java", server_command_args)

def main():
  script_cli_args = sys.argv[1:] if len(sys.argv) > 1 else [""]
  script_command = script_cli_args[0]

  match script_command:
    case "start":
      start_server()
    case "":
      print("[ERROR]: No command was provided")
    case _:
      print(f"[ERROR]: Unknown command: {script_command}")


if __name__ == "__main__":
  main()