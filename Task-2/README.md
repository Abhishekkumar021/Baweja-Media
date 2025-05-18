# Task-2: MySQL SQL Queries Usage Guide

This guide explains how to use the SQL queries in `Task-2/SQL_QUERIES.SQL` with a MySQL database.

---

## 1. **Prerequisites**

- MySQL Server installed and running
- Access to a MySQL database with an `orders` table

---

## 2. **File Structure**

```
Task-2/
└── SQL_QUERIES.SQL
```

---

## 3. **Orders Table Structure (Example)**

Make sure your `orders` table has at least these columns:

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    amount DECIMAL(10,2),
    order_date DATE
);
```

---

## 4. **How to Run the Queries**

### **A. Open MySQL Command Line or Workbench**

- **Command Line:**  
  Open Command Prompt and enter:
  ```sh
  mysql -u your_username -p
  ```
  Enter your password when prompted.

- **Workbench:**  
  Open MySQL Workbench and connect to your database.

---

### **B. Select Your Database**

```sql
USE your_database_name;
```

---

### **C. Run the Queries**

#### **Option 1: Source the File**

If you are in the MySQL command line and your SQL file is at (locate your `SQL_QUERIES.SQL` file)`C:\Users\user_name\dir\dir\Task-2\SQL_QUERIES.SQL`:

```sql
SOURCE C:/Users/user_name/dir/dir/Task-2/SQL_QUERIES.SQL;
```
*(Use forward slashes `/` in the path)*

#### **Option 2: Copy-Paste Individual Queries**

Open `SQL_QUERIES.SQL`, copy the desired query, and paste it into your MySQL client.

---

## 5. **Query Reference**

**1. Total amount spent by each customer**
```sql
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id;
```

**2. Orders placed after '2023-01-03'**
```sql
SELECT * FROM orders
WHERE order_date > '2023-01-03';
```

**3. Customers who made more than one order**
```sql
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1;
```

---

## 6. **Notes**

- Adjust table or column names if your schema is different.
- Results will be shown in your MySQL client after execution.

---