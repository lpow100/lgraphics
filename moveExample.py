import lgraphics as lg
import time
from threading import Thread
def moveloop():
    while(lg.running()):
        if(lg.Input.get_keypress("d")):
            window.move(square,10,0)
        elif(lg.Input.get_keypress("a")):
            window.move(square,-10,0)
        if(lg.Input.get_keypress("w")):
            window.move(square,0,-10)
        elif(lg.Input.get_keypress("s")):
            window.move(square,0,10)
        time.sleep(0.25)
i = 0
window = lg.Window(300,300,"test",lg.RGB(255,255,255))
window.clear_screen()
square = window.create_square(-30,-30,30,30,lg.RGB(255,0,0))
x = Thread(target=moveloop)
x.start()
while(lg.running()):
    lg.update(window)
lg.quit()
exit()
