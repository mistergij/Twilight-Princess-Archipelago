"""Module to scan and see if an item should be sent"""
import platform

os = platform.system()
if os == "Windows":
    import dolphin_memory_engine_windows as dme
elif os == "Linux":
    import dolphin_memory_engine_linux as dme
