from vector import Vector as vect

class Light(object):
	def __init__(self, color):
		self.color = color

class Sky(Light):
	def __init__(self, color, height):
		Light.__init__(self, color)
		self.height = height 

	def find_normal(self, point):
		return vect(0,-1,0)

	def find_intersection(self, origin, ray):
		if ray[1] < 0:
			return None
		else:
			unit_ray = ray.normalize()
			distance_from_sky = self.height - origin[1] 
			intersection = origin + (distance_from_sky*unit_ray)
			return intersection

