from vector import Vector as vect
from colorlib import *

class Floor(object):
	def __init__(self, height, albedo):
		self.height = height
		self.albedo = albedo.normalize()

	def find_intersection(self, origin, ray):
		if ray[1] >= 0:
			return None
		else:
			unit_ray = ray.normalize()
			distance_from_floor = origin[1] - self.height
			intersection = origin + (distance_from_floor*unit_ray)

			return intersection

	def find_normal(origin, point):
		return vect(0,1,0).normalize()

class LeftWall(object):
	def __init__(self, xcoord, albedo):
		self.xcoord = xcoord
		self.albedo = albedo.normalize()

	def find_intersection(self, origin, ray):
		if ray[0] >= 0:
			return None
		else:
			unit_ray = ray.normalize()
			distance_from_wall = origin[0] - self.xcoord

			if distance_from_wall < 0:
				return None
			
			else:
				intersection = origin + (distance_from_wall*unit_ray)

			return intersection

	def find_normal(origin, point):
		return vect(-1,0,0).normalize()

class RightWall(object):
	def __init__(self, xcoord, albedo):
		self.xcoord = xcoord
		self.albedo = albedo.normalize()

	def find_intersection(self, origin, ray):
		if ray[0] >= 0:
			return None
		else:
			unit_ray = ray.normalize()
			distance_from_wall = self.xcoord - origin[0]

			if distance_from_wall < 0:
				return None
			
			else:
				intersection = origin + (distance_from_wall*unit_ray)

			return intersection

	def find_normal(origin, point):
		return vect(1,0,0).normalize()
