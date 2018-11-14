import autopy
import urllib.request
import webbrowser
import time
import pyautogui

url = 'http://www.trex-game.skipser.com/'
webbrowser.open(url)

def find_tree(tree_x, tree_y):
	print(capture, (247,247,247))
	if capture != (247,247,247):
		print('found tree')
		return True
	else:
		return False

def find_jumping_point(x, y):
	jumping_x = 100
	jumping_y = 25
	pyautogui.press('space')

	capture = autopy.bitmap.capture_screen().get_color(jumping_y, jumping_x)

	while True:
		capture_tree = autopy.bitmap.capture_screen().get_color( jumping_y, jumping_x)
		print(capture, capture_tree)
		if capture != capture_tree:
			pyautogui.press('space')
			autopy.bitmap.capture_screen().save('images/screen_test.png')
			break
		else:
			print('not found tree')

def find_dinosor_point():
	autopy.bitmap.capture_screen().save('images/screengrab.png')
	screen  = autopy.bitmap.Bitmap.open('images/screengrab.png')
	dinosor = autopy.bitmap.Bitmap.open('images/dinosor.png')

	find_dinosor = screen.find_bitmap(dinosor)
	if find_dinosor:
		print("Found dinosor at: %s" % str(find_dinosor))
		x, y = find_dinosor
		print(x, y)

		find_jumping_point(x, y)
	else:
		print("not found dinosor .____.")

if urllib.request.urlopen(url).getcode() == 200:
	time.sleep(5)
	find_dinosor_point()
else:
	print('I\'m so sorry. This url is gone!')

