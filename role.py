class Role:
	def __init__(self, roleName, roleAbility):
		self.roleName    = roleName
		self.roleAbility = roleAbility
	
	def getRoleName(self):
		return self.roleName

	def getAbility(self):
		return self.roleAbility