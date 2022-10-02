files={'auxilary.py': [], 'main.py': ['from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair\n', 'from spike.control import wait_for_seconds, wait_until, Timer\n', '\n', 'def main():\n', '    hub = PrimeHub()\n', '    while True:\n', "        hub.light_matrix.show_image('HAPPY')\n", '        wait_for_seconds(5)\n', "        hub.light_matrix.show_image('SAD')\n", '        wait_for_seconds(5)']}
for k in files:
	with open(f'./{k}', 'w') as f:
		f.write('\n'.join(files[k]))
exec('./main.py')