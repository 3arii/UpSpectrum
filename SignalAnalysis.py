
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from openpyxl import *
import os

def txt_to_excel(text_file, excel_name):
    df = pd.read_table(text_file)
    df.to_excel(excel_name, 'Sheet1')

def get_column(file_name, column_title):
    wb = load_workbook(file_name)
    ws = wb.active

    column_a = ws[column_title]
    column_request = []

    for cell in column_a:
        column_request.append(cell.value)
    
    return column_request

def format_data(file_path, column_name):
    """
    Sums the first column of the data
    give the file path as a raw string in
    case of a unicode error.
    """
    column = get_column(file_path, column_name)
    column.pop(0)

    sum = 0

    for i in column:
        sum += float(i)

    return sum

txt_to_excel("servoBrokenSpectrum.txt", "broken_output.xlsx")
