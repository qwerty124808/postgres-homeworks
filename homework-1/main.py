"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

def r_file(file_name):
    data_list = []
    with open(f"C:\\Users\\79056\\Documents\\git\\17.1\\postgres-homeworks\\homework-1\\north_data\\{file_name}.csv", 
              encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter = ",")
        for row in file_reader:
            data_list.append(row)
    print(data_list)
    return data_list
    

# print("ТЕСТ_1")
# test_1 = r_file("customers_data")
# print("ТЕСТ_2")
# test_2 = r_file("employees_data")
# print("ТЕСТ_3")
# TEST_3 = r_file("orders_data")

# подключение к БД
conn = psycopg2.connect(host="localhost", database="test", user="postgres", password="12345")
# создаём объект cursor 
cur = conn.cursor()
cur.execute("SELECT * FROM customers")

rows = cur.fetchall()
for row in rows:
    print(row)

сur.close()
conn.close()
