# 🚀 Order Management System

A full-stack **CRUD (Create, Read, Update, Delete)** web application built using **Flask, MySQL, HTML, CSS, and JavaScript**.

This project allows users to efficiently manage orders with a modern, interactive, and professional UI dashboard.

---

## 📌 Features

- ✅ Create new orders
- 📋 View all orders in a dynamic table
- 🔄 Update order status (Pending, Shipped, Delivered, Confirmed, Cancelled)
- ❌ Delete orders
- 🎨 Modern UI with animations and hover effects
- 🟢 Color-coded status badges for better visualization

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** MySQL (PyMySQL)
- **Frontend:** HTML, CSS, JavaScript
- **API Testing:** Postman

---

## 📂 Project Structure
Order_api_project/
│
├── app.py
├── templates/
│ └── index.html
├── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

---

### 2. Install Dependencies

---

### 3. Setup MySQL Database

Run the following queries in MySQL:
CREATE DATABASE order_db;

USE order_db;

CREATE TABLE orders (
id INT AUTO_INCREMENT PRIMARY KEY,
item VARCHAR(100),
status VARCHAR(50)
);


---

### 4. Run the Application

Open your browser:
http://127.0.0.1:5000