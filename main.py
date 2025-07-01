from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "KATOCH MART", ln=True, align="C")
        self.set_font("Arial", "", 12)
        self.cell(0, 10, "Bill Receipt", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, "Thank you for shopping with us!", align="C")

def generate_grocery_bill_pdf(bill_data, filename="grocery_bill.pdf"):
    pdf = PDF()
    pdf.add_page()

    # Customer Info
    pdf.set_font("Arial", size=12)
    pdf.cell(100, 10, f"Customer Name: {bill_data['customer_name']}", ln=True)
    pdf.cell(100, 10, f"Bill Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(10)

    # Table Header
    pdf.set_font("Arial", "B", 12)
    pdf.cell(80, 10, "Item", border=1)
    pdf.cell(30, 10, "Quantity", border=1)
    pdf.cell(40, 10, "Unit Price (Rs.)", border=1)
    pdf.cell(40, 10, "Total (Rs.)", border=1)
    pdf.ln()

    # Table Data
    pdf.set_font("Arial", size=12)
    grand_total = 0
    for item in bill_data["items"]:
        name = item["item"]
        qty = item["quantity"]
        price = item["price"]
        total = qty * price
        grand_total += total

        pdf.cell(80, 10, name, border=1)
        pdf.cell(30, 10, str(qty), border=1)
        pdf.cell(40, 10, f"Rs. {price:.2f}", border=1)
        pdf.cell(40, 10, f"Rs. {total:.2f}", border=1)
        pdf.ln()

    # Total
    pdf.set_font("Arial", "B", 12)
    pdf.cell(150, 10, "Grand Total", border=1)
    pdf.cell(40, 10, f"Rs. {grand_total:.2f}", border=1)

    pdf.output(filename)
    print(f"\nPDF Bill saved as '{filename}'")

# -------------------------
# Get input from user
# -------------------------

def take_input_from_user():
    customer_name = input("Enter customer name: ")
    items = []
    print("\nEnter item details (type 'done' to finish):")
    
    while True:
        item_name = input("Item name: ")
        if item_name.lower() == 'done':
            break

        try:
            qty = int(input("Quantity: "))
            price = float(input("Unit Price (Rs.): "))
            items.append({"item": item_name, "quantity": qty, "price": price})
        except ValueError:
            print("Invalid input. Please enter numbers for quantity and price.")
    
    return {
        "customer_name": customer_name,
        "items": items
    }

# Main execution
if __name__ == "__main__":
    bill_data = take_input_from_user()
    if bill_data["items"]:
        generate_grocery_bill_pdf(bill_data)
    else:
        print("No items entered. Bill not generated.")
