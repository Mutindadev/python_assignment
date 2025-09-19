# 📘 Python Assignments  

Welcome to my Python Assignments repository!  
This is where I document my journey of learning Python step by step through weekly projects and practice tasks. Each week builds on the last; from writing my first calculator to handling files and functions—all in one place.  

---

## 📑 Table of Contents
- [Week 1: Basic Calculator & List Operations](#week-1-basic-calculator--list-operations)
- [Week 2: More on Lists](#week-2-more-on-lists)
- [Week 3: Functions & Discounts](#week-3-functions--discounts)
- [Week 4: File Handling](#week-4-file-handling)
- [Week 5: Object-Oriented Programming (OOP)](#week-5-object-oriented-programming-oop)
- [Week 6: Ubuntu-Inspired Image Fetcher](#week-6-ubuntu-inspired-image-fetcher)
- [Week 7: Data Analysis with Pandas & Matplotlib](#week-7-data-analysis-with-pandas--matplotlib)
- [Week 8: Streamlit App Development](#week-8-streamlit-app-development)
- [Troubleshooting Guide](#troubleshooting-guide)

---

## 🚀 What’s Inside  

### 🧮 Week 1 – Basic Calculator  
I built a simple calculator that takes two numbers and an operator, then performs addition, subtraction, multiplication, or division.  
👉 My first hands-on practice with input, variables, and operators.  

---

### 📋 Week 2 – Working with Lists  
This week was all about Python lists. I learned how to:  
- Append and insert values  
- Extend a list with multiple elements  
- Remove items  
- Sort lists  
- Find indexes  

👉 End result: a well-structured list after different operations.  

---

### 💰 Week 3 – Functions & Discounts  
Here, I created a function that calculates the final price of an item after applying a discount.  
👉 A practical way to learn functions, parameters, and return values, while making the code reusable.  

---

### 📂 Week 4 – File Handling  
I explored reading and writing files in Python.  
I practiced with:  
- `open()` in read and write modes  
- `read()`, `readline()`, and `write()`  
- Handling errors like `FileNotFoundError` and `ValueError`  

👉 Now I can create, read, and update text files smoothly.  

---

---

## 📘 Week 5: Object-Oriented Programming (OOP)

### 🏗 Assignment 1: Design Your Own Class
- Created a *Smartphone class* with attributes and methods.  
- Used *constructors* to initialize each object.  
- Demonstrated *encapsulation* by making price private with getters and setters.  
- Added an *inheritance layer* through a GamingSmartphone class.  
- Showcased *polymorphism* by overriding methods.

---
---

### 🎭 Activity 2: Polymorphism Challenge
- Built a *Vehicle base class* with subclasses (Car, Plane, Boat).  
- Each subclass defined its own move() method.
  

- ## Week 6: Ubuntu-Inspired Image Fetcher
- A program inspired by the Ubuntu philosophy:  
  *"I am because we are."*  

### Features:
- Prompts user for an image URL.  
- Creates a folder called **Fetched_Images** if it doesn’t exist.  
- Downloads the image using the **requests** library.  
- Extracts a filename from the URL (or generates one).  
- Saves the image in binary mode.  
- Handles errors gracefully with user-friendly messages.  

## Troubleshooting Guide ⚡

While building **Week 6**, I encountered some issues. Here’s how to fix them:

### 1. `Import "requests" could not be resolved from source`

**Cause:**
VS Code was running with the wrong Python interpreter.

**Fix:**

* Open Command Palette → `Ctrl+Shift+P`
* Select **Python: Select Interpreter**
* Choose the interpreter where `requests` is installed (e.g., Python 3.11).
* Restart VS Code.

---

### 2. Installed `request` instead of `requests`

**Cause:**
The correct library is `requests` (plural). Installing `request` will not work.

**Fix:**
Run:

bash
pip uninstall request
pip install requests


---

### 3. Multiple Python Environments

Sometimes `pip` installs libraries in a different environment than the one VS Code is using.

**Fix:**
Check Python path:

bash
which python        # Mac/Linux
where python        # Windows


Check where `requests` is installed:

bash
pip show requests


Make sure both match. If not, install requests into the correct interpreter:

bash
python -m pip install requests

## Week 7: Data Analysis with Pandas & Matplotlib
- Introduction to **pandas** (DataFrames & Series).  
- Data manipulation: filtering, sorting, aggregating.  
- Summary statistics (`mean()`, `sum()`, `max()`).  
- Visualization with **matplotlib** (line plot, bar chart, histogram, scatter plot).  
- Challenge: Analyze `sales_data.csv` → save insights to `sales_summary.txt`.  
- Bonus: Plot sales trends.
1.Create a CSV file called sales_data.csv with columns:
Date (YYYY-MM-DD)
Product
Quantity Sold
Revenue (ksh)
2.Write a Python script week7_data_analysis.py to:
Load the CSV file using pandas.
Calculate the total revenue.
Find the best-selling product.
Identify the day with the highest sales.
Save results to a file: sales_summary.txt.
Print insights clearly in the terminal.

🛠️ Common Errors & Fixes

Error: Import "pandas" could not be resolved
✅ Fix: Make sure you installed the library using pip install pandas.

Error: Import "matplotlib" could not be resolved
✅ Fix: Run pip install matplotlib.

Wrong Python Interpreter: Sometimes VS Code highlights imports with a yellow line.
✅ Fix: Press Ctrl + Shift + P → Python: Select Interpreter → choose Python 3.11 (or your installed version).

---

## Week 8: Streamlit App Development
- Built an interactive web application using **Streamlit**.
- Displayed insights and visualizations from the COVID-19 research dataset (`metadata.csv`).
- Implemented widgets like sliders and dropdowns for dynamic data filtering.
- Explored publication trends, top journals, and frequent words in paper titles.
- Created a simple **COVID-19 research data explorer** to present findings clearly and interactively.

---

*Next Steps:**
- Test with larger `metadata.csv` if needed
- Add additional visualizations (e.g., source distribution, frequent words in abstracts)
- Finalize documentation and comments in the code
---

✅ This repository now covers:  
-Week 1 → Python Basics: variables, data types, operators, input/output

-Week 2 → Control Flow & Loops: if-else, for/while loops, break & continue

-Week 3 → Functions & Modules: defining functions, arguments, return values, importing modules

-Week 4 → Lists & Dictionaries: list operations, slicing, comprehension, dictionary operations

-Week 5 → Object-Oriented Programming: classes, objects, methods, inheritance

-Week 6 → File Handling & Web Requests: downloading files, creating directories, error handling, saving files

Week 7 → Data Analysis with Pandas & Matplotlib: dataframes, filtering, aggregating, summary statistics, visualizations, plotting trends

Week 8 → Streamlit App Development: interactive web app, displaying visualizations, widgets (sliders, dropdowns), exploring COVID-19 research

---

## ⚡ How to Run  
Clone this repo and navigate into the folder. Then run any assignment file with Python:  

```bash
git clone https://github.com/Mutindadev/python_assignment.git
cd python_assignment
python week1_assignment.py
```
Replace `week1_assignment.py` with the assignment file you want to run.

---
