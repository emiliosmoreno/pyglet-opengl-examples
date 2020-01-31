from pyglet.gl import *

# create a pyglet window
win = pyglet.window.Window()


# Create the vertex_list - 3 vertices, with 2-dimensional position data, and nothing else
vlist = pyglet.graphics.vertex_list(3, ('v2f', [0,0, 400,50, 200,300]))

# override the method that draws when the window loads
@win.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    vlist.draw(GL_TRIANGLES)

# run our pyglet app, and show the window
pyglet.app.run()