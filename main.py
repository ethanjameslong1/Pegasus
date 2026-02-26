import subprocess
import time
import pyperclip
import io
import proc
import sys
import termios
import tty

RAP_URI = "https://open.spotify.com/playlist/1meh7fDcfNbjZrOz3jIlQU?si=e583a37e9cc94f81"


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


c = "a"
while c != "q":
    print("Press a key: ")
    c = getch()
    print(f"You pressed: {c}")
    match c:
        case "a":
            subprocess.run("hns")
            filename = "./transcriptions.txt"
            try:
                clipboard_content = pyperclip.paste()
                clipboard_content += "\n###"
                if not clipboard_content:
                    print(
                        "Clipboard is empty or contains non-text data (e.g., an image). No file created."
                    )
                    break
                with open(filename, "w") as f:
                    f.write(clipboard_content)
                print(f"Successfully wrote clipboard content to {filename}")

            except pyperclip.PyperclipException as e:
                print(f"Error accessing clipboard: {e}")
            except IOError as e:
                print(f"Error writing to file: {e}")
        case "s":
            foundFlag = False
            proc = subprocess.Popen(["playerctl", "--list-all"], stdout=subprocess.PIPE)
            for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
                if line == "Spotify":
                    subprocess.run(["playerctl", "--player=spotify", "play"])
                    foundFlag = True
            if not foundFlag:
                subprocess.Popen(
                    ["spotify", "--minimized"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                time.sleep(3)
                subprocess.run(["playerctl", "--player=spotify", "play"])
        case "r":
            foundFlag = False
            proc = subprocess.Popen(["playerctl", "--list-all"], stdout=subprocess.PIPE)
            for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
                if line == "Spotify":
                    subprocess.run(["playerctl", "--player=spotify", "play"])
                    foundFlag = True
            if not foundFlag:
                subprocess.Popen(
                    ["spotify", "--minimized"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                time.sleep(3)
            subprocess.run(["playerctl", "open", RAP_URI])
