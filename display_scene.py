import numpy as np
import scipy.misc as smp

from src.vector import Vector as vect
from src.colors import *
from src.props.solids import Sphere 
from src.props.lights import Sky 
from src.props.walls import Floor 
from src.scene import shoot_rays 

sky = Sky(white,1000)
sphere = Sphere(center=vect(-30,0,300),radius=50, albedo = 1*vect(255, 235, 49))
sphere2 = Sphere(center=vect(80,50,200),radius=70, albedo = 1*vect(255, 61, 73))
sphere3 = Sphere(center=vect(-30,-50,180),radius=50, albedo = 1*vect(142, 44, 232))
floor = Floor(-500, albedo=(0.9*white))
scene_objects = [sky, sphere, sphere2, sphere3, floor]
resolution = (100,100) #in pixels
depth = 100 #in pixels
iteration_by_pixel = 1 

shoot_rays(scene_objects, resolution[0], resolution[1], depth, 100)


