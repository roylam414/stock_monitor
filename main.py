import time
import threading
import stock_monitor

def foo(stop_event):
	while True:
		if stop_event.is_set():
			print("Process timeout!!!")
			return
		stock_monitor.bot()
		time.sleep(0.25)



stop_event = threading.Event()
t = threading.Thread(target=foo, args=(stop_event,))
t.start()


time.sleep(240.0)
stop_event.set()
