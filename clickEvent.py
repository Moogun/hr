import request
import openpyxl

def button_login_clicked(right_label):
    right_label.setText("Login clicked,see the console")
    request.login()

def button_mk_cap_clicked(right_label, right_label2):
    right_label.setText("Market Cap")
    right_label2.setText("2222")

def button_tr_vol_clicked(right_label):
    right_label.setText("Trading Vol")


def button_tr_val_clicked(right_label, right_label2):
    right_label.setText("Trading Value")
    #0 kospi, 1kosdaq / # 0 today, 1 yesterday
    # request.tr_val(0, 0)
