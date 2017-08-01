from psycopg2 import *
from Aplication.settings.bases import *

class conectionDb(object):
  """docstring for conectionDb"""
  def __init__(self):
    self.conecta = 'dbname={0} user={1} password={2} host={3}'.format(arg["dbname"],arg["usuario"],arg["pass"],arg["host"]) 
    #super(conectionDb, self).__init__()
    #self.arg = arg
  
  def rawQuery(self, sql):
    try:
      con = connect(self.conecta)
      cursor = con.cursor()
      cursor.execute(str(sql))
      return cursor.fetchall()
    except DatabaseError as e:
    	return e
    else:
    	return 'error desconocido'