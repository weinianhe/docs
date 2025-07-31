#import subprocess
from pywinauto import Application, Desktop
import pyautogui

#process = subprocess.Popen(["notepad.exe"])
#app = Application(backend="win32").start("notepad.exe")
#main_window = app.window(title = "Untitled - NotepadDialog")
#main_window.show()
#main_window.set_focus()
#app.set_focus()
#app.UntitledNotepadDialog.set_focus()
app = Application(backend='win32').start('notepad.exe')
#https://github.com/pywinauto/pywinauto/issues/1375
dlg = Desktop(backend='win32')['Untitled - NotepadDialog']
#dlg.Edit.set_edit_text("Hello World")
pyautogui.PAUSE = 2.5
#pyautogui.locateOnScreen(r'c:\temp\notepadmenu.png')
#pyautogui.click(x=left,y=top+height+5,clicks=1,interval=1,button='left')
pyautogui.typewrite("hello world\n", interval=0.3)