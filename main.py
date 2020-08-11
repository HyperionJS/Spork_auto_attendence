import pygame as pg
import time
import win32api


class Cursor:
    def __init__(self):
        self.cursor_x = 0
        self.cursor_y = 0
        self.class_ammnt = 2

    def getpos(self, class_ammnt):
        self.class_ammnt = class_ammnt
        class_count = 0
        state_left = win32api.GetKeyState(0x01)
        while True:
            #print(class_count)
            if class_count == self.class_ammnt:
                break
            a = win32api.GetKeyState(0x01)
            if a != state_left:  # Button state changed
                state_left = a
                print(a)
                if a < 0:
                    print('Left Button Pressed')
                    self.cursor_x, self.cursor_y = win32api.GetCursorPos()
                    print(self.cursor_x, self.cursor_y)

                    class_count = class_count + 1
                else:
                    pass
                    print('Left Button Released')
            time.sleep(0.001)


cursor = Cursor()
cursor.getpos(5)
