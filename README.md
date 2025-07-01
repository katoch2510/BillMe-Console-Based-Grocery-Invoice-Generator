# BillMe-Console-Based-Grocery-Invoice-Generator
This is my major project of python on my training session of project bases python programming. It is an enhanced form of my minor project 2  bill generator . It basically solves an real life problem of having record of the sales in soft copy format  but not  hard copy format . so it provide a Pdf of the given sales.
# 🧾 BillMe: Console-Based Grocery Invoice Generator

**BillMe** is a Python console application that generates professional PDF bills for a grocery store. It allows you to enter customer details and purchased items, and creates a well-structured invoice using the `fpdf` library.

---

## 🚀 Features

- Input customer name and items via terminal
- Calculates item-wise totals and grand total
- Generates a clean and printable PDF invoice
- Uses "Rs." instead of "₹" to avoid encoding issues
- Lightweight, simple, and effective

---

## 🗂️ Project Structure

billme/
├── main.py         # Main application script  
├── README.md       # This file  
├── grocery_bill.pdf # Output PDF (generated after running)

---

## 🛠️ Requirements

- Python 3.x
- fpdf library

Install it using pip:
## 🧑‍💻 How to Use

1. Run the script:
2. Provide inputs like:
3. PDF will be saved as:


---

## 🖨️ Sample Output (PDF Content)

SuperMart Grocery Store  
Bill Receipt  

Customer Name: Ravi Sharma  
Bill Date: 2025-07-01 14:20:10  

Item           Quantity    Unit Price    Total  
Rice           2           Rs. 50.00     Rs. 100.00  
Sugar          1           Rs. 45.00     Rs. 45.00  
Grand Total:                             Rs. 145.00  

Thank you for shopping with us!

---

## 💡 Future Enhancements

- Add GST and discount fields
- GUI version using Tkinter
- Save/load product catalog from file/database
- Export as CSV/Excel
- Print directly from script

---

## 👨‍💻 Author

**Piyush Katoch**  
Made with ❤️ in Python

---

## 📄 License

This project is open-source and free to use for educational or commercial purposes.
