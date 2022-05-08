from db_config import DBConfig
import openpyxl

number_file = openpyxl.load_workbook('당첨번호.xlsx')

number_sheet = number_file['당첨번호']

whole_data = number_sheet['B4':'T1016']

# 회차 추첨일 1등 당첨자 수 / 당첨금액 ~ 5등 당첨번호 & 보너스

for row in whole_data:
    times = row[0].value
    date = row[1].value
    match_numbers = [n.value for n in row[-7:]]
    print(times,date,match_numbers)


