import configparser

config_file = 'server.ini'


def init():
  cf = configparser.ConfigParser()
  cf.read(config_file)
  
  params = dict()
  
  params['server_ip'] = cf.get('SERVER','ip')
  params['server_port'] = cf.get('SERVER','port')
  params['debug_level'] = cf.get('SERVER','debug_level')
  params['log_path'] = cf.get('SERVER','log_path')

  params['db_ip'] = cf.get('DB','ip')
  params['db_port'] = cf.get('DB','port')
  params['db_username'] = cf.get('DB','username')
  params['db_password'] = cf.get('DB','password')
  params['db_database'] = cf.get('DB','database')

  return params

config = init()
