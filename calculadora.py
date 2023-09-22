import sys  # Importa o módulo 'sys' para interagir com o sistema operacional
from PySide6.QtCore import Qt  # Importa o módulo 'Qt' do PySide6 para recursos de GUI
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel

# Cria uma classe 'Calculadora' que herda de QMainWindow
class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")  # Define o título da janela
        self.setGeometry(100, 100, 300, 300)  # Define a posição e o tamanho da janela

        central_widget = QWidget(self)  # Cria um widget central para a janela
        self.setCentralWidget(central_widget)  # Define o widget central

        layout = QGridLayout(central_widget)  # Cria um layout de grade para organizar os elementos

        self.result_label = QLabel(self, alignment=Qt.AlignmentFlag.AlignRight)  # Cria um rótulo alinhado à direita
        layout.addWidget(self.result_label, 0, 0, 1, 4)  # Adiciona o rótulo à grade (linha 0, coluna 0, rowspan 1, colspan 4)

        buttons = [  # Lista de textos dos botões
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        # Dicionário de posições dos botões na grade
        button_positions = [(i, j) for i in range(1, 5) for j in range(4)]

        for button_text, (i, j) in zip(buttons, button_positions):
            button = QPushButton(button_text)  # Cria um botão com o texto especificado
            button.clicked.connect(self.on_button_click)  # Conecta o sinal 'clicked' do botão a um manipulador de clique
            layout.addWidget(button, i, j)  # Adiciona o botão à grade na posição especificada

        self.current_input = ""  # Inicializa a entrada atual
        self.current_operation = None  # Inicializa a operação atual
        self.first_operand = None  # Inicializa o primeiro operando

    # Função chamada quando um botão é clicado
    def on_button_click(self):
        button_text = self.sender().text()  # Obtém o texto do botão clicado

        if button_text.isdigit() or button_text == ".":
            # Se o botão for um dígito ou ponto, adiciona à entrada atual
            self.current_input += button_text
            self.result_label.setText(self.current_input)
        elif button_text in "+-*/":
            # Se o botão for um operador, verifica se é a primeira operação
            if self.current_input:  # Verifica se a entrada não está vazia
                self.first_operand = float(self.current_input)
                self.current_input = ""
                self.current_operation = button_text
        elif button_text == "=":
            # Se o botão for igual, calcula o resultado
            if self.current_operation and self.current_input:
                second_operand = float(self.current_input)
                operators = {"+": lambda x, y: x + y,
                             "-": lambda x, y: x - y,
                             "*": lambda x, y: x * y,
                             "/": lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"}
                operation = operators.get(self.current_operation)
                if operation:
                    result = operation(self.first_operand, second_operand)
                    self.result_label.setText(str(result))
                else:
                    self.result_label.setText("Operação inválida")
                self.current_input = ""
                self.first_operand = None
                self.current_operation = None
        else:
            self.current_input = ""

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Inicializa a aplicação Qt
    calc = Calculadora()  # Cria uma instância da classe 'Calculadora'
    calc.show()  # Exibe a janela da calculadora
    sys.exit(app.exec())  # Executa o loop de eventos da aplicação
