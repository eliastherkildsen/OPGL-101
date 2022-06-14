# Open GL 

## requirments 

    $ pip3 install pygame 
    $ pip3 install PyOpenGL 
    $ pip3 install PyOpenGL_accelerate 
    $ pip3 install numpy

### dictionary

    - vertices is a point in a vector 
        example:       -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,  <- vector 0
                        0.5, -0.5, 0.0, 0.0, 1.0, 0.0, <- vector 1
                        0.0, 0.5, 0.0, 0.0, 0.0, 1.0  <- vector 2

        in this example index 0 through 2 represents x, y and z
        index 2 through 5 represents RGB


    - VAO = vertex array object, tells the GPU, what each index represents in VBO, so that
            the information can be processed by the GPU in the right order. 

            lets say that we are making a object, and we have som information
            ex. x, y, z, r, g, b, a
            this is stored in a buffer, call VBO 
            but if we are making more then one object, the data for alle the object will be stored in the same buffer
               
            ex BUFFER = [x, y, z, r, g, b, a, x, y, z, r, g, b, a]
            each value represents 4 bytes of data

            STRIDE = means the value from the first object to the next. 
            in this example with list:BUFFER
            object1 startes at index[0] and endes at index[6]
            object2 starts at index[7] and endes at index[13]

            the size of the stride can be calculated as 4bytes pr. number, and in this example we have 7 numbers
            witch means that we have 4 * 7 bytes = 28 bytes pr object

            we also want to know where each atribute startes, this is calculated as where in bytes.
            ex.     |---|----|---|-----------|
                    | x | 0  | > |  4 bytes  |
                    |---|----|---|-----------|
                    | y | 4  | > |  8 bytes  |
                    |---|----|---|-----------|
                    | z | 8  | > |  12 bytes |
                    |---|----|---|-----------|
                    | r | 12 | > |  16 bytes |
                    |---|----|---|-----------|
                    | g | 16 | > |  20 bytes |
                    |---|----|---|-----------|
                    | b | 20 | > |  24 bytes |
                    |---|----|---|-----------|
                    | a | 24 | > |  28 bytes |
                    |---|----|---|-----------|
            


    