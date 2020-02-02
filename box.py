import pyglet
from pyglet.gl import *


pos = [0, 0, -20]
rot_y = 0

miConfig = Config(double_buffer=True,red_size=8, green_size=8, blue_size=8, sample_buffers=1, samples=1)
# create a pyglet window
win = pyglet.window.Window(height=500, width=500, config=miConfig)


# Create the vertex_list - 3 vertices, with 2-dimensional position data, and nothing else
vlist = pyglet.graphics.vertex_list(3, ('v2f', [0,0, 400,50, 200,300]))

# override the method that draws when the window loads
@win.event
def on_draw():
        print('Draw triggered!') #Se pinta esto en consola cuando se termina de construir la ventana
        
        
        global pos_z, rot_y

        win.clear()
    
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90, 1, 0.1, 100)
    
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    
        glTranslatef(*pos)
        glRotatef(rot_y, 0, 1, 0)

        # Render a cube
        glBegin( GL_QUADS );
        # Top face
        glColor3f(   0.0, 1.0,  0.0 );  # Green
        glVertex3f(  1.0, 1.0, -1.0 );  # Top-right of top face
        glVertex3f( -1.0, 1.0, -1.0 );  # Top-left of top face
        glVertex3f( -1.0, 1.0,  1.0 );  # Bottom-left of top face
        glVertex3f(  1.0, 1.0,  1.0 );  # Bottom-right of top face
        
        # Bottom face
        glColor3f(   1.0,  0.5,  0.0 ); # Orange
        glVertex3f(  1.0, -1.0, -1.0 ); # Top-right of bottom face
        glVertex3f( -1.0, -1.0, -1.0 ); # Top-left of bottom face
        glVertex3f( -1.0, -1.0,  1.0 ); # Bottom-left of bottom face
        glVertex3f(  1.0, -1.0,  1.0 ); # Bottom-right of bottom face
        
        # Front face
        glColor3f(   1.0,  0.0, 0.0 );  # Red
        glVertex3f(  1.0,  1.0, 1.0 );  # Top-Right of front face
        glVertex3f( -1.0,  1.0, 1.0 );  # Top-left of front face
        glVertex3f( -1.0, -1.0, 1.0 );  # Bottom-left of front face
        glVertex3f(  1.0, -1.0, 1.0 );  # Bottom-right of front face
        
        # Back face
        glColor3f(   1.0,  1.0,  0.0 ); # Yellow
        glVertex3f(  1.0, -1.0, -1.0 ); # Bottom-Left of back face
        glVertex3f( -1.0, -1.0, -1.0 ); # Bottom-Right of back face
        glVertex3f( -1.0,  1.0, -1.0 ); # Top-Right of back face
        glVertex3f(  1.0,  1.0, -1.0 ); # Top-Left of back face
        
        # Left face
        glColor3f(   0.0,  0.0,  1.0);  # Blue
        glVertex3f( -1.0,  1.0,  1.0);  # Top-Right of left face
        glVertex3f( -1.0,  1.0, -1.0);  # Top-Left of left face
        glVertex3f( -1.0, -1.0, -1.0);  # Bottom-Left of left face
        glVertex3f( -1.0, -1.0,  1.0);  # Bottom-Right of left face
        
        # Right face
        glColor3f(   1.0,  0.0,  1.0);  # Violet
        glVertex3f(  1.0,  1.0,  1.0);  # Top-Right of left face
        glVertex3f(  1.0,  1.0, -1.0);  # Top-Left of left face
        glVertex3f(  1.0, -1.0, -1.0);  # Bottom-Left of left face
        glVertex3f(  1.0, -1.0,  1.0);  # Bottom-Right of left face
        glEnd();

        # Pop Matrix off stack
        #glPopMatrix()
        glFlush()


@win.event
def on_key_press(s,m):

    global pos_z, rot_y

    if s == pyglet.window.key.W:
        pos[2] -= 1
    if s == pyglet.window.key.S:
        pos[2] += 1
    if s == pyglet.window.key.A:
        rot_y += 5
    if s == pyglet.window.key.D:
        rot_y -= 5
        
# run our pyglet app, and show the window
pyglet.app.run()

 
