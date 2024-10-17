import sys

from PyQt5.QtWidgets import *


class Window(QWidget):

  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Cadastro")
    self.setGeometry(50, 50, 350, 350)
    
    self.UI()

  def UI(self):

    self.username_line_edit = QLineEdit(parent=self)
    self.username_line_edit.setPlaceholderText("Por favor entre com o seu nome")

    self.date_nasc_line_edit = QLineEdit(parent=self)
    self.date_nasc_line_edit.setPlaceholderText("01/01/2024")
    self.date_nasc_line_edit.setInputMask("99/99/9999")


    self.address_line_edit = QLineEdit(parent=self)
    self.address_line_edit.setPlaceholderText("Por favor entre com o seu endereço")

    self.cpf_line_edit = QLineEdit(parent=self)
    self.cpf_line_edit.setPlaceholderText("000.000.000-00")
    self.cpf_line_edit.setInputMask("999.999.999-99")

    self.rg_line_edit = QLineEdit(parent=self)
    self.rg_line_edit.setPlaceholderText("00.000.000-0")
    self.rg_line_edit.setInputMask("99.999.999-9")

    self.phone_line_edit = QLineEdit(parent=self)
    self.phone_line_edit.setPlaceholderText("(00) 00000-0000")
    self.phone_line_edit.setInputMask("(99) 99999-9999")

    button = QPushButton("Salvar", self)
    button.clicked.connect(self.getValues)
    self.show()

    layout = QFormLayout()
    layout.addRow("Nome: ", self.username_line_edit)
    layout.addRow("Data de Nascimento: ", self.date_nasc_line_edit)
    layout.addRow("Endereço: ", self.address_line_edit)
    layout.addRow("CPF: ", self.cpf_line_edit)
    layout.addRow("RG: ", self.rg_line_edit)
    layout.addRow("Telefone: ", self.phone_line_edit)

    layout.addRow(button)
    

    self.setLayout(layout)

  def getValues(self):
    name = self.username_line_edit.text()
    date_nasc = self.date_nasc_line_edit.text()
    address = self.address_line_edit.text()
    cpf = self.cpf_line_edit.text()
    rg = self.rg_line_edit.text()
    phone = self.phone_line_edit.text()

    QMessageBox.information(None, "Info", f"""O nome é: {name}\nData de nascimento: {date_nasc}\nEndereço: {address}\nCPF: {cpf}\nRG: {rg}\nTelefone: {phone}""")
  
def main():
  app = QApplication(sys.argv)
  win = Window()
  win.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()