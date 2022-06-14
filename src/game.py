# pygame to render window
import pygame as pg 
from OpenGL.GL import * 
import numpy as np
import ctypes 
# to import and use shaders from shaders dictionary
from OpenGL.GL.shaders import compileProgram, compileShader

class App: 

    # class attribute that represents the windows dimensions
    window_height = 800
    window_height = 800

    def __init__(self): 

        # initialize pygame 
        pg.init()
        #                    parses the dimensions of the window,   tells pg that opengl will be used.   DOUBLEBUF = each frame a window is parsed, while another is beinge drawed.
        pg.display.set_mode((App.window_height, App.window_height), pg.OPENGL|pg.DOUBLEBUF)
        
        # creates a universal clock for the app, to controle FPS 
        self.clock = pg.time.Clock()

        # initialize opengl
        #            R     G    B   A  32 bit 8 bit for each value, colors are normalized. there for each value is between 0 and 1, and not between 0 and 255.  
        glClearColor(0.5, 0.0, 1.0, 1)

        self.shader = self.createShader("src\shaders/vertex.txt", "src\shaders/fragment.txt")
        glUseProgram(self.shader)
        self.triangle = Triangle()

        self.mainloop()

    def createShader(self, vertexFilepath, fragmentFilepath):
        
        # imports the shaders from directory
        with open(vertexFilepath, 'r') as f:
            vertex_src = f.readlines()
      
        with open(fragmentFilepath, 'r') as f:
            fragment_src = f.readlines()

        # compailes fragment & vertex shaders into VAR:shader 
        shader = compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)

        )

        return shader 

    def mainloop(self):

        running = True 
        while running:
            # checks event
            for event in pg.event.get():
                # makes the user able to close the program, if exit button is pressed
                if (event.type == pg.QUIT):
                    running = False    
                
            # refresh the screen 
            glClear(GL_COLOR_BUFFER_BIT)
            
            # drawes the triangle
            # tells witch shader to use
            glUseProgram(self.shader)
            # tells what we are going to draw, and takes VAO data
            glBindVertexArray(self.triangle.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.triangle.vertex_count)
            
            
            # filps so that the screen is showing the new buffer, and the old is beinge updated behind the screen. 
            pg.display.flip()

            # timing 
            self.clock.tick(60)
        self.quit()

    def quit(self):
        self.triangle.destroy()
        glDeleteProgram(self.shader) 
        pg.quit()
        print("The program has ended..")

class Triangle: 

    def __init__(self):
        # x, y, z, r, g, b
        # x, y, z position in 3d space 
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,  # vertex 0
             0.5, -0.5, 0.0, 0.0, 1.0, 0.0, # vertex 1
             0.0, 0.5, 0.0, 0.0, 0.0, 1.0  # vertex 2
        )   
        
        # makes self.vertices into a data type that the GPU can read. 
        # dtype is a float with size 32bit
        self.vertices = np.array(self.vertices, dtype=np.float32)
        
        self.vertex_count = 3
        # vao = vertex array object, tells the GPU, what each index represents
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        # vbo = vertex buffer object
        # func that ships the data to the GPU
        self.vbo = glGenVertexArrays(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        # Means that we send the data once, but calls it menny times.
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        # enables a attribute, and descripes the VBO for that attribute
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))

# makes sure that the app can only be runned from the main game file. 
if __name__ == "__main__": 
    myApp = App()
    print("Program has started...")
