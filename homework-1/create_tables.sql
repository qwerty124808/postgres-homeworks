-- SQL-команды для создания таблиц

CREATE TABLE employees (
	first_name VARCHAR(255),        --имя
	last_name VARCHAR(255),         --фамилия
	title VARCHAR(255) NOT NULL,    --должность
	birth_date DATE                 --дата рождения
	notes TEXT,
    employer_id INT                   
	PRIMARY KEY (employer_id)
);

CREATE TABLE customers (
	customer_id VARCHAR(255),       --id_клиента
	company_name VARCHAR(255),      --название компании
	contact_name VARCHAR(255),      --имя для связи
	PRIMARY KEY (customer_id)
);

CREATE TABLE orders (
	order_id INT PRIMARY KEY,                                           --id_заказа                                         
	employee_id int REFERENCES employees(employer_id) NOT NULL,         --id_работника
	order_date DATE,                                                    --дата заказа
	ship_city VARCHAR(255)
    customer_id VARCHAR(255) REFERENCES customers(customer_id) NOT NULL --id_клиента
    
);	