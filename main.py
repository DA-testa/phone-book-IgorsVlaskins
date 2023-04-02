class Contact:
    def __init__(self, number, name):
        self.number = number
        self.name = name

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, number, name):
        self.contacts[number] = Contact(number, name)

    def del_contact(self, number):
        if number in self.contacts:
            del self.contacts[number]

    def find_contact(self, number):
        if number in self.contacts:
            return self.contacts[number].name
        else:
            return "not found"

def process_queries(queries):
    phone_book = PhoneBook()
    result = []
    for query in queries:
        query_parts = query.split()
        if query_parts[0] == "add":
            phone_book.add_contact(int(query_parts[1]), query_parts[2])
        elif query_parts[0] == "del":
            phone_book.del_contact(int(query_parts[1]))
        elif query_parts[0] == "find":
            result.append(phone_book.find_contact(int(query_parts[1])))
    return result

if __name__ == '__main__':
    n = int(input())
    queries = [input() for i in range(n)]
    result = process_queries(queries)
    print("\n".join(result))
