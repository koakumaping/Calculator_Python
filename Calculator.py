#coding=utf-8
from __future__ import division
import sys

from PyQt4 import QtGui, QtCore

########################################################################
class Example(QtGui.QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(Example, self).__init__()

        self.initUI()


    #----------------------------------------------------------------------
    def initUI(self):
        """"""

        self.flag = 0
        self.flag_equ = 0
        self.flag_add = 0 #加
        self.flag_sub = 0 #减
        self.flag_mul = 0 #乘
        self.flag_div = 0 #除
        self.flag_flag = ''

        self.num_1 = '0'
        self.num_2 = ''
        self.num_3 = ''
        
        global lcd
        lcd = QtGui.QTextBrowser()
        lcd.setFixedHeight(190)
        lcd.setFont(QtGui.QFont("Microsoft YaHei", 20))
        
        #lcd.setFixedWidth(100)
        lcd.setText('0'.decode('utf-8'))
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        #self.setMinimumSize(300, 300)
        #self.setMaximumSize(300, 300)
        #self.setGeometry( 200, 100, 200, 200 )
        grid.setSpacing(0)
        grid.addWidget(lcd, 0, 0, 1, 4)

        button_1 = QtGui.QPushButton('1')
        button_2 = QtGui.QPushButton('2')
        button_3 = QtGui.QPushButton('3')
        button_4 = QtGui.QPushButton('4')
        button_5 = QtGui.QPushButton('5')
        button_6 = QtGui.QPushButton('6')
        button_7 = QtGui.QPushButton('7')
        button_8 = QtGui.QPushButton('8')
        button_9 = QtGui.QPushButton('9')
        button_0 = QtGui.QPushButton('0')
        button_dot = QtGui.QPushButton('.')
        button_equ = QtGui.QPushButton('=')
        button_div = QtGui.QPushButton('/')
        button_mul = QtGui.QPushButton('*')
        button_add = QtGui.QPushButton('+')
        button_sub = QtGui.QPushButton('-')
        button_cls = QtGui.QPushButton('cls')
        
        button_0.setFixedSize(50, 50)
        button_1.setFixedSize(50, 50)
        button_2.setFixedSize(50, 50)
        button_3.setFixedSize(50, 50)
        button_4.setFixedSize(50, 50)
        button_5.setFixedSize(50, 50)
        button_6.setFixedSize(50, 50)
        button_7.setFixedSize(50, 50)
        button_8.setFixedSize(50, 50)
        button_9.setFixedSize(50, 50)
        button_dot.setFixedSize(50, 50)
        button_equ.setFixedSize(200, 50)
        button_div.setFixedSize(50, 50)
        button_mul.setFixedSize(50, 50)
        button_add.setFixedSize(50, 50)
        button_sub.setFixedSize(50, 50)
        button_cls.setFixedSize(50, 50)
        
        button_0.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_1.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_2.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_3.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_4.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_5.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_6.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_7.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_8.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_9.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_dot.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_equ.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_div.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_mul.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_add.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_sub.setFont(QtGui.QFont("Microsoft YaHei", 16))
        button_cls.setFont(QtGui.QFont("Microsoft YaHei", 16))
        

        grid.addWidget(button_7, 1,0)
        grid.addWidget(button_8, 1,1)
        grid.addWidget(button_9, 1,2)
        grid.addWidget(button_div, 1,3)
        grid.addWidget(button_4, 2,0)
        grid.addWidget(button_5, 2,1)
        grid.addWidget(button_6, 2,2)
        grid.addWidget(button_mul, 2,3)
        grid.addWidget(button_1, 3,0)
        grid.addWidget(button_2, 3,1)
        grid.addWidget(button_3, 3,2)
        grid.addWidget(button_sub, 3,3)
        grid.addWidget(button_0, 4,0)
        grid.addWidget(button_dot, 4,1)
        grid.addWidget(button_cls, 4,2)
        grid.addWidget(button_add, 4,3)
        grid.addWidget(button_equ, 5, 0, 1, 4)

        self.move(300, 400)
        self.setWindowTitle('Calculator')
        grid.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.show()

        self.connect(button_0,QtCore.SIGNAL('clicked()'),self.func_button_0)
        self.connect(button_1,QtCore.SIGNAL('clicked()'),self.func_button_1)
        self.connect(button_2,QtCore.SIGNAL('clicked()'),self.func_button_2)
        self.connect(button_3,QtCore.SIGNAL('clicked()'),self.func_button_3)
        self.connect(button_4,QtCore.SIGNAL('clicked()'),self.func_button_4)
        self.connect(button_5,QtCore.SIGNAL('clicked()'),self.func_button_5)
        self.connect(button_6,QtCore.SIGNAL('clicked()'),self.func_button_6)
        self.connect(button_7,QtCore.SIGNAL('clicked()'),self.func_button_7)
        self.connect(button_8,QtCore.SIGNAL('clicked()'),self.func_button_8)
        self.connect(button_9,QtCore.SIGNAL('clicked()'),self.func_button_9)

        self.connect(button_cls,QtCore.SIGNAL('clicked()'),self.func_button_cls)
        self.connect(button_dot,QtCore.SIGNAL('clicked()'),self.func_button_dot)

        self.connect(button_add,QtCore.SIGNAL('clicked()'),self.func_button_add)
        self.connect(button_sub,QtCore.SIGNAL('clicked()'),self.func_button_sub)
        self.connect(button_mul,QtCore.SIGNAL('clicked()'),self.func_button_mul)
        self.connect(button_div,QtCore.SIGNAL('clicked()'),self.func_button_div)

        self.connect(button_equ,QtCore.SIGNAL('clicked()'),self.func_button_equ)


    #----------------------------------------------------------------------
    def keyPressEvent(self, event):
        """"""
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
            
        if event.key() == QtCore.Qt.Key_0:
            self.func_button_0()
            
        if event.key() == QtCore.Qt.Key_1:
            self.func_button_1()
        
        if event.key() == QtCore.Qt.Key_2:
            self.func_button_2()
                    
        if event.key() == QtCore.Qt.Key_3:
            self.func_button_3()

        if event.key() == QtCore.Qt.Key_4:
            self.func_button_4()

        if event.key() == QtCore.Qt.Key_5:
                    self.func_button_5()
        
        if event.key() == QtCore.Qt.Key_6:
            self.func_button_6()
                            
        if event.key() == QtCore.Qt.Key_7:
            self.func_button_7()

        if event.key() == QtCore.Qt.Key_8:
            self.func_button_8()

        if event.key() == QtCore.Qt.Key_9:
            self.func_button_9()

        if event.key() == QtCore.Qt.Key_Period:
            self.func_button_dot()        
    
        if event.key() == QtCore.Qt.Key_Enter:
            self.func_button_equ()

        if event.key() == QtCore.Qt.Key_Plus:
            self.func_button_add()
                    
        if event.key() == QtCore.Qt.Key_Minus:
            self.func_button_sub()
        
        if event.key() == QtCore.Qt.Key_Asterisk:
            self.func_button_mul()          
                    
        if event.key() == QtCore.Qt.Key_Slash:
            self.func_button_div()
            
        if event.key() == QtCore.Qt.Key_C:
            self.func_button_cls()

    #----------------------------------------------------------------------
    def func_button_0(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0': #防止在QLineEdit里连续出现 0 ，比如 000.1
                    self.num_1 = '0'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1+'0'
                    lcd.setText(self.num_1)
            else:
                if self.num_2 == '0' or '':
                    self.num_2 = '0'
                else:
                    self.num_2 = self.num_2+'0'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else :
            self.flag_equ =1 #Important:点击等号之后，除clear按键以外的按键都失效，用pass代替也可以，这里只是为了方便以后添加更多功能所以用了flag

    #----------------------------------------------------------------------
    def func_button_1(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '1'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '1'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or '':
                    self.num_2 = '1'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '1'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else :
            self.flag_equ =1

    #----------------------------------------------------------------------
    def func_button_2(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '2'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '2'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or '':
                    self.num_2 = '2'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '2'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else :
            self.flag_equ =1

    #----------------------------------------------------------------------
    def func_button_3(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '3'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '3'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or '':
                    self.num_2 = '3'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '3'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else :
            self.flag_equ =1

    #----------------------------------------------------------------------
    def func_button_4(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '4'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '4'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or '':
                    self.num_2 = '4'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '4'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else :
            self.flag_equ =1

    #----------------------------------------------------------------------
    def func_button_5(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '5'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '5'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or '':
                    self.num_2 = '3'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '5'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else :
            self.flag_equ =1

    #----------------------------------------------------------------------
    def func_button_6(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '6'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '6'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or '':
                    self.num_2 = '6'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '6'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else :
            self.flag_equ =1


    #----------------------------------------------------------------------
    def func_button_7(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '7'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '7'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or '':
                    self.num_2 = '7'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '7'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else :
            self.flag_equ =1

    #----------------------------------------------------------------------
    def func_button_8(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '8'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '8'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or '':
                    self.num_2 = '8'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '8'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else :
            self.flag_equ =1

    #----------------------------------------------------------------------
    def func_button_9(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:
                if self.num_1 == '0':
                    self.num_1 = '9'
                    lcd.setText(self.num_1)
                else:
                    self.num_1 = self.num_1 + '9'
                    lcd.setText(self.num_1)

            else:
                if self.num_2 == '0' or '':
                    self.num_2 = '9'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
                else:
                    self.num_2 = self.num_2 + '9'
                    lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else :
            self.flag_equ =1

    #----------------------------------------------------------------------
    def func_button_dot(self):
        """"""
        if self.flag_equ == 0:

            if self.flag == 0:

                if '.' not in self.num_1:

                    if self.num_1 == '0':
                        self.num_1 = '0.'
                        print self.num_1
                        lcd.setText(self.num_1)
                    else:
                        self.num_1 = self.num_1 + '.'
                        lcd.setText(self.num_1)

            else:
                if '.' not in self.num_2:

                    if self.num_2 == '':
                        self.num_2 = '0.'
                        lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
                    else:
                        self.num_2 = self.num_2 + '.'
                        lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else :
            self.flag_equ =1

    #----------------------------------------------------------------------
    def func_button_cls(self):
        """"""
        self.num_1 = '0'
        self.num_2 = ''
        self.flag = 0
        self.flag_equ = 0
        self.flag_add = 0
        self.flag_sub = 0
        self.flag_mul = 0
        self.flag_div = 0
        lcd.setText(self.num_1)

    #----------------------------------------------------------------------
    def func_button_add(self):
        """"""
        if self.flag == 0:
            self.flag = 1
            self.flag_add = 1
            self.flag_sub = 0
            self.flag_mul = 0
            self.flag_div = 0
            self.flag_flag = '+'
            lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else:
            pass

    #----------------------------------------------------------------------
    def func_button_sub(self):
        """"""
        if self.flag == 0:
            if self.num_1 == '0':
                self.num_1 = '-'
                lcd.setText(self.num_1)

            #elif self.num_2 == '':
                #self.num_2 = '-'
                #lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)

            else:
                self.flag = 1
                self.flag_add = 0
                self.flag_sub = 1
                self.flag_mul = 0
                self.flag_div = 0
                self.flag_flag = '-'

                lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else:
            if self.num_2 == '':
                self.num_2 = '-'
                lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)

    #----------------------------------------------------------------------
    def func_button_mul(self):
        """"""
        if self.flag == 0:

            self.flag = 1
            self.flag_add = 0
            self.flag_sub = 0
            self.flag_mul = 1
            self.flag_div = 0
            self.flag_flag = '*'

            lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else:
            pass

    #----------------------------------------------------------------------
    def func_button_div(self):
        """"""
        if self.flag == 0:
            self.flag = 1
            self.flag_add = 0
            self.flag_sub = 0
            self.flag_mul = 0
            self.flag_div = 1
            self.flag_flag = '/'

            lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2)
        else:
            pass

    #----------------------------------------------------------------------
    def func_button_equ(self):
        """"""
        if self.flag == 1:
            if self.flag_flag == '+':

                if '.' in self.num_1:
                    self.num_3 = str(float(self.num_1) + float(self.num_2))

                if '.' not in self.num_1:
                    if '.' not in self.num_2:
                        self.num_3 = str(int(self.num_1) + int(self.num_2))

                    elif '.' in self.num_2:
                        self.num_3 = str(float(self.num_1) + float(self.num_2))

                    else:
                        self.num_3 = str(int(self.num_1) + int(self.num_2))

                lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2 + '\n=\n' + self.num_3)
                self.flag = 0
                self.num_1 = '0'
                self.num_2 = ''
                self.num_3 = ''

            elif self.flag_flag == '-':

                if '.' in self.num_1:
                    self.num_3 = str(float(self.num_1) - float(self.num_2))

                if '.' not in self.num_1:
                    if '.' not in self.num_2:
                        self.num_3 = str(int(self.num_1) - int(self.num_2))

                    elif '.' in self.num_2:
                        self.num_3 = str(float(self.num_1) - float(self.num_2))

                    else:
                        self.num_3 = str(int(self.num_1) - int(self.num_2))

                lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2 + '\n=\n' + self.num_3)
                self.flag = 0
                self.num_1 = '0'
                self.num_2 = ''
                self.num_3 = ''            


            elif self.flag_flag == '*':

                if '.' in self.num_1:
                    self.num_3 = str(float(self.num_1) * float(self.num_2))

                if '.' not in self.num_1:
                    if '.' not in self.num_2:
                        self.num_3 = str(int(self.num_1) * int(self.num_2))

                    elif '.' in self.num_2:
                        self.num_3 = str(float(self.num_1) * float(self.num_2))

                    else:
                        self.num_3 = str(int(self.num_1) * int(self.num_2))

                lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2 + '\n=\n' + self.num_3)
                self.flag = 0
                self.num_1 = '0'
                self.num_2 = ''
                self.num_3 = ''

            elif self.flag_flag == '/':

                if self.num_2 == '0':
                    lcd.setText("0不能作为除数！".decode('utf-8'))
                    self.flag = 0
                    self.num_1 = '0'
                    self.num_2 = ''
                    self.num_3 = ''

                else:
                    self.num_3 = float(self.num_1) / float(self.num_2)

                    if (self.num_3 * 10) % 10 == 0:
                        lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2 + '\n=\n' + str(int(self.num_3)))

                        self.flag = 0
                        self.num_1 = '0'
                        self.num_2 = ''
                        self.num_3 = ''
                    else:
                        lcd.setText(self.num_1 + '\n' + self.flag_flag + '\n' + self.num_2 + '\n=\n' + str(float(self.num_3)))

                        self.flag = 0
                        self.num_1 = '0'
                        self.num_2 = ''
                        self.num_3 = ''                        

        else:
            pass


#----------------------------------------------------------------------
def main():
    """"""
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
