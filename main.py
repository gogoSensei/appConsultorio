from Aplication.App import *

if (__name__=='__main__'):
  csrf.init_app(app)
  app.run(port=5000)
