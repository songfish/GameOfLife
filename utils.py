import numpy as np
def readRLE_New(filename):
    ''' Read the RLE file and returns the parameters and the pattern chain'''
    # see http://www.conwaylife.com/wiki/RLE

    # Open file and cast it into a unique string
    f = open(filename,"r")
    s = ''
    #initialize parameters
    Cshape = (0,0)
    position = (0,0)
    rH = False
    rV = False
    trim = False
    T = 0
    tp = False
    while True:
        l = f.readline()
        if l == '':             # Empty indicates end of file. An empty line would be '\n'
            break
        if l[0] =='#':
            continue
        if l[0] =='x':
            continue
        if l[0] == 'p':
            params = l.split(';')
            # 16/9 ratio
            shapeY = int(params[1]) #to remove ';'
            Cshape=(int(1.78*shapeY),shapeY)
            position=(int(params[2]),int(params[3]))
            T=int(params[4])
            rH=bool(params[5])
            rV=bool(params[6])
            trim=bool(params[7])
            tp=bool(params[8])
        else:
            s = s + l[:-1]   # To remove EOL
    f.close()
    return (Cshape,position,T,rH,rV,trim,tp,s)


def readPattern(pattern,Cshape,position,rH,rV,tp):
    """Reads the pattern, to set initial condition of the game."""
    # Create matrix
    SHAPE_MAX = (2500,2500)
    B = np.zeros(SHAPE_MAX).astype(bool)

    # We parse each character and decide accordingly what to do
    # If the character is a digit, we keep going until we reach 'b' or 'o'
    curX, curY = 0, 0
    qs = ''
    for c in pattern:

        # End of file
        if c=='':
            break

        # Next Line
        if c=='$':
            q = 1 if qs=='' else int(qs)
            curY += q
            curX = 0
            qs = ''

        # Digit (check ascii code for a digit from 0 to 9)
        if ord(c)>47 and ord(c)<58:  #
            qs = qs + c

        # Alive (o) or Dead (b) cell
        if c == 'b' or c=='o':
            q = 1 if qs=='' else int(qs)
            for i in range(q):
                B[curX, curY] = False if c=='b' else True
                curX += 1
            qs = ''


    posX, posY = position
    BshapeY=max(np.where(sum(B)>0)[0])+1
    BshapeX=max(np.where(sum(B.T)>0)[0])+1

    B = B[0:BshapeX, 0:BshapeY]

    if rV:
        B=B[:,::-1]
    if rH:
        B=B[::-1,:]
    if tp:
        B=B.T

    # C = np.zeros(Cshape)
    # C[posX:(posX+B.shape[0]),posY:(posY+B.shape[1])] = np.copy(B)
    return B.astype(bool)