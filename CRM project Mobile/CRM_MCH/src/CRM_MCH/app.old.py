"""
Aplicatico mobile CRM para controle e acompanhando de relacionamentos de clientes e estatisticas
"""
import toga
import pandas as pd
from toga.style.pack import COLUMN, Pack

error = ''
usuarios = []
userfile = 'user.txt'
def validaArquivo(userfile):
    try:
        a = open(userfile,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criaArquivo(userfile):
    try:
        a = open(userfile,'wt+')
        a.close()
    except: print('erro ao criar arquivo')

if validaArquivo(userfile):
    print('arquivo localizado')
else:
    criaArquivo(userfile)



class Registro:
    def __init__(self,window=None):
        self.window = window
        self.registerBox = toga.Box(style=Pack(direction=COLUMN))
        try:
            a = open(userfile, 'rt')
            a.close()
        except:
            return
        else:

            self.registerNameLabel = toga.Label('Nome de usuário:')
            self.registerPassLabel = toga.Label('Senha do usuário:')
            self.registerButton = toga.Button('Registrar', on_press=self.Registro, style=Pack(padding=10))
            self.userNameRegister = toga.TextInput(placeholder='Usuário...', style=Pack(padding=10))
            self.userPassRegister = toga.TextInput(placeholder='Senha...', style=Pack(padding=10))
            self.backButton = toga.Button('Voltar', on_press=LoginBox, style=Pack(padding=10))
            self.registerBox.add(
                self.registerNameLabel,
                self.userNameRegister,
                self.registerPassLabel,
                self.userPassRegister,
                self.registerButton,
                self.backButton
            )

    def Registro(self):
        global usuarios
        usuarios.append('{"user":{},"pass":{}}'.format(self.userNameRegister,
                                                       self.userPassRegister))

        file = open(userfile, 'wt')
        file.write(usuarios)
        file.close()
        return




class SuccessBox:

    def __init__(self,user):
        self.box = toga.Box()
        self.titleLabel = toga.Label(f'Bem vindo{user}', style=Pack(font_size=25,font_familiy='cursive'))
        self.logoff = toga.Button('Logoff',on_press = LoginBox)
        self.user.clear()
        self.box.add(
            self.titleLabel,
            self.logoff
        )


class LoginBox:

    def __init__(self,window=None):
        self.window = window
        self.box = toga.Box()
        self.usernameLabel = toga.Label(
            'Usuário:',style=Pack(font_size=30,padding=10))
        self.passwordLabel = toga.Label(
            'Senha:', style=Pack(font_size=30,padding=10))
        self.userNameInput = toga.TextInput(
            placeholder='Usuário...',
            style=Pack(padding=10,font_size=25))
        self.passwordInput = toga.TextInput(
            placeholder='Senha...',
            style=Pack(padding=10,font_size=25))

        self.passwordInput.style.update(padding=10)
        self.errorOutput = toga.TextInput(readonly=True)

        self.loginInput = toga.Button('Login',on_press=self.login_handler)
        self.loginInput.style.update(padding=10)
        self.registerInput = toga.Button('Registro',on_press=Registro())
        self.registerInput.style.update(padding=10)

        self.box.style.update(direction=COLUMN)
        self.box.add(
            self.usernameLabel,
            self.userNameInput,
            self.passwordLabel,
            self.passwordInput,
            self.errorOutput,
            self.loginInput,
            self.registerInput
        )


    def login_handler(self,widget):
        val1 = self.userNameInput.value
        val2 = self.passwordInput.value
        flagUser = 0
        try:
            a = open(userfile,'rt')
        except:
            self.errorOutput.value = 'Login error'
            self.userNameInput.clear()
            self.passwordInput.clear()
            a.close()
            return self.errorOutput.value
        else:
            if not a:
                self.errorOutput.value = 'Crie seu login primeiro...'
                self.userNameInput.clear()
                self.passwordInput.clear()
                a.close()
            else:
                for i in a:
                    if i['user'] == val1:
                        flagUser = 1
                        if i['pass'] == val2:
                            a.close()
                            self.window.content = SuccessBox(self.userNameInput.value).box

                        else:
                            self.errorOutput.value = "Senha invalida"
                            self.userNameInput.clear()
                            self.passwordInput.clear()
                            a.close()
                if flagUser == 1:
                    self.errorOutput.value = 'Usuário invalido'
                    self.userNameInput.clear()
                    self.passwordInput.clear()
                    a.close()


class CRM(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = LoginBox(self.main_window).box
        self.main_window.show()


def main():
    return CRM()
