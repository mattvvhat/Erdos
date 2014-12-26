def to_bin(x):
  """
  Converts an integer to a binary string
  """
  s = ""
  while x > 0:
    if x % 2 == 1: s = "1" + s
    else: s = "0" + s
    x /= 2
  return s

def to_oct(x):
  """
  Converts an integer to an octal string
  """
  s = ""
  while x > 0:
    s = "%s%s" % (x%8, s)
    x /= 8
  return s

def to_hex(x):
  """
  Converts an integer to an octal string
  """
  s = ""
  while x > 0:
    val = x % 16
    if val < 10:
      s = "%s%s" % (val, s)
    else:
      char = chr(65 + (val-10))
      s = "%s%s" % (char, s)
    x /= 16
  return s

def is_pal(x): return x == x[::-1]

MAX_VAL = 1000000000
MAX_BIN = to_bin(MAX_VAL)
MAX_BIN_LEN = len(MAX_BIN)


#
#
#
def bins(length):
  """
  """
  x = 0
  n = '0'.zfill(length)
  largest = '1' * length
  while n <> largest:
    n = to_bin(x).zfill(length)
    yield n
    if n == largest: break
    x += 1

def bin_pals_len(length):
  n = length//2
  # ...
  if length == 1: yield '1'

  elif length % 2 == 0:
    for s in bins(n):
      # if s and s[-1] != '0': yield s[::-1] + s
      yield s[::-1] + s
  # ...
  else:
    for mid in ('0', '1'):
      for s in bins(n):
        # if s and s[-1] != '0': yield s[::-1] + mid + s
        yield s[::-1] + mid + s

def bin_pals(length):
  for n in range(0, length+1):
    for k in bin_pals_len(n):
      yield k




vals = [ int(x, 2) for x in bin_pals(MAX_BIN_LEN) if x ]
vals = set(vals)
print len(vals)
vals = filter(lambda x: x <= 1000000000, vals)
vals = filter(lambda x: is_pal(to_hex(x)), vals)
vals = filter(lambda x: is_pal(to_oct(x)), vals)
vals = filter(lambda x: is_pal(to_bin(x)), vals)
print vals
print sum(vals)
