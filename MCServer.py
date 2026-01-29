import os

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
    f"-Xms{server_ram["min"]}",
    f"-Xmx{server_ram["max"]}",
    "-jar",
    server_config["jarfile"]
  ]

  if server_config["hide_gui"]:
    server_command_args.append("nogui")

  print(f"[INFO]: Running command: {' '.join(server_command_args)}")
  os.execvp("java", server_command_args)

def main():
  start_server()

if __name__ == "__main__":
  main()