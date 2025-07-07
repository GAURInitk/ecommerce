# 🛒 Django eCommerce App

A simple eCommerce web app built with **Django 4.2**, featuring product listings, cart functionality (for guests and logged-in users), and a basic checkout system.

---

## ⚙️ Features

- 🛍️ Product catalog with images and prices  
- 👤 Guest & user-based shopping carts  
- 🔄 Cart updates using JavaScript (AJAX)  
- 🧾 Checkout with shipping info  
- ⚙️ Admin panel for managing products and orders  

---

## 🔧 Getting Started

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/GAURInitk/ecommerce.git
cd ecommerce
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install Django==4.2.*
```

### 2. Apply Migrations & Create Superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 3. Run the Development Server
```bash
python manage.py runserver
```

- Visit the store: `http://127.0.0.1:8000/`  
- Admin panel: `http://127.0.0.1:8000/admin/`

---

## 🚀 To Improve

- 💳 Add payment gateway (e.g., Stripe, Razorpay)  
- 🎨 Improve UI with TailwindCSS or Bootstrap  
- ☁️ Deploy to cloud (Render, Heroku, etc.)  
- 🧪 Add tests and CI workflows  

---


