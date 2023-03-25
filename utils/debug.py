import sys
from utils.parse import config
# set 0 to turn debug mode off
debug_level  = int(config['debug_level'])

DBUG_OFF    = 0
DBUG_DEBUG  = 1
DBUG_INFO   = 2
DBUG_ERROR  = 3

MODE = {
  'GREEN': '\033[1;32m',
  'YELLOW': '\033[1;33m',
  'BLUE': '\033[1;34m',
  'RED' : '\033[1;31m',
  'PURPRED': '\033[1;35m',
  'END' : '\033[0m'
}
def debug_help(**kwargs):
  for x in kwargs:
    print('{}:{} '.format(x,kwargs[x]),end='')
    
def ERROR(**kwargs):
    print(MODE['RED']+'[ERROR] ',end='')
    debug_help(**kwargs)
    print(MODE['END'])

def INFO(**kwargs):
  if debug_level >= DBUG_INFO:
    print(MODE['BLUE']+'[INFO ] ',end='')
    debug_help(**kwargs)
    print(MODE['END'])

def DEBUG(**kwargs):
  if debug_level >= DBUG_DEBUG:
      print('[DEBUG] ',end='')
      debug_help(**kwargs)
      print()

class Logger(object):
  def __init__(self, filename='/tmp/garbage.log', stream=sys.stdout):
    self.terminal = stream
    self.log = open(filename, 'a')

  def write(self, message):
    self.terminal.write(message)
    self.log.write(message)

  def flush(self):
    pass