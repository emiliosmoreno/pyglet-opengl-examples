from pyglet.gl import *

# create a pyglet window
win = pyglet.window.Window()


# Create the vertex_list - 3 vertices, with 2-dimensional position data, and nothing else
vlist = pyglet.graphics.vertex_list(3, ('v2f', [0,0, 400,50, 200,300]))

# override the method that draws when the window loads
@win.event
def on_draw():
        
       glClearColor(0, 0, 0, 1)
       glEnable(GL_DEPTH_TEST)  
       # Push Matrix onto stack
       glPushMatrix()

       #glRotatef(xRotation, 1, 0, 0)
       #glRotatef(yRotation, 0, 1, 0)

       # Draw the six sides of the cube
       glBegin(GL_QUADS)

       # White
       glColor3ub(255, 255, 255)
       glVertex3f(50,50,50)

       # Yellow
       glColor3ub(255, 255, 0)
       glVertex3f(50,-50,50)

       # Red
       glColor3ub(255, 0, 0)
       glVertex3f(-50,-50,50)
       glVertex3f(-50,50,50)

       # Blue
       glColor3f(0, 0, 1)
       glVertex3f(-50,50,-50)

         # 

       glEnd()

       # Pop Matrix off stack
       glPopMatrix()

# run our pyglet app, and show the window
pyglet.app.run()

 
