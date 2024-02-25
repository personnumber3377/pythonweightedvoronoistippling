
# This implements the Lloyd's algorithm, which evenly spaces out points.

class Lloyd:
	def __init__(self, points: list, constrain=False) -> None: # Constructor.
		self.points = points
		self.bounds = self.get_bounds() # This is such that we can draw a bounding box around the points such that they do not fly into outer space. Returns a list of [min_x, max_x, min_y, max_y]
		assert not self.ensure_no_duplicates() # There shouldn't be any duplicates.
		self.should_constrain = constrain
		self.construct_voronoi()

	def get_bounds(self) -> list: # gets the bounds of the points.
		x_vals = [p[0] for p in self.points]
		y_vals = [p[1] for p in self.points]
		return [min(x_vals), max(x_vals), min(y_vals), max(y_vals)]

	def ensure_no_duplicates(self) -> None:
		# Check such that no two points have the exact same coordinates.
		checked_points = set()
		for p in self.points:
			if p in checked_points:
				return True # There ARE duplicates
			else:
				checked_points.add(tuple(p))
		return False # No duplicates.

