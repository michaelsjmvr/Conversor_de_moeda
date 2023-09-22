import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

# Defina sua chave da API do Google aqui
API_KEY = "sua_api_key_aqui"

# Classe principal da aplicação
class ConversorMoedas(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conversor de Moedas")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Campos de entrada para as moedas
        self.moeda_origem_input = QLineEdit(self)
        self.moeda_origem_input.setPlaceholderText("Moeda de origem (ex: USD)")
        self.moeda_destino_input = QLineEdit(self)
        self.moeda_destino_input.setPlaceholderText("Moeda de destino (ex: BRL)")

        # Botão para realizar a conversão
        self.converter_button = QPushButton("Converter", self)
        self.converter_button.clicked.connect(self.converter_moedas)

        # Rótulo para exibir o resultado
        self.resultado_label = QLabel(self)

        # Adiciona os elementos ao layout vertical
        layout.addWidget(self.moeda_origem_input)
        layout.addWidget(self.moeda_destino_input)
        layout.addWidget(self.converter_button)
        layout.addWidget(self.resultado_label)

    # Método para converter as moedas
    def converter_moedas(self):
        # Obtém as moedas de origem e destino dos campos de entrada
        moeda_origem = self.moeda_origem_input.text().strip().upper()
        moeda_destino = self.moeda_destino_input.text().strip().upper()

        # Verifica se as moedas de origem e destino foram fornecidas
        if not moeda_origem or not moeda_destino:
            self.mostrar_mensagem("Erro", "Digite as moedas de origem e destino.")
            return

        # Verifica se o usuário deseja encerrar o programa
        if moeda_origem.lower() in ("sair", "exit", "encerrar", "fechar") or \
           moeda_destino.lower() in ("sair", "exit", "encerrar", "fechar"):
            self.mostrar_mensagem("Encerrando", "Encerrando o programa...")
            sys.exit()

        # Cria a URL da API do Google para obter a taxa de câmbio
        url = f"https://www.googleapis.com/currency/exchange/v1/conversion?q={moeda_origem}_{moeda_destino}&key={API_KEY}"

        # Faz a solicitação da API e armazena a resposta em uma variável
        response = requests.get(url)

        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            # Extrai a taxa de câmbio da resposta JSON
            data = response.json()
            taxa_cambio = data.get("result")

            if taxa_cambio is not None:
                # Exibe a taxa de câmbio no rótulo
                resultado = f"1 {moeda_origem} = {taxa_cambio:.2f} {moeda_destino}"
                self.resultado_label.setText(resultado)
            else:
                self.mostrar_mensagem("Erro", f"Moeda de destino '{moeda_destino}' não encontrada.")
        else:
            # Caso contrário, exibe uma mensagem de erro
            self.mostrar_mensagem("Erro", "Ocorreu um erro ao consultar a API.")

    # Método para mostrar uma mensagem em uma caixa de diálogo
    def mostrar_mensagem(self, titulo, mensagem):
        mensagem_box = QMessageBox(self)
        mensagem_box.setWindowTitle(titulo)
        mensagem_box.setText(mensagem)
        mensagem_box.setStandardButtons(QMessageBox.Ok)
        mensagem_box.exec()

# Função principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    conversor = ConversorMoedas()
    conversor.show()
    sys.exit(app.exec())
