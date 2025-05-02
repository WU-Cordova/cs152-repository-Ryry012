from datastructures.deque import Deque
from datastructures.liststack import ListStack
from projects.project3.Customer_Order import Customer_Order

class Order_Queue:
    def __init__(self):
        self.queue = Deque(data_type= Customer_Order)
        self._complete_queue = ListStack(data_type= Customer_Order)
        
    def add_order(self, customer_order: Customer_Order) -> None:  
        self.queue.enqueue(customer_order)

    def front_order(self) -> Customer_Order:
        return self.queue.front()
    
    def complete_order(self) -> None:  
        done = self.queue.dequeue()
        self._complete_queue.push(done)
    
    def view_open_orders(self):
        if self.queue._list.empty:
            print("No open orders.")
            return

        print("\nOpen Orders:")
        temp_queue = Deque(data_type=Customer_Order)  # temp to preserve order

        while not self.queue._list.empty:
            order = self.queue.dequeue()
            print(f"- {order.name}:")
            order.repeat_order()
            temp_queue.enqueue(order)

        # Restore original queue
        while not temp_queue._list.empty:
            self.queue.enqueue(temp_queue.dequeue())

    def end_of_day_report(self) -> None:
        drink_summary = {}
        total_revenue = 0.0
        while not self._complete_queue.empty:
            order = self._complete_queue.pop()
            for drink in order._order:
                name = drink.name
                drink_summary[name] = drink_summary.get(name, {'count': 0, 'revenue': 0.0})
                drink_summary[name]['count'] += 1
                drink_summary[name]['revenue'] += drink.price
                total_revenue += drink.price

        print("\nEnd-of-Day Report:")
        for drink, stats in drink_summary.items():
            print(f"{drink}: {stats['count']} sold, ${stats['revenue']:.2f}")
        print(f"Total Revenue: ${total_revenue:.2f}")