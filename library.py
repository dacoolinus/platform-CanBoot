# 2022 Collin Brown
# https://github.com/dacoolinus
Import('env')
from os.path import join, realpath
from pathlib import Path
from SCons.Script import (AlwaysBuild, builder, COMMAND_LINE_TARGETS, Default, DefaultEnvironment)
from colorama import Fore

print('<<<<<<<<<<' + 'Adding CANboot Bootloader' + '>>>>>>>>>>')

# Output Directory

# Common Command Definitions

# Source Files

# Default Compiler Flags

# Default Targets

# Include Board Specific Scons File

Export('env')
SConscript('SConscript')

# Main Build Rules

# Deployer Build Rules

# Compile Time Requests

# Auto Generation of "board/ include file link"

#Generic Rules