class Gun:
	def __init__(self, kind):
		self.kind = kind

	def bang(self):
		print('Bang!!')

class Police:
	def __init__(self):
		self.gun = None

	def acquire_gun(self, gun): #3.
		self.gun = gun

	def release_gun(self):
		gun = self.gun
		self.gun = None
		return gun

	def shoot(self):
		if self.gun:
			self.gun.bang()
		else:
			print('unable shoot!')

if __name__ == "__main__":
	p1 = Police()
	print('p1 shoots')
	p1.shoot()

	revolver = Gun('Revolver') # 1. revolver 객체를 생성하고
	p1.acquire_gun(revolver) # 2. p1.acquire_gun함수에 전달하게 되면
	p1.shoot()

	p1.release_gun()
	p1.shoot()