import random
import string
import sys
from datetime import datetime

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from gui import loginWindow
from gui import guestWindow
from gui import authorizationWindow
from gui import registrationWindow
from gui import userWindow
from gui import adminWindow
from gui import cartWindow
from gui import staffLoginWindow
from gui import tableReserveWindow
from gui import reservesTableWindow
from gui import waiterWindow
from gui import cookWindow
import connection

ADMIN_CODE = "ADMIN"
STAFF_CODE = "STAFF"


class CookWindow(QtWidgets.QWidget, cookWindow.Ui_cookWindow):
    authorization_window = None
    msgBox = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.refresh_orders_list()
        self.sendToKitchenButton.clicked.connect(self.send_to_paid)
        self.ordersList.doubleClicked.connect(self.show_order_info)
        self.OpenTheScheduleCook.clicked.connect(self.show_schedule_cook_info)

    def show_schedule_cook_info(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText(f"""Кухар №1 - 1-5 столики, 8.00-16.00
Кухар №2 - 6-10 столики, 8.00-16.00
Кухар №3 - 11-15 столики, 8.00-16.00
Кухар №4 - 1-5 столики, 16.00-00.00
Кухар №5 - 6-10 столики, 16.00-00.00
Кухар №6 - 11-15 столики, 16.00-00.00""")
        self.msgBox.setWindowTitle("Info")
        self.msgBox.show()

    def show_order_info(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        order = connection.get_order_by_username(self.ordersList.currentItem().text())
        amount_sum = 0
        count = 0
        dishes = ""
        for dish in order.get('dishes'):
            amount_sum += float(dish.get('price'))
            count += 1
            dishes += dish.get('name') + "\n"

        self.msgBox.setText(f"""Ціна - {amount_sum}ГРН
Кількість страв - {count}
Столик № {order.get('table')}
Список страв - {dishes}""")
        self.msgBox.setWindowTitle("Info")
        self.msgBox.show()

    def refresh_orders_list(self):
        self.ordersList.clear()
        orders = connection.get_orders()
        for i in orders:
            if i.get('status') == "cooking":
                user = connection.get_user_by_id(i.get('user_id'))
                self.ordersList.addItem(user.get('username'))

    def send_to_paid(self):
        if self.ordersList.currentItem() is None:
            return
        users = connection.get_users()
        for i in users:
            if i.get('username') == self.ordersList.currentItem().text():
                connection.set_order_status(i.get('_id'), "completed")
                break
        self.refresh_orders_list()

    def closeEvent(self, event):
        self.authorization_window = AuthorizationWindow()
        self.authorization_window.show()
        return super(CookWindow, self).closeEvent(event)


class WaiterWindow(QtWidgets.QWidget, waiterWindow.Ui_waiterWindow):
    authorization_window = None
    table_reserve_window = None
    cart_window = None
    msgBox = None
    current_user = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.dishDetailsTextEdit.setReadOnly(True)
        self.create_guest()
        self.refresh_dishes_list()
        pixmap = QPixmap('resources/cart.png')
        self.label_4.setPixmap(pixmap)
        self.dishesList.doubleClicked.connect(self.show_dish_details)
        self.addToCartButton.setDisabled(True)
        self.searchLineEdit.textChanged.connect(self.search_dish)
        self.addToCartButton.clicked.connect(self.add_to_cart)
        self.cartButton.clicked.connect(self.show_cart)
        self.refresh_orders_list()
        self.refresh_orders_list_2()
        self.sendToKitchenButton.clicked.connect(self.send_to_kitchen)
        self.paidButton.clicked.connect(self.order_paid)
        self.ordersList.doubleClicked.connect(self.show_order_info)
        self.ordersList_2.doubleClicked.connect(self.show_order_2_info)
        self.OpenTheScheduleButton.clicked.connect(self.show_schedule_info)

    def create_guest(self):
        self.current_user = {'username': f"Гiсть {len(connection.get_users())}"}
        connection.insert_user(self.current_user)

    def show_schedule_info(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText(f"""Офіціант №1 - 1-5 столики, 8.00-16.00
Офіціант №2 - 6-10 столики, 8.00-16.00
Офіціант №3 - 11-15 столики, 8.00-16.00
Офіціант №4 - 1-5 столики, 16.00-00.00
Офіціант №5 - 6-10 столики, 16.00-00.00
Офіціант №6 - 11-15 столики, 16.00-00.00""")
        self.msgBox.setWindowTitle("Info")
        self.msgBox.show()

    def show_order_info(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        order = connection.get_order_by_username(self.ordersList.currentItem().text())
        amount_sum = 0
        count = 0
        dishes = ""
        for dish in order.get('dishes'):
            amount_sum += float(dish.get('price'))
            count += 1
            dishes += dish.get('name') + "\n"

        self.msgBox.setText(f"""Ціна - {amount_sum}ГРН
Кількість страв - {count}
Столик № {order.get('table')}
Список страв - {dishes}""")
        self.msgBox.setWindowTitle("Info")
        self.msgBox.show()

    def show_order_2_info(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        order = connection.get_order_by_username(self.ordersList_2.currentItem().text())
        amount_sum = 0
        count = 0
        dishes = ""
        for dish in order.get('dishes'):
            amount_sum += float(dish.get('price'))
            count += 1
            dishes += dish.get('name') + "\n"

        self.msgBox.setText(f"""Ціна - {amount_sum}ГРН
Кількість страв - {count}
Столик № {order.get('table')}
Список страв - {dishes}""")
        self.msgBox.setWindowTitle("Info")
        self.msgBox.show()

    def show_cart(self):
        self.cart_window = CartWindow(self.current_user)
        self.cart_window.orderButton.clicked.connect(self.refresh_orders_list)
        self.cart_window.orderButton.clicked.connect(self.refresh_orders_list_2)
        self.cart_window.orderButton.clicked.connect(self.create_guest)
        self.cart_window.show()

    def add_to_cart(self):

        self.msgBox = QMessageBox()
        self.msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msgBox.setText("Подтверждение")
        result = self.msgBox.exec_()
        if QMessageBox.Yes == result:
            for dish in connection.get_dishes():
                if dish.get("name") == self.dishesList.currentItem().text():
                    for i in range(int(self.dishesCountSpinBox.text())):
                        connection.insert_dish_in_cart(self.current_user, dish)
                    if self.cart_window is not None:
                        self.cart_window.refresh_cart()
        else:
            pass

    def search_dish(self):
        self.dishesList.clear()
        if self.searchLineEdit.text() == "":
            self.refresh_dishes_list()
            return
        dishes = connection.get_dishes()
        for dish in dishes:
            if self.searchLineEdit.text().lower() in dish.get('name').lower():
                self.dishesList.addItem(dish.get('name'))

    def show_dish_details(self):
        for dish in connection.get_dishes():
            if dish.get('name') == self.dishesList.currentItem().text():
                self.dishDetailsTextEdit.setText(f"""
    Назва - {dish.get('name')}
    Ціна - {dish.get('price')} ГРН
    Опис - {dish.get('description')}
                        """)
                self.addToCartButton.setDisabled(False)
                return

    def refresh_dishes_list(self):
        dishes = connection.get_dishes()
        for dish in dishes:
            self.dishesList.addItem(dish.get("name"))

    def refresh_orders_list_2(self):
        self.ordersList_2.clear()
        orders = connection.get_orders()
        for i in orders:
            if i.get('status') == "completed":
                user = connection.get_user_by_id(i.get('user_id'))
                self.ordersList_2.addItem(user.get('username'))

    def refresh_orders_list(self):
        self.ordersList.clear()
        orders = connection.get_orders()
        for i in orders:
            if i.get('status') == "confirmed":
                user = connection.get_user_by_id(i.get('user_id'))
                self.ordersList.addItem(user.get('username'))

    def send_to_kitchen(self):
        if self.ordersList.currentItem() is None:
            return
        users = connection.get_users()
        for i in users:
            if i.get('username') == self.ordersList.currentItem().text():
                connection.set_order_status(i.get('_id'), "cooking")
        self.refresh_orders_list()

    def order_paid(self):
        if self.ordersList_2.currentItem() is None:
            return
        users = connection.get_users()
        for i in users:
            if i.get('username') == self.ordersList_2.currentItem().text():
                connection.paid_order(i.get('_id'))
        self.refresh_orders_list_2()

    def closeEvent(self, event):
        self.authorization_window = AuthorizationWindow()
        self.authorization_window.show()
        if self.cart_window is not None:
            self.cart_window.close()
        return super(WaiterWindow, self).closeEvent(event)


class ReservesTableWindow(QtWidgets.QWidget, reservesTableWindow.Ui_reservesTableWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.refresh_table()
        self.deleteReserveButton.clicked.connect(self.delete_reserve)

    def delete_reserve(self):
        if self.reservesTableWidget.item(self.reservesTableWidget.currentRow(), 0) is not None:
            name = self.reservesTableWidget.item(self.reservesTableWidget.currentRow(), 0).text()
            for user in connection.get_users():
                if user.get('name') == name:
                    connection.delete_reserve_by_user_id(user.get('_id'))
                    self.refresh_table()
                    break

    def refresh_table(self):
        self.reservesTableWidget.clear()
        self.reservesTableWidget.setColumnCount(4)
        self.reservesTableWidget.setHorizontalHeaderLabels(
            ["Имя и фамилия", "Столик", "Тип", "ДАТА"])

        self.reservesTableWidget.setRowCount(len(connection.get_reserves()))
        index = 0
        for i in connection.get_reserves():
            user = connection.get_user_by_id(i.get('user_id'))
            self.reservesTableWidget.setItem(index, 0, QTableWidgetItem(user.get('name')))
            self.reservesTableWidget.setItem(index, 1, QTableWidgetItem(i.get('table')))
            self.reservesTableWidget.setItem(index, 2, QTableWidgetItem(i.get('type')))
            self.reservesTableWidget.setItem(index, 3, QTableWidgetItem(i.get('date')))
            index += 1
        self.reservesTableWidget.resizeColumnsToContents()


class AdminWindow(QtWidgets.QWidget, adminWindow.Ui_adminWindow):
    authorization_window = None
    reserves_table_window = None
    flag = True

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.show_dish_add_form()
        self.showDishAddFormButton.clicked.connect(self.show_dish_add_form)
        self.addDishButton.clicked.connect(self.add_dish)
        self.dayProfitReportButton.clicked.connect(self.day_profit_report)
        self.monthProfitReportButton.clicked.connect(self.month_profit_report)
        self.weekProfitReportButton.clicked.connect(self.week_profit_report)
        self.newPasswordGenerateButton.clicked.connect(self.generate_new_password)
        self.showReservesTableButton.clicked.connect(self.show_reserves_table_window)

    def show_reserves_table_window(self):
        self.reserves_table_window = ReservesTableWindow()
        self.reserves_table_window.show()

    def generate_new_password(self):
        self.flag = True
        self.show_dish_add_form()
        choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in [i for i in list(string.ascii_uppercase)]:
            choice.append(i)
        code = ""
        for i in range(6):
            code += str(random.choice(choice))

        global STAFF_CODE
        STAFF_CODE = code

        self.detailsTextEdit.setText(f"""
INVITE CODE - {code}
""")

    def day_profit_report(self):
        self.flag = True
        self.show_dish_add_form()
        orders = connection.get_orders()
        amount = 0
        for order in orders:
            if order.get('date') is not None:
                if order.get('date').date() == datetime.today().date():
                    for dish in order.get('dishes'):
                        amount += float(dish.get('price'))
        self.detailsTextEdit.setText(f"""
Виручка за сьогодні - {amount}ГРН
""")

    def week_profit_report(self):
        self.flag = True
        self.show_dish_add_form()
        orders = connection.get_orders()
        amount = 0
        for order in orders:
            if order.get('date') is not None:
                if order.get('date').weekday() == datetime.today().weekday():
                    for dish in order.get('dishes'):
                        amount += float(dish.get('price'))
        self.detailsTextEdit.setText(f"""
Виручка за тиждень - {0}ГРН
""")

    def month_profit_report(self):
        self.flag = True
        self.show_dish_add_form()
        orders = connection.get_orders()
        amount = 0
        for order in orders:
            if order.get('date') is not None:
                if order.get('date').month == datetime.today().month:
                    for dish in order.get('dishes'):
                        amount += float(dish.get('price'))
        self.detailsTextEdit.setText(f"""
Виручка за місяць - {0}ГРН
""")

    def info(self, text):
        if text == "":
            self.infoLabel.setVisible(False)
        else:
            self.infoLabel.setVisible(True)
            self.infoLabel.setText(text)

    def add_dish(self):
        if len(self.dishNameLineEdit.text()) < 1 or len(self.dishPriceLineEdit.text()) < 1 or len(
                self.dishDescriptionPlainTextEdit.toPlainText()) < 1:
            self.info("Ви заповнили не всі поля")
            return

        for dish in connection.get_dishes():
            if dish.get('name') == self.dishNameLineEdit.text():
                self.dishNameLineEdit.clear()
                self.info("Блюдо з такою назвою\nвже існує")
                return

        connection.insert_dish({"name": self.dishNameLineEdit.text(), "price": int(self.dishPriceLineEdit.text()),
                                "description": self.dishDescriptionPlainTextEdit.toPlainText()})
        self.info("")

    def show_dish_add_form(self):
        self.flag = not self.flag
        self.detailsTextEdit.setVisible(not self.flag)
        self.dishNameLineEdit.setVisible(self.flag)
        self.dishPriceLineEdit.setVisible(self.flag)
        self.dishDescriptionPlainTextEdit.setVisible(self.flag)
        self.addDishButton.setVisible(self.flag)

    def closeEvent(self, event):
        self.authorization_window = AuthorizationWindow()
        self.authorization_window.show()
        return super(AdminWindow, self).closeEvent(event)


class TableReserveWindow(QtWidgets.QWidget, tableReserveWindow.Ui_tableReserveForm):
    reserves_table_window = None

    def __init__(self, user):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.current_user = user
        self.reserveButton.clicked.connect(self.reserve)
        self.comboBox.currentTextChanged.connect(self.change)
        self.comboBox.addItem("Банкет")
        self.comboBox.addItem("Столик")
        self.change()
        self.check_reserve()
        for i in range(1, 16):
            self.tableChoiceComboBox.addItem(str(i))
        self.showReservesTableButton.clicked.connect(self.show_reserves_table_window)

    def show_reserves_table_window(self):
        self.reserves_table_window = ReservesTableWindow()
        self.reserves_table_window.show()
        self.reserves_table_window.deleteReserveButton.hide()

    def check_reserve(self):
        reserves = connection.get_reserves()
        for i in reserves:
            if i.get("user_id") == self.current_user.get('_id'):
                self.infoLabel.setText(f"Ви вже забронювали {i.get('type')}\nна {i.get('date')}")
                self.timeEdit.setDisabled(True)
                self.dateEdit.setDisabled(True)
                self.reserveButton.setDisabled(True)
                self.comboBox.setDisabled(True)
                self.tableChoiceComboBox.setDisabled(True)

    def change(self):
        if self.comboBox.currentText() == "Банкет":
            self.timeEdit.hide()
            self.dateEdit.show()
            self.tableLabel.hide()
            self.tableChoiceComboBox.hide()
        else:
            self.timeEdit.show()
            self.tableLabel.show()
            self.tableChoiceComboBox.show()
            self.dateEdit.hide()

    def reserve(self):
        reserves = connection.get_reserves()
        reserve = {'type': self.comboBox.currentText(), 'user_id': self.current_user.get('_id')}
        if self.comboBox.currentText() == "Банкет":
            for i in reserves:
                if i.get("date") == self.dateEdit.date().toString():
                    self.infoLabel.setText("Ця дата заброньована")
                    return
            self.infoLabel.setText("")
            reserve.update({'date': self.dateEdit.date().toString()})
        else:
            for i in reserves:
                if i.get("date") == str(datetime.now().today().date()) + self.timeEdit.time().toString():
                    self.infoLabel.setText("Ця время заброньована")
                    return
            self.infoLabel.setText("")
            reserve.update({'date': str(datetime.now().today().date()) + self.timeEdit.time().toString(),
                            'table': self.tableChoiceComboBox.currentText()})
        connection.insert_reserve(reserve)
        self.close()


class GuestWindow(QtWidgets.QWidget, guestWindow.Ui_guestWindow):
    authorization_window = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.dishDetailsTextEdit.setReadOnly(True)
        self.refresh_dishes_list()
        self.dishesList.doubleClicked.connect(self.show_dish_details)
        self.searchLineEdit.textChanged.connect(self.search_dish)

    def search_dish(self):
        self.dishesList.clear()
        if self.searchLineEdit.text() == "":
            self.refresh_dishes_list()
            return
        dishes = connection.get_dishes()
        for dish in dishes:
            if self.searchLineEdit.text().lower() in dish.get("name").lower():
                self.dishesList.addItem(dish.get("name"))

    def show_dish_details(self):
        for dish in connection.get_dishes():
            if dish.get("name") == self.dishesList.currentItem().text():
                self.dishDetailsTextEdit.setText(f"""
Назва - {dish.get("name")}
Ціна - {dish.get("price")} ГРН
Опис - {dish.get("description")}
                """)
                return

    def refresh_dishes_list(self):
        dishes = connection.get_dishes()
        for dish in dishes:
            self.dishesList.addItem(dish.get("name"))

    def closeEvent(self, event):
        self.authorization_window = AuthorizationWindow()
        self.authorization_window.show()
        return super(GuestWindow, self).closeEvent(event)


class CartWindow(QtWidgets.QMainWindow, cartWindow.Ui_cartWindow):
    msgBox = None

    def __init__(self, user):
        self.current_user = user
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.amountLabel.setText("")
        self.refresh_cart()
        self.orderButton.clicked.connect(self.confirm_order)
        for i in range(1, 16):
            self.tableChoiceComboBox.addItem(str(i))

    def confirm_order(self):
        self.msgBox = QMessageBox()
        self.msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msgBox.setText("Подтверждение")
        result = self.msgBox.exec_()
        if QMessageBox.Yes == result:
            connection.confirm_order(self.current_user.get('_id'), self.tableChoiceComboBox.currentText())
            self.close()
        else:
            pass

    def delete_dish(self, name):
        connection.delete_dish_from_cart(self.current_user, name)
        self.refresh_cart()

    def refresh_cart(self):
        amount = 0

        for i in reversed(range(self.l.count())):
            self.l.itemAt(i).widget().setParent(None)

        for i in reversed(range(self.l_2.count())):
            self.l_2.itemAt(i).widget().setParent(None)
        if connection.get_order_by_user(self.current_user) is not None:
            for i in connection.get_order_by_user(self.current_user).get('dishes'):
                amount += i.get('price')
                label = QtWidgets.QLabel()
                label.setText(i.get('name'))
                delete_button = QtWidgets.QPushButton()
                delete_button.setText("Видалити блюдо")
                delete_button.clicked.connect((lambda ch, name=i.get('name'): self.delete_dish(name)))
                self.l.addWidget(label)
                self.l_2.addWidget(delete_button)
            self.amountLabel.setText(f"{amount} ГРН")


class UserWindow(QtWidgets.QWidget, userWindow.Ui_userWindow):
    authorization_window = None
    cart_window = None
    table_reserve_window = None
    msgBox = None

    def __init__(self, user):
        self.current_user = user
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.dishDetailsTextEdit.setReadOnly(True)
        self.refresh_dishes_list()
        pixmap = QPixmap('resources/cart.png')
        self.label_4.setPixmap(pixmap)
        self.dishesList.doubleClicked.connect(self.show_dish_details)
        self.addToCartButton.setDisabled(True)
        self.searchLineEdit.textChanged.connect(self.search_dish)
        self.addToCartButton.clicked.connect(self.add_to_cart)
        self.cartButton.clicked.connect(self.show_cart)
        self.reserveButton.clicked.connect(self.show_table_reserve_window)

    def show_table_reserve_window(self):
        self.table_reserve_window = TableReserveWindow(self.current_user)
        self.table_reserve_window.show()

    def show_cart(self):
        self.cart_window = CartWindow(self.current_user)
        self.cart_window.show()

    def add_to_cart(self):

        self.msgBox = QMessageBox()
        self.msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msgBox.setText("Подтверждение")
        result = self.msgBox.exec_()
        if QMessageBox.Yes == result:
            for dish in connection.get_dishes():
                if dish.get("name") == self.dishesList.currentItem().text():
                    for i in range(int(self.dishesCountSpinBox.text())):
                        connection.insert_dish_in_cart(self.current_user, dish)
                    if self.cart_window is not None:
                        self.cart_window.refresh_cart()
        else:
            pass

    def search_dish(self):
        self.dishesList.clear()
        if self.searchLineEdit.text() == "":
            self.refresh_dishes_list()
            return
        dishes = connection.get_dishes()
        for dish in dishes:
            if self.searchLineEdit.text().lower() in dish.get('name').lower():
                self.dishesList.addItem(dish.get('name'))

    def show_dish_details(self):
        for dish in connection.get_dishes():
            if dish.get('name') == self.dishesList.currentItem().text():
                self.dishDetailsTextEdit.setText(f"""
Назва - {dish.get('name')}
Ціна - {dish.get('price')} ГРН
Опис - {dish.get('description')}
                    """)
                self.addToCartButton.setDisabled(False)
                return

    def refresh_dishes_list(self):
        dishes = connection.get_dishes()
        for dish in dishes:
            self.dishesList.addItem(dish.get("name"))

    def closeEvent(self, event):
        self.authorization_window = AuthorizationWindow()
        self.authorization_window.show()
        if self.cart_window is not None:
            self.cart_window.close()
        return super(UserWindow, self).closeEvent(event)


class AuthorizationWindow(QtWidgets.QMainWindow, authorizationWindow.Ui_authorizationWindow):
    guest_window = None
    login_window = None
    staff_login_window = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.guestButton.clicked.connect(self.show_guest_window)
        self.userButton.clicked.connect(self.show_login_window)
        self.adminButton.clicked.connect(self.show_admin_login_window)
        self.waiterButton.clicked.connect(self.show_waiter_login_window)
        self.cookButton.clicked.connect(self.show_cook_login_window)

    def show_admin_login_window(self):
        self.staff_login_window = StaffLoginWindow("ADMIN")
        self.staff_login_window.show()
        self.close()

    def show_cook_login_window(self):
        self.staff_login_window = StaffLoginWindow("COOK")
        self.staff_login_window.show()
        self.close()

    def show_waiter_login_window(self):
        self.staff_login_window = StaffLoginWindow("WAITER")
        self.staff_login_window.show()
        self.close()

    def show_guest_window(self):
        self.guest_window = GuestWindow()
        self.guest_window.show()
        self.close()

    def show_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


class StaffLoginWindow(QtWidgets.QWidget, staffLoginWindow.Ui_staffLoginForm):
    authorization_window = None
    admin_window = None
    waiter_window = None
    cook_window = None

    def __init__(self, type):
        super().__init__()
        self.setupUi(self)
        self.type = type
        self.setFixedSize(self.size())
        self.loginButton.clicked.connect(self.login)

    def login(self):
        if self.type == "ADMIN":
            if self.keyLineEdit.text() == ADMIN_CODE:
                self.show_admin_window()
        if self.type == "WAITER":
            if self.keyLineEdit.text() == STAFF_CODE:
                self.show_waiter_window()
        if self.type == "COOK":
            if self.keyLineEdit.text() == STAFF_CODE:
                self.show_cook_window()

    def show_cook_window(self):
        self.cook_window = CookWindow()
        self.cook_window.show()
        self.hide()

    def show_waiter_window(self):
        self.waiter_window = WaiterWindow()
        self.waiter_window.show()
        self.hide()

    def show_admin_window(self):
        self.admin_window = AdminWindow()
        self.admin_window.show()
        self.hide()

    def closeEvent(self, event):
        self.authorization_window = AuthorizationWindow()
        self.authorization_window.show()
        return super(StaffLoginWindow, self).closeEvent(event)


class LoginWindow(QtWidgets.QWidget, loginWindow.Ui_loginForm):
    registration_window = None
    user_window = None
    authorization_window = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.registrationButton.clicked.connect(self.registration)
        self.loginButton.clicked.connect(self.login)

    def login(self):
        for user in connection.get_users():
            if user.get('username') == self.usernameLineEdit.text() and user.get(
                    'password') == self.passwordLineEdit.text():
                self.user_window = UserWindow(user)
                self.user_window.show()
                self.hide()

    def registration(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()
        self.hide()

    def closeEvent(self, event):
        self.authorization_window = AuthorizationWindow()
        self.authorization_window.show()
        return super(LoginWindow, self).closeEvent(event)


class RegistrationWindow(QtWidgets.QWidget, registrationWindow.Ui_registrationForm):
    loginWindow = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.registrationButton.clicked.connect(self.registration)
        self.usernameLineEdit.textChanged.connect(self.check_password_and_password_valid)
        self.passwordLineEdit.textChanged.connect(self.check_password_and_password_valid)
        self.nameLineEdit.textChanged.connect(self.check_name_and_surname_valid)
        self.surnameLineEdit.textChanged.connect(self.check_name_and_surname_valid)

    def check_name_and_surname_valid(self):
        valid = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджiIэячсмитьбю"
        for i in self.nameLineEdit.text():
            if i not in valid:
                self.nameLineEdit.setText(self.nameLineEdit.text().replace(i, ""))
        for i in self.surnameLineEdit.text():
            if i not in valid:
                self.surnameLineEdit.setText(self.surnameLineEdit.text().replace(i, ""))

    def check_password_and_password_valid(self):
        valid = string.ascii_letters + "123456789"
        for i in self.usernameLineEdit.text():
            if i not in valid:
                self.usernameLineEdit.setText(self.usernameLineEdit.text().replace(i, ""))
        for i in self.passwordLineEdit.text():
            if i not in valid:
                self.passwordLineEdit.setText(self.passwordLineEdit.text().replace(i, ""))

    def registration(self):
        if len(self.usernameLineEdit.text()) < 1 or len(self.passwordLineEdit.text()) < 1 or len(
                self.nameLineEdit.text()) < 1 or len(self.surnameLineEdit.text()) < 1:
            self.info("Ви заповнили не всі поля")
            return

        for user in connection.get_users():
            if user.get('username') == self.usernameLineEdit.text():
                self.usernameLineEdit.clear()
                self.info("Користувачів з таким логіном вже існує")
                return

        user = {'username': self.usernameLineEdit.text(), 'password': self.passwordLineEdit.text(),
                'name': self.nameLineEdit.text() + " " + self.surnameLineEdit.text()}
        connection.insert_user(user)
        self.close()

    def closeEvent(self, event):
        self.loginWindow = LoginWindow()
        self.loginWindow.show()
        return super(RegistrationWindow, self).closeEvent(event)

    def info(self, text):
        if text == "":
            self.infoLabel.setVisible(False)
        else:
            self.infoLabel.setVisible(True)
            self.infoLabel.setText(text)


def my_except_hook(in_type, value, type_back):
    """
    Ловит исключения возникающие в оболочке
    """

    QtWidgets.QMessageBox.critical(
        window, "CRITICAL ERROR", str(value),
        QtWidgets.QMessageBox.Cancel
    )

    sys.__excepthook__(in_type, value, type_back)


if __name__ == '__main__':
    sys.excepthook = my_except_hook
    app = QtWidgets.QApplication(sys.argv)
    window = AuthorizationWindow()
    window.show()
    sys.exit(app.exec_())
