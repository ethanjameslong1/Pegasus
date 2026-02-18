import subprocess
import io
import proc
import sys
import termios
import tty


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
        case "s":
            foundFlag = False
            output = subprocess.run(["playerctl", "--list-all"])
            proc = subprocess.Popen(["prog", "arg"], stdout=subprocess.PIPE)
            for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
                if line == "Spotify":
                    subprocess.run(["playerctl", "--player=spotify", "play"])
                    foundFlag = True
