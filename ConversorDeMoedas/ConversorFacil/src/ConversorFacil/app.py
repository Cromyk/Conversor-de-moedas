import toga
import requests
from toga.style.pack import COLUMN, ROW, CENTER
from toga.style import Pack
import toga.widgets



background = toga.images.Image(path='resources/imagens/Carbon-Fiber.png')
background_image = toga.ImageView(image=background)


class MeuAplicativo:

    def __init__(self, window=None):
        global start_time
        self.window = window
        self.image = toga.Image('resources/imagens/Carbon-Fiber.png')

        # Criar as box para uso
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=0, flex=1))
        self.content = toga.Box(style=Pack(direction=COLUMN, padding=10))
        self.box1 = toga.Box(style=Pack(direction=ROW, padding=5))  # linha 1
        self.box2 = toga.Box(style=Pack(direction=ROW, padding=5))  # linha 2
        self.box3 = toga.Box(style=Pack(direction=ROW, padding=5))  # linha 5
        self.box4 = toga.Box(style=Pack(direction=ROW, padding=5))  # linha6
        self.box5 = toga.Box(style=Pack(direction=ROW, padding=5))  # linha7
        self.box6 = toga.Box(style=Pack(direction=ROW, padding=5))  # linha8

        # ELEMENTOS:
        self.moeda1 = toga.Button(f'Dólar:\n R$ {self.pega_cotacao("USD")}', style=Pack(
            font_size=16,
            width=180, height=70,
            padding=5))
        self.moeda2 = toga.Button(f'Euro:\n R$ {self.pega_cotacao("EUR")}', style=Pack(
            font_size=16,
            width=180, height=70,
            padding=5))
        self.moeda3 = toga.Button(f'Ethereum:\n R$ {self.pega_cotacao("ETH")}', style=Pack(
            font_size=16,
            width=180, height=70,
            padding=5))
        self.moeda4 = toga.Button(f'Bitcoin:\n R$ {self.pega_cotacao("BTC")}', style=Pack(
            font_size=16,
            width=180, height=70,
            padding=5))

        self.button = toga.Button('Atualizar', on_press=self.atualizar,
                                  style=Pack(font_size=12, padding=15))

        self.feedback = toga.Label('Iniciado', style=Pack(font_size=10, padding=15))

        self.lista1 = toga.Selection(items=['Real-BRL', 'Dólar-USD', 'Euro-EUR', 'Bitcoin-BTC', 'Ethereum-ETH'], id='Lista1',
                                style=Pack(padding=5, font_size=12, width=180, height=45))

        self.lista2 = toga.Selection(items=['Real-BRL', 'Dólar-USD', 'Euro-EUR', 'Bitcoin-BTC', 'Ethereum-ETH'], id='Lista2',
                                style=Pack(padding=5, font_size=12, width=180, height=45))
        self.valor =toga.NumberInput(style=Pack(padding=5, font_size=12, width=180, height=45))

        conversao = toga.Button('Conversão',on_press=self.calcular, style=Pack(padding=5, font_size=12, width=180, height=45))
        self.resultado= toga.Label('', style=Pack(padding=5, font_size=20, width=180, height=45))


        # MONTAGEM DAS BOX
        self.box1.add(self.moeda1, self.moeda2),  # primeira linha
        self.box2.add(self.moeda3, self.moeda4),  # segunda linha
        self.box3.add(
            toga.Label('Sua moeda:', style=Pack(padding=5, font_size=12, width=180, height=45)),
            toga.Label('Moeda alvo:', style=Pack(padding=5, font_size=12, width=180, height=45))
        )
        self.box4.add(self.lista1, self.lista2)
        self.box5.add(self.valor,conversao)
        self.box6.add(self.resultado)

        self.content.add(
            self.box1,
            self.box2,
            self.button,
            self.feedback,
            self.box3,
            self.box4,
            self.box5,
            self.box6,
        )
        # Insere todo o conteudo na Main_BOX
        self.main_box.add(self.content)

    def atualizar(self, widget):
        self.moeda1 = toga.Button(f'Dólar:\n R$ {self.pega_cotacao("USD")}')
        self.moeda2 = toga.Button(f'Euro:\n R$ {self.pega_cotacao("EUR")}')
        self.moeda3 = toga.Button(f'Ethereum:\n R$ {self.pega_cotacao("ETH")}')
        self.moeda4 = toga.Button(f'Bitcoin:\n R$ {self.pega_cotacao("BTC")}')
        self.feedback.text = 'Atualizado'
        self.window.info_dialog('Atualização', "valores atualizados!")

    def pega_cotacao(self, moeda):
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f'{moeda}BRL']['bid']
        return cotacao

    def limpar_feedback(self):
        self.feedback.text = ' '

    def calcular(self,widget):
        moeda_origem = self.lista1.value[-3:]
        moeda_destino = self.lista2.value[-3:]

        valor_origem = self.valor.value
        if moeda_origem == moeda_destino:
            self.resultado.text = valor_origem
            return
        if moeda_origem == 'BRL':
            cotacao_destino = float(self.pega_cotacao(moeda_destino))
            cotacao_origem = 1
        elif moeda_destino =='BRL':
            cotacao_origem = self.pega_cotacao(moeda_origem)
            cotacao_destino = 1
        else:
            cotacao_destino = self.pega_cotacao(moeda_destino)
            cotacao_destino = float(cotacao_destino)
            cotacao_origem = self.pega_cotacao(moeda_origem)
            cotacao_origem= float(cotacao_origem)



        resultado = (float(valor_origem) / float(cotacao_destino)) * float(cotacao_origem)
        self.resultado.text = f'{resultado:.2f} {moeda_destino}'

class Main(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = background_image
        self.main_window.content = MeuAplicativo(self.main_window).main_box
        self.main_window.show()


def main():
    return Main()
