from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
from mainform import *

class MainForm(QtWidgets.QWidget):

    def __init__(self):
        super(MainForm, self).__init__()
        self.setWindowTitle("智能证件照生成系统")
        self.setWindowIcon(QtGui.QIcon('tubiao.png'))
        self.setFixedSize(1000, 630)
        self.setStyleSheet("background-color: white; color: black;")

        self.init_db()  # Initialize the database
        self.init_ui()

    def init_db(self):
        # Connect to SQLite database and create table if not exists
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def init_ui(self):
        layout = QtWidgets.QHBoxLayout(self)
        self.sidebar = self.create_sidebar()
        layout.addWidget(self.sidebar, 1)

        self.stacked_widget = QtWidgets.QStackedWidget(self)
        layout.addWidget(self.stacked_widget, 4)
        self.login_page = self.create_login_page()
        self.register_page = self.create_register_page()

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.register_page)

        self.animation = QtCore.QPropertyAnimation(self.stacked_widget, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)

    def create_sidebar(self):
        sidebar = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(sidebar)

        login_button = QtWidgets.QPushButton("登录")
        login_button.setFixedSize(100, 40)
        login_button.setStyleSheet("background-color: blue; color: white; font-size: 18px;")
        login_button.clicked.connect(lambda: self.display(0))

        register_button = QtWidgets.QPushButton("注册")
        register_button.setFixedSize(100, 40)
        register_button.setStyleSheet("background-color: blue; color: white; font-size: 18px;")
        register_button.clicked.connect(lambda: self.display(1))

        layout.addStretch(2)
        layout.addWidget(login_button, alignment=QtCore.Qt.AlignHCenter)
        layout.addStretch(2)
        layout.addWidget(register_button, alignment=QtCore.Qt.AlignHCenter)
        layout.addStretch(4)

        return sidebar

    def display(self, index):
        self.animation.setStartValue(self.stacked_widget.geometry())
        self.stacked_widget.setCurrentIndex(index)
        self.animation.setEndValue(self.stacked_widget.geometry())
        self.animation.start()

    def create_login_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)

        top_bg = QtWidgets.QLabel(page)
        top_bg.setPixmap(QtGui.QPixmap('logup.png').scaled(1000, 150))  # Adjusted size
        top_bg.setAlignment(QtCore.Qt.AlignCenter)

        form_widget = QtWidgets.QWidget(page)
        form_layout = QtWidgets.QFormLayout(form_widget)
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setSpacing(20)

        username_label = QtWidgets.QLabel("用户名", page)
        username_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.username_input = QtWidgets.QLineEdit(page)
        self.username_input.setPlaceholderText("请输入账号")
        self.username_input.setFixedWidth(600)
        self.username_input.setFixedHeight(50)
        self.username_input.setStyleSheet("background-color: lightgray; color: black; font-size: 20px;")

        password_label = QtWidgets.QLabel("密码", page)
        password_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.password_input = QtWidgets.QLineEdit(page)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setPlaceholderText("请输入密码")
        self.password_input.setFixedWidth(600)
        self.password_input.setFixedHeight(50)
        self.password_input.setStyleSheet("background-color: lightgray; color: black; font-size: 20px;")

        login_button = QtWidgets.QPushButton("登录", page)
        login_button.setFixedWidth(300)
        login_button.setFixedHeight(50)
        login_button.setStyleSheet("background-color: gray; color: white; font-size: 20px;")
        login_button.clicked.connect(self.login)

        form_layout.addRow(username_label, self.username_input)
        form_layout.addRow(password_label, self.password_input)
        form_layout.addRow(QtWidgets.QLabel(), login_button)

        bottom_bg = QtWidgets.QLabel(page)
        bottom_bg.setPixmap(QtGui.QPixmap('logdown.png').scaled(1000, 300))  # Adjusted size
        bottom_bg.setAlignment(QtCore.Qt.AlignCenter)

        layout.addWidget(top_bg)
        layout.addWidget(form_widget, 1)
        layout.addWidget(bottom_bg)

        return page

    def create_register_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)

        top_bg = QtWidgets.QLabel(page)
        top_bg.setPixmap(QtGui.QPixmap('regup.png').scaled(1000, 130))  # Adjusted size
        top_bg.setAlignment(QtCore.Qt.AlignCenter)

        form_widget = QtWidgets.QWidget(page)
        form_layout = QtWidgets.QFormLayout(form_widget)
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setSpacing(20)

        register_label = QtWidgets.QLabel("注册账号", page)
        register_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.register_input = QtWidgets.QLineEdit(page)
        self.register_input.setPlaceholderText("请输入账号")
        self.register_input.setFixedWidth(600)
        self.register_input.setFixedHeight(40)
        self.register_input.setStyleSheet("background-color: lightgray; color: black; font-size: 20px;")

        password_label = QtWidgets.QLabel("密码", page)
        password_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.register_password_input = QtWidgets.QLineEdit(page)
        self.register_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_password_input.setPlaceholderText("请输入密码")
        self.register_password_input.setFixedWidth(600)
        self.register_password_input.setFixedHeight(40)
        self.register_password_input.setStyleSheet("background-color: lightgray; color: black; font-size: 20px;")

        confirm_password_label = QtWidgets.QLabel("确认密码", page)
        confirm_password_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.confirm_password_input = QtWidgets.QLineEdit(page)
        self.confirm_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_input.setPlaceholderText("请确认密码")
        self.confirm_password_input.setFixedWidth(600)
        self.confirm_password_input.setFixedHeight(40)
        self.confirm_password_input.setStyleSheet("background-color: lightgray; color: black; font-size: 20px;")

        register_button = QtWidgets.QPushButton("注册", page)
        register_button.setFixedWidth(300)
        register_button.setFixedHeight(40)
        register_button.setStyleSheet("background-color: gray; color: white; font-size: 20px;")
        register_button.clicked.connect(self.register)

        form_layout.addRow(register_label, self.register_input)
        form_layout.addRow(password_label, self.register_password_input)
        form_layout.addRow(confirm_password_label, self.confirm_password_input)
        form_layout.addRow(QtWidgets.QLabel(), register_button)

        bottom_bg = QtWidgets.QLabel(page)
        bottom_bg.setPixmap(QtGui.QPixmap('regdown.png').scaled(1000, 190))  # Adjusted size
        bottom_bg.setAlignment(QtCore.Qt.AlignCenter)

        layout.addWidget(top_bg)
        layout.addWidget(form_widget, 1)
        layout.addWidget(bottom_bg)

        return page

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QtWidgets.QMessageBox.warning(self, "警告", "请输入账号和密码")
            return

        self.cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        result = self.cursor.fetchone()

        if result and result[0] == password:
            QtWidgets.QMessageBox.information(self, "成功", "登录成功！", QtWidgets.QMessageBox.Ok)
            self.username_input.clear()
            self.password_input.clear()
            user_ui.show()
            mainForm.close()
            # Proceed to the main form or main application functionality here
            # For example, you could hide the login/register widget and show the main application widget
        else:
            reply = QtWidgets.QMessageBox.question(self, '注册', '账号或密码错误，是否前往注册账号', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.sidebar.findChildren(QtWidgets.QPushButton)[1].click()

    def register(self):
        username = self.register_input.text()
        password = self.register_password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not username or not password or not confirm_password:
            QtWidgets.QMessageBox.warning(self, "警告", "请输入账号和密码")
            return

        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self, "警告", "密码不匹配，请重试！")
            return

        try:
            self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            self.conn.commit()
            QtWidgets.QMessageBox.information(self, "成功", "注册成功！", QtWidgets.QMessageBox.Ok)
            self.register_input.clear()
            self.register_password_input.clear()
            self.confirm_password_input.clear()
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "警告", "用户名已存在，请选择其他用户名！")

    def closeEvent(self, event):
        self.conn.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainForm = MainForm()
    user_ui=user_mainWindow()
    mainForm.show()
    sys.exit(app.exec_())
