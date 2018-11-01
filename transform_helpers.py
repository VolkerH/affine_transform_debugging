import numpy as np
import matplotlib.pyplot as plt

def get_transformed_corners(aff, vol, zeroindex=True):
    ''' given an affine transformation matrix for a volume
    and a corresponding volume vol. This function will return
    the positions of the corner points after the mapping.
    '''

    d0, d1, d2 = vol.shape
    # these give the dimensions of the array
    # the maximum index is one less
    if zeroindex:
        d0 -= 1
        d1 -= 1
        d2 -= 1
    # all corners of the input volume
    corners_in = [ ( 0,  0,  0, 1), \
                   (d0,  0,  0, 1), \
                   ( 0, d1,  0, 1), \
                   ( 0,  0, d2, 1), \
                   ( d0, d1, 0, 1), \
                   ( d0,  0,d2, 1), \
                   (  0, d1, d2, 1),\
                   ( d0, d1, d2, 1)] \
    
    corners_out = list(map(lambda c: aff @ np.array(c), corners_in))

    corner_array =  np.concatenate(corners_out).reshape((-1,4))
    #print(corner_array)
    return(corner_array)    

def get_projections(in_array, fun=np.max):
    """ given an array, projects along each axis using the function fun (defaults to np.max).
    Returns a mapping (iterator) of projections """

    projections = map(lambda ax: fun(in_array, axis=ax), range(in_array.ndim))
    return projections

def plot_all(imlist, backend = "matplotlib"):
    """ given a list of images, plots all of them in order
    Will add different backends later """
    for im in imlist:
        plt.imshow(im)
        plt.show()


def imprint_coordinate_system(volume, origin=(0,0,0), l=100, w=5, vals=(6000, 10000, 14000)):
    """ imprints coordinate system axes in a volume at origin
    axes imprints have length l and widht w and intensity values in val """
    o = origin
    volume[o[0]:o[0]+l, o[1]:o[1]+w, o[2]:o[2]+w] = vals[0]
    volume[o[0]:o[0]+w, o[1]:o[1]+l, o[2]:o[2]+w] = vals[1]
    volume[o[0]:o[0]+w, o[1]:o[1]+w, o[2]:o[2]+l] = vals[2]
    
    