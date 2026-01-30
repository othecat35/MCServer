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
  ram_limit = server_config["ram"]

  command_args = [
    "java",
    f"-Xms{ram_limit['min']}",
    f"-Xmx{ram_limit['max']}",
    "-jar",
    server_config["jarfile"]
  ]

  if server_config["hide_gui"]:
    command_args.append("nogui")

  print(f"[INFO]: Running command: {' '.join(command_args)}")
  os.execvp("java", command_args)

def main():
  cli_args = sys.argv[1:] if len(sys.argv) > 1 else [""]
  command = cli_args[0]

  match command:
    case "start":
      start_server()
    case "":
      print("[ERROR]: No command was provided")
    case _:
      print(f"[ERROR]: Unknown command: {command}")

if __name__ == "__main__":
  main()