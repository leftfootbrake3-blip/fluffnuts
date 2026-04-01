from cx_Freeze import setup, Executable
import os

# Use a simple path with no spaces to avoid cx_Freeze cleanup bug
build_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")

include_files = [
    "FluffnutsPro_logo.png",
    "munch.wav",
    "Fluffnutspro.ico",
]

build_options = {
    "packages": ["flask", "pystray", "keyboard", "PIL", "sqlite3",
                 "threading", "webbrowser", "urllib.request", "json",
                 "datetime", "pathlib"],
    "include_files": include_files,
    "excludes": ["test", "unittest", "tkinter", "customtkinter", "pygame"],
    "optimize": 2,
    "build_exe": build_dir,
}

setup(
    name="FluffnutsPro",
    version="4.0.0",
    description="Elite Prompt Engine by Left Foot Brake",
    options={"build_exe": build_options},
    executables=[Executable(
        "FluffnutsPro.py",
        base="Win32GUI",
        icon="Fluffnutspro.ico",
        target_name="FluffnutsPro.exe",
    )]
)
