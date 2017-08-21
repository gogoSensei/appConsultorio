class config(object):
  """docstring for Config"""
  SECRET_KEY = 'angelesyoshua'

class ConfigDevelop(config):
  DEBUG = True
  DATA_BASE = {"dbname" : 'consultorio201707', "usuario" : 'gradmin', "pass" : '1q2w3e4r5T', "host" : 'localhost'}
    
# class ConfigProduction(object):
#   """docstring for ClassName"""
#   def __init__(self, arg):
#     super(ClassName, self).__init__()
#     self.arg = arg
#     