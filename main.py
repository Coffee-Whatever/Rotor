import kivy
from kivy.app import App
from kivy.app import runTouchApp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.context_instructions import PushMatrix, PopMatrix, Rotate

kivy.require('2.1.0')

x, y = 800, 800
Window.size = (x, y)
Window.top = 35
Window.left = 5
class Main(FloatLayout):
	def __init__(self, **kwargs):
		super(Main, self).__init__(**kwargs)
		self.rot = None
		global x
		global y
		self.L = Button(text="W lewo", size_hint=(0.2, 0.1))
		self.R = Button(text="W prawo", size_hint=(0.2, 0.1))
		self.T = Label(text="0.0", size_hint=(0.2, 0.1))
		self.Im = Image(source="arrow.png")

		self.L.bind(on_press=self.press)
		self.R.bind(on_press=self.press)
		self.L.bind(on_release=self.release)
		self.R.bind(on_release=self.release)

		self.add_widget(self.L)
		self.add_widget(self.R)
		self.add_widget(self.T)
		self.add_widget(self.Im)

		self.clock = None
		self.clock2 = Clock.schedule_interval(self.update_visuals, 0.5)

	def press(self, butt="finally this is useful"):
		if butt != "finally this is useful":
			if butt.text == "W lewo":
				self.clock = Clock.schedule_interval(self.rotate_L, 0.01)
			else:
				self.clock = Clock.schedule_interval(self.rotate_R, 0.01)
		pass
	def release(self, butt="but not here..."):
		if butt != "but not here...":
			Clock.unschedule(self.clock)
		pass
	def rotate_L(self, really):
		if float(self.T.text) == 0.0:
			self.T.text = "359.9"
		else:
			self.T.text = str(round(float(self.T.text) - 0.1, 1))
		self.update(0.1)
		pass
	def rotate_R(self, really):
		if float(self.T.text) == 359.9:
			self.T.text = "0"
		else:
			self.T.text = str(round(float(self.T.text) + 0.1, 1))
		self.update(-0.1)
		pass
	def update(self, sign):
		with self.Im.canvas.before:
			PushMatrix()
			self.rot = Rotate()
			self.rot.axis = (0, 0, 1)
			self.rot.origin = self.center
			self.rot.angle = sign
		with self.Im.canvas.after:
			PopMatrix()
	def update_visuals(self, really):
		global x, y
		x, y = Window.size
		self.L.pos = (((1/3*x) - (0.5*0.2*x)), ((0.7*y) - (0.1*y*0.5)))
		self.R.pos = (((2/3*x) - (0.5*0.2*x)), ((0.7*y) - (0.1*y*0.5)))
		self.T.pos = (((0.5*x) - (0.5*0.2*x)), ((0.4*y) - (0.1*y*0.5)))

class MyApp(App):
	@staticmethod
	def build():
		return Main()

if __name__ == '__main__':
	MyApp().run()
