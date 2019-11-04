import os

class Config:
	HOST = 'ec2-23-21-87-183.compute-1.amazonaws.com'
	DATABASE = 'd88uimb8o1icuj'
	USERNAME = 'mnofjufewttlml'
	PASSWORD = 'ba1363f48f60105758ebc4cc01b7706e56165b358bcd1a837077271027a2dfe9'
	PORT = '5432'
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

SECRET_KEY = 'the random string'
