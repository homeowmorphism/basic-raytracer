from math import cos
from math import acos
import numpy as np
import scipy.misc as smp
import random 

from src.vector import Vector as vect
from src.display import initialize_screen, find_screen_center, find_absolute_screen_position, write_screen_pixel, display_image
from src.props.lights import Light

def random_direction(normal):
    random_vector = vect(random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1))
    unit_random_vector = random_vector.normalize()

    if normal.inner(unit_random_vector) >= 0:
        return unit_random_vector
    else:
        return -1*unit_random_vector

class Scene(object):
    def __init__(self, props):
        self.props = props

    def ray_trace(self, origin, direction):
        direction = direction.normalize()

        distances = []
        intersections = []

        for prop in self.props:
            prop_intersection = prop.find_intersection(origin, direction)
            intersections.append(prop_intersection)

            if prop_intersection is None:
                distance_from_prop = float("inf")  
            else:
                distance_from_prop = (prop_intersection-origin).norm()

            distances.append(distance_from_prop)

        if all(intersection is None for intersection in intersections):
            return black

        else: 
            index_closest_prop = np.argmin(distances)
            closest_prop = self.props[index_closest_prop]

            if isinstance(closest_prop, Light):
                normal = closest_prop.find_normal(prop_intersection)
                return closest_prop.color

            else:
                closest_intersection = intersections[index_closest_prop]

                albedo = closest_prop.albedo
                normal = closest_prop.find_normal(closest_intersection)

                new_origin = closest_intersection
                reflected_ray = random_direction(normal)

                lambertian = reflected_ray.inner(normal)

                epsilon = 1

                return lambertian*albedo.compwise_mult(self.ray_trace(new_origin + (epsilon*reflected_ray), reflected_ray))

    def shoot_rays(self, screen_width, screen_height, screen_depth, iteration_by_pixel):
        screen = initialize_screen(screen_width, screen_height)
        screen_center = find_screen_center(screen_width, screen_height, screen_depth)

        for i in range(screen_width):
            for j in range(screen_height):
                relative_position = vect(i,-j,0)
                absolute_position = find_absolute_screen_position(relative_position, screen_center)
                direction = absolute_position
                sum_of_colors = vect(0,0,0)
                total_intensity = 0

                for k in range(iteration_by_pixel):
                    color = self.ray_trace(absolute_position, direction)
                    sum_of_colors += color

                average_color = sum_of_colors/iteration_by_pixel
                
                write_screen_pixel(screen, relative_position, average_color) 
        
        display_image(screen)





