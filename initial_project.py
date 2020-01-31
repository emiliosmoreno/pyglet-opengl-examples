from pyglet.gl import *

# create a pyglet window
win = pyglet.window.Window()


# override the method that draws when the window loads
@win.event
def on_draw():
    print('Draw triggered!') #Se pinta esto en consola cuando se termina de construir la ventana

# run our pyglet app, and show the window
pyglet.app.run()