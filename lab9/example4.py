import time
def simple_timer(t):
  if t == 0:
    print("Time finish!")
  else:
    print("Waits your {} second.".format(t))
    time.sleep(1)
    simple_timer(t-1)
simple_timer(3)