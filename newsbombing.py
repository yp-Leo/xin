def keyboard_input(string):
	from pynput.keyboard import Key,Controller
	keyboard= Controller()  #开始是控制键盘
	keyboard.type(string)
	return None

def mouse_click():
	mouse=Controller()
	mouse.press(Button.left) #按住鼠标左键
	mouse.release(Button.left) #松开鼠标左键
	return None
def main(number,string):
	import time
	time.sleep(5)
	for i in range(number):
		keyboard_input(string)
		mouse_click()
		time.sleep(0.2)


if __name__ == '__main__':
	main(20,'不知道你在说什么呢')