from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
import requests




class Ui(ScreenManager):
	pass

class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		Builder.load_file('desing.kv')
		self.url ="https://news4geek-c1ca7-default-rtdb.firebaseio.com/.json"
		self.key='74NzXMR6QMv9xO5xCWhpYRMxHxSA8J6Li6gYl4yH'
		return Ui()

	def login_data(self):
		user = self.root.ids.user.text
		password = self.root.ids.password.text
		state =False
		data = requests.get(self.url +'?auth='+self.key)

		for key, value in data.json().items():
			user_reg=value['User']
			password_reg =value['Password']

			if user == user_reg:
				if password==password_reg:
					state=True
					self.root.ids.signal_login.text =''
					self.root.ids.user.text =''
					self.root.ids.password.text =''
				else:
					self.root.ids.signal_login.text ='Contraseña incorrecta'
					self.root.ids.user.text =''
					self.root.ids.password.text =''
			else:
				self.root.ids.signal_login.text ='Usuario incorrecta'
				self.root.ids.user.text =''
				self.root.ids.password.text =''
		return state

	def register_data(self):
		state= 'datos incorrectos'

		user = user = self.root.ids.new_user.text
		password = self.root.ids.new_password.text
		data = requests.get(self.url +'?auth='+self.key)

		if(len(user)<=4):
			state='Nombre muy corto'
		else:
			for key, value in data.json().items():
				User = value['User']
				if user== User:
					state= 'Este usuario ya existe'
					break
			if user!= User:
				state= 'Registrado correctamente'
				send_data ={user:{'User':user,'Password':password}}
				requests.patch(url=self.url, json=send_data)
				self.root.ids.signal_register.text=state
		
		self.root.ids.signal_register.text=state
		self.root.ids.new_user.text=''
		self.root.ids.new_password.text=''
		return state
	
	def clear_signal(self):
		self.root.ids.signal_register.text=''
		self.root.ids.signal_login.text=''
	
if __name__=="__main__":
	MainApp().run()
