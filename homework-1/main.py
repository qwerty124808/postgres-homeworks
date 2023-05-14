"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

# подключение к БД
conn = psycopg2.connect(host="localhost", database="north_data", user="postgres", password="1234")
# создаём объект cursor 
cur = conn.cursor()

def r_file(file_name):
    data_list = []
    with open(f"C:\\Users\\79056\\Documents\\git\\17.1\\postgres-homeworks\\homework-1\\north_data\\{file_name}.csv", 
              encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter = ",")
        for row in file_reader:
            data_list.append(row)
    return data_list

def customers_list(customers, conn, cur):
    for customer in customers[1:len(customers)]:
        cuctumer_id = customer[0]
        compani_name = customer[1]
        contact_name = customer[2]
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (cuctumer_id, compani_name, contact_name))
        conn.commit()
    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()
    
def emploees_list(emploees, conn, cur):
    for emploee in emploees[1:len(emploees)]:
        first_name = emploee[0]
        last_name = emploee[1]
        title = emploee[2]
        birth_date = emploee[3]
        notes = emploee[4]
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, title, birth_date, notes))
        conn.commit()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    

def orders_list(orders, conn, cur):
    for order in orders[1:len(orders)]:
        order_id = order[0]
        customer_id = order[1]
        employee_id = order[2]
        order_date = order[3]
        ship_city = order[4]
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (order_id, employee_id, customer_id, order_date, ship_city))
        conn.commit()
    cur.execute("SELECT * FROM orders")


customers = r_file("customers_data")
customers_list(customers, conn, cur)
emploees = r_file("employees_data")
emploees_list(emploees, conn, cur)
orders = r_file("orders_data")
orders_list(orders, conn, cur)
