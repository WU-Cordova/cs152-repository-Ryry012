from Menu import Menu
from Customer_Order import Customer_Order
from Order_Queue import Order_Queue

def main():
    order_queue = Order_Queue()

    while True:
        print("\nDrink Ordering System")
        print("1. Display Menu")
        print("2. Take New Order")
        print("3. View Open Orders")
        print("4. Mark Next Order as Complete")
        print("5. End-of-Day Report")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            Menu().print_menu()
        elif choice == '2':
            name = input("Customer name: ")
            customer_order = Customer_Order(name)
            order = customer_order.take_order()
            order.repeat_order()
            confirm = input("Confirm this order? (Y/N): ").strip().upper()
            if confirm == 'Y':
                order_queue.add_order(order)
        elif choice == '3':
            order_queue.view_open_orders()
        elif choice == '4':
            order_queue.complete_order()
        elif choice == '5':
            order_queue.end_of_day_report()
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
