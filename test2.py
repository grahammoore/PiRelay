import PiRelay2
import time

PiRelay2.Board.init()

r1 = PiRelay2.Board.RELAY_1
r2 = PiRelay2.Board.RELAY_2
r3 = PiRelay2.Board.RELAY_3
r4 = PiRelay2.Board.RELAY_4

PiRelay2.Board.output_on()

r1.on()
time.sleep(2)
r1.off()
time.sleep(2)

r2.on()
time.sleep(2)
r2.off()
time.sleep(2)

r3.on()
time.sleep(2)
r3.off()
time.sleep(2)

r4.on()
time.sleep(2)
r4.off()
time.sleep(2)
