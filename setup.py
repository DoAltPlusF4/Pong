import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages=["source", "pyglet", "pymunk"], excludes=[])

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('main.py', base=base, targetName='Pong')
]

setup(name='Pong',
      version='1.1',
      description="It's pong.",
      options=dict(build_exe=buildOptions),
      executables=executables)
