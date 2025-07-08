from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="GalacticBattle",
    version="1.0",
    description="GalacticBattle app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)