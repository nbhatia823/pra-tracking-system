import os


class Config:
    HOST = 'ec2-23-21-87-183.compute-1.amazonaws.com'
    DATABASE = 'd88uimb8o1icuj'
    USERNAME = 'mnofjufewttlml'
    PASSWORD = 'ba1363f48f60105758ebc4cc01b7706e56165b358bcd1a837077271027a2dfe9'
    PORT = '5432'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ADMIN_USERNAME = "mdh_admin"
    ADMIN_PASSWORD = b'$2b$12$W27zJAauOqHwX2x0nK7LWO3frFbxCHgkxhbNh.JccWYYM.G6RtQk2'
    GUEST_USERNAME = "mdh_guest"
    GUEST_PASSWORD = b'$2b$12$YYP4zDbjtIXgIOrOo0DbDup.rmmuL/vS8L2ud6V0bAgT/jsX2zJyK'


SECRET_KEY = 'theeeeeee random string'
