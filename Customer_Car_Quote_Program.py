import Customer_Car_Quote as c

def main():
    name = input("Name: ")
    address = input("Address: ")
    phone = input("Phone: ")
    customer = c.Customer(name, address, phone)
    print()

    make = input("Make: ")
    model = input("Model: ")
    year = input("Year: ")
    car = c.Car(make, model, year)
    print()

    pcharge = float(input("Parts Charges: "))
    lcharge = float(input("Labor Charges: "))
    charges = c.ServiceQuote(pcharge, lcharge)
    print()

    customer = c.Customer(name, address, phone)
    car = c.Car(make, model, year)
    quote = c.ServiceQuote(pcharge, lcharge)

    print("Customer Name:", customer.get_name())
    print("Customer Phone No.:", customer.get_phone())
    print("Make/Model/Year:", car.get_make(), " ", car.get_model(), " ", car.get_year())
    print("Parts Charges:", quote.get_parts_charges())
    print("Labor Charges:", quote.get_labor_charges())
    print("Sales Tax:", quote.get_sales_tax())
    print("Total Charges:", quote.get_total_charges())

main()