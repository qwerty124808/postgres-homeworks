-- SQL-команды для создания таблиц

CREATE TABLE employees (
	first_name VARCHAR(255),      
	last_name VARCHAR(255),        
	title VARCHAR(255) NOT NULL,    
	birth_date DATE,                 
	notes TEXT,
	employer_id SERIAL PRIMARY KEY
);

CREATE TABLE customers (
	customer_id VARCHAR(255) PRIMARY KEY,     
	company_name VARCHAR(255),      
	contact_name VARCHAR(255) 
);

CREATE TABLE orders (
	order_id INT PRIMARY KEY,                                                                               
    customer_id VARCHAR(255) REFERENCES customers(customer_id) NOT NULL,   
	employee_id int REFERENCES employees(employer_id) NOT NULL,          
	order_date DATE,                                                    
	ship_city VARCHAR(255)
);	