from customer import Customer

def main():
    print("Customer 1")
    email = str(input("Enter email"))
    customer = Customer(email)
    customer.input_info()
    customer.verify_info()
    print("Customer 2:")
    email_two = str(input("Enter email"))
    customer_two = Customer(email_two)
    customer_two.input_info()
    customer_two.verify_info()
    customer.output_info()
    customer_two.output_info()
main()
