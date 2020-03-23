from elev import Elevator

def main():
	elev = Elevator()
	elev.setSpeed(300)

	while True:
		if elev.getFloorSensorSignal() == 0:
			elev.setSpeed(300)
		elif elev.getFloorSensorSignal() == elev.NUM_FLOORS-1:
			elev.setSpeed(-300)

		if elev.getStopSignal():
			elev.setSpeed(0)
			break

main()