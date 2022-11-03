import parallel
import time
p = parallel.Parallel()
p.setData(0xff)
for trigger_value in range(0,256):
    print (f"Sending Trigger : {trigger_value}")
    p.setData(trigger_value)
    time.sleep(0.1)
p.setData(0x00)