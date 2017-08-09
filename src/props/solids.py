from math import sin as sin
from math import cos as cos
from math import acos as acos
from math import sqrt as sqrt 

from src import colors


class Sphere(object):
    def __init__(self, center, radius, albedo=0.9*colors.white):
        self.center = center
        self.radius = radius
        self.albedo = albedo.normalize()

    def find_normal(self, point):
        return ((point - self.center).normalize())

    # for variable meanings, refer to sphere_geometry.pdf
    def find_intersection(self, screen_point, ray):
        v_vect = ray.normalize()

        pc_vect = self.center - screen_point 
        pc = pc_vect.norm()

        if pc <= self.radius:
            raise InsideSphereException

        cos_theta = v_vect.inner(pc_vect)/pc_vect.norm()

        if cos_theta < -0.1:
            return None

        theta = acos(cos_theta)

        d = sin(theta)*pc

        if d >= self.radius:
            return None

        # is else necessary here? ask Victoria

        else:
            e = sqrt(pow(self.radius,2) - pow(d,2)) 
            s = pc*cos_theta - e
            intersection_vect = screen_point + s*v_vect
            return intersection_vect

class InsideSphereException(Exception):
    '''raise when inside sphere'''
    pass


