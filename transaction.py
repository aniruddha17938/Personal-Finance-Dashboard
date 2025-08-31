class TransactionNode:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date
        self.next = None

class TransactionLinkedList:
    def __init__(self):
        self.head = None

    def add_transaction(self, amount, category, date):
        new_node = TransactionNode(amount, category, date)
        new_node.next = self.head
        self.head = new_node

    def get_all_transactions(self):
        current = self.head
        transactions = []
        while current:
            transactions.append({
                'amount': current.amount,
                'category': current.category,
                'date': current.date
            })
            current = current.next
        return transactions