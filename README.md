### Hi, I'm Michael D.🤙

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/michael-douglas-640a11180/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/michael.douglaspdl/)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://web.facebook.com/MikeeD.Cloud9/)


# Projeto: Conversor de Moedas com Interface Gráfica

## Visão Geral
Este projeto é um conversor de moedas que permite aos usuários converter valores de uma moeda para outra utilizando taxas de câmbio atualizadas. O programa possui uma interface gráfica simples para a entrada de moedas de origem e destino e exibe o resultado da conversão.

## Funcionalidades
- O programa utiliza a API do Google para obter as taxas de câmbio atualizadas.
- Os campos de entrada permitem ao usuário especificar a moeda de origem e destino.
- Ao clicar no botão "Converter", o programa consulta a API, obtém a taxa de câmbio e exibe o resultado no rótulo.
- O programa permite ao usuário encerrar a aplicação digitando "sair" ou "exit" nas moedas de origem ou destino.

## Componentes Principais
1. `ConversorMoedas` (Classe QMainWindow):
   - Representa a janela principal da aplicação.
   - Contém campos de entrada para as moedas de origem e destino, um botão de conversão e um rótulo para exibir o resultado.
   - Possui um método `converter_moedas` que realiza a conversão com base nas moedas fornecidas.
   - Exibe mensagens de erro ou encerramento em caixas de diálogo.

2. `moeda_origem_input` (QLineEdit):
   - Campo de entrada para a moeda de origem.

3. `moeda_destino_input` (QLineEdit):
   - Campo de entrada para a moeda de destino.

4. `converter_button` (QPushButton):
   - Botão para iniciar a conversão.

5. `resultado_label` (QLabel):
   - Rótulo para exibir o resultado da conversão.

## Requisitos
- É necessário ter a chave da API do Google para utilizar o serviço de taxas de câmbio.

## Como Usar
1. Execute o programa.
2. Insira a moeda de origem (por exemplo, "USD") no campo apropriado.
3. Insira a moeda de destino (por exemplo, "BRL") no campo correspondente.
4. Clique no botão "Converter" para ver o resultado da conversão.
5. Para encerrar o programa, digite "sair" ou "exit" em qualquer campo de moeda.

## Dependências
- PySide6: A biblioteca PySide6 é usada para criar a interface gráfica.
- Requests: A biblioteca requests é utilizada para fazer solicitações à API do Google.

## Executando o Projeto
1. Certifique-se de ter as dependências instaladas.
2. Substitua `"sua_api_key_aqui"` na variável `API_KEY` pelo seu próprio token de API do Google.
3. Execute o script Python.

## Contribuições
Contribuições são bem-vindas. Sinta-se à vontade para melhorar este projeto e enviar sugestões ou correções.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

---

Espero que este arquivo.md ajude a documentar e explicar seu projeto. Lembre-se de substituir `"sua_api_key_aqui"` pela sua chave de API real para o funcionamento correto do programa.
