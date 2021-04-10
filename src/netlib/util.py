class Object(dict):

	def __init__(self, **kwargs):
		super().__init__(kwargs)

	def __getattr__(self, i):
		if i in self:
			return self[i]
		else: return super().__getattr__(i)

	def __setattr__(self, i, x):
		if i in self:
			self[i] = x
		else: super().__setattr__(i, x)

	def copy(self):
		return Object(**self)

class Template(dict):

	def __init__(self, *args, **kwargs):
		values = dict()
		for i in range(len(args)):
			values[args[i]] = None
		for i in kwargs:
			values[i] = kwargs[i]
		super().__init__(values)

	def __call__(self, *args, **kwargs):
		values = dict()
		keys = list(self.keys())
		for i in range(len(keys)):
			if i < len(args):
				values[keys[i]] = args[i]
			elif keys[i] in kwargs:
				values[keys[i]] = kwargs[keys[i]]
			else: values[keys[i]] = self[keys[i]]
		return Object(**values)

