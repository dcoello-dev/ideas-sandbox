import fcntl
import termios

BACKSPACE = '\x08'


def write_on_parent_shell(cmd: str, NB: int = 0):
    backspace = BACKSPACE * NB
    cmd = f"{backspace}{cmd}\n"
    for c in cmd:
        fcntl.ioctl(2, termios.TIOCSTI, c)
