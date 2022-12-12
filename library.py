# 2022 Collin Brown
# https://github.com/dacoolinus
Import('env')
from os.path import join, realpath
from pathlib import Path
from SCons.Script import (AlwaysBuild, builder, COMMAND_LINE_TARGETS, Default, DefaultEnvironment)
from colorama import Fore

print('<<<<<<<<<<' + 'Adding CANboot Bootloader' + '>>>>>>>>>>')
