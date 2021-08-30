import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog,QVBoxLayout,QWidget
from PyQt5.QtGui import QIcon
from calculator_ui import Ui_Form
from PyQt5 import QtCore

class Calculator(QMainWindow):
	def __init__(self):

		super(Calculator,self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.setWindowIcon(QIcon('calculator.ico'))
		self.last_operator = ''
		self.expression = ' '

		self.setFixedSize(249,470)
		self.setWindowTitle('Calculator')
		self.ui.result.setDisabled(True)

		self.ui.result.setPlaceholderText('0')
		self.ui.result.setMaxLength(8)
		self.ui.all_clear.hide()

		''' Signals '''
		self.ui.number0.clicked.connect(self.insertZero)
		self.ui.number1.clicked.connect(lambda :self.insertNumber('1'))
		self.ui.number2.clicked.connect(lambda :self.insertNumber('2'))
		self.ui.number3.clicked.connect(lambda :self.insertNumber('3'))
		self.ui.number4.clicked.connect(lambda :self.insertNumber('4'))
		self.ui.number5.clicked.connect(lambda :self.insertNumber('5'))
		self.ui.number6.clicked.connect(lambda :self.insertNumber('6'))
		self.ui.number7.clicked.connect(lambda :self.insertNumber('7'))
		self.ui.number8.clicked.connect(lambda :self.insertNumber('8'))
		self.ui.number9.clicked.connect(lambda :self.insertNumber('9'))
		
		self.ui.dot.clicked.connect(self.insertDot)
		self.ui.equal_btn.clicked.connect(self.equalExpression)
		self.ui.clear.clicked.connect(self.clear)
		self.ui.all_clear.clicked.connect(self.all_clear)

		self.ui.neg_pos.clicked.connect(self.negative_or_posetive)
		self.ui.percentage.clicked.connect(self.set_percentage)
		self.ui.plus_btn.clicked.connect(lambda :self.insertOperator('+'))
		self.ui.sub_btn.clicked.connect(lambda :self.insertOperator('-'))
		self.ui.div_btn.clicked.connect(lambda :self.insertOperator('/'))
		self.ui.mul_btn.clicked.connect(lambda :self.insertOperator('*'))

	def show_all_clear(self):
		self.ui.clear.hide()
		self.ui.all_clear.show()

	def show_clear(self):
		self.ui.all_clear.hide()
		self.ui.clear.show()

	def insertToInput(self,value,append=True):
		current_value = self.ui.result.text()
		
		value = str(value)
		if append:
			self.ui.result.setText(current_value + value)
		else:
			self.ui.result.setText(value)
		if self.last_operator == '=':
			self.last_operator = ''

	def remove_last(self):
		current_value = self.ui.result.text()
		if current_value == '0.' or current_value == '-0' or current_value == '-0.':
			current_value = ''
		else:	
			current_value = current_value[:-1]
		self.insertToInput(current_value,False)

	def insertDot(self):

		if self.ui.result.text() == '':
			self.insertToInput('0.')
		if '.' not in self.ui.result.text():
			self.insertToInput('.')

	def insertNumber(self,num):
		current_value = self.ui.result.text()
		
		if current_value == '-0':
			return
		if self.last_operator != '=':
			self.insertToInput(num)
		else:
			self.insertToInput(num,False)

	def removeNumber(self,char):
		current_value = self.ui.result.text()
		current_value.replace(char,'')
		self.insertToInput(current_value,False)

	def insertZero(self):
		try:
			if self.ui.result.text():
				if not self.ui.result.text().endswith('0'):
					self.insertToInput('0')
		except:
			pass


	def insertExpression(self,value):
		self.expression += value

	def insertOperator(self,operator):
		current_value = self.ui.result.text()
		self.insertExpression(current_value)
		if self.expression[-1].isdigit():
			self.expression += operator
			self.show_all_clear()
			self.clear()


	def clear(self):
		self.ui.result.setText('')


	def all_clear(self):
		self.expression = ' '
		self.clear()
		self.show_clear()


	def set_percentage(self):
		try:
			current_value = self.ui.result.text()
			value = float(current_value) / 100
			self.insertToInput(value,False)
		except:
			pass

	def negative_or_posetive(self):
		current_value = self.ui.result.text()
		if '-' in current_value:
			current_value = current_value[1:]
		else:
			current_value = '-' + current_value
		self.insertToInput(current_value,False)



	def equalExpression(self):
		current_value = self.ui.result.text()
		self.insertExpression(current_value)
		try:
			result = str(eval(self.expression))
			print('the result is:',result)
			self.insertToInput(result,False)
			self.expression = ' '
			self.last_operator = '='
			self.show_clear()
		except:
			pass

	def all_clear(self):
		self.expression = ' '
		self.clear()
		self.show_clear()


	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_0:
			self.insertZero()
		elif event.key() == QtCore.Qt.Key_1:
			self.insertNumber(1)
		elif event.key() == QtCore.Qt.Key_2:
			self.insertNumber(2)
		elif event.key() == QtCore.Qt.Key_3:
			self.insertNumber(3)
		elif event.key() == QtCore.Qt.Key_4:
			self.insertNumber(4)
		elif event.key() == QtCore.Qt.Key_5:
			self.insertNumber(5)
		elif event.key() == QtCore.Qt.Key_6:
			self.insertNumber(6)
		elif event.key() == QtCore.Qt.Key_7:
			self.insertNumber(7)
		elif event.key() == QtCore.Qt.Key_8:
			self.insertNumber(8)
		elif event.key() == QtCore.Qt.Key_9:
			self.insertNumber(9)
		elif event.key() == QtCore.Qt.Key_Backspace:
			self.remove_last()
		elif event.key() == QtCore.Qt.Key_Delete:
			self.clear()
		elif event.key() == QtCore.Qt.Key_Enter:
			self.equalExpression()
		elif event.key() == QtCore.Qt.Key_Percent:
			self.set_percentage()
		elif event.key() == QtCore.Qt.Key_Plus:
			self.insertOperator('+')
		elif event.key() == QtCore.Qt.Key_Period:
			self.insertDot()
		elif event.key() == QtCore.Qt.Key_Slash:
			self.insertOperator('/')
		elif event.key() == QtCore.Qt.Key_Asterisk:
			self.insertOperator('*')
		elif event.key() == QtCore.Qt.Key_Minus:
			self.insertOperator('-')
		elif event.key() == QtCore.Qt.Key_Alt:
			self.negative_or_posetive()




if __name__ == '__main__':
	app = QApplication(sys.argv)

	calculator = Calculator()
	calculator.show()

	app.exec_()