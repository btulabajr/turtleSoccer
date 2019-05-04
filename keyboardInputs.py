# from: https://stackoverflow.com/questions/13207678/whats-the-simplest-way-of-detecting-keyboard-input-in-python-from-the-terminal

from pynput import keyboard

keyList = list()
key = ' '

def on_press(key):
	# try:
	# 	print(key.char, 'pressed')
	# except AttributeError:
	# 	print(key, 'pressed')
	if key not in keyList:
		keyList.append(key)
		print(keyList)
	
def on_release(key):
	
	if key in keyList: 
		keyList.remove(key)
		print(keyList)
	if key == keyboard.Key.esc:
		return False

with keyboard.Listener(
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()