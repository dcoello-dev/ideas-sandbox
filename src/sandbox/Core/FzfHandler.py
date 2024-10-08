import os
import sys
import pathlib
from pyfzf.pyfzf import FzfPrompt


def sniff_dir(dir):
    dd = pathlib.Path(dir)
    ret = []
    for elem in dd.iterdir():
        if os.path.isfile(elem):
            ret.append(elem)
        else:
            ret += sniff_dir(elem)
    return ret


def fzf_handler(elems):
    fzf = FzfPrompt()
    ret = fzf.prompt(elems)
    if len(ret) == 0:
        sys.exit(0)
    return ret[0]
