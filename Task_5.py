class ContactBook:
    def __init__(self):
        self.__data = {}
    
    def add_contact(self, name=None, address=None, phone_number=None, email=None):
        if name and address and phone_number and email:
            if phone_number not in self.__data:
                self.__data[phone_number] = [name, address, phone_number, email]
                print("Added successfully")
            else:
                print("Number already exists")
        else:
            print("Please enter all the values")

    def delete_contact(self, phone_number=None):
        if phone_number:
            if phone_number in self.__data:
                del self.__data[phone_number]
                print("Deleted successfully")
            else:
                print("Phone number does not exist in the database")
        else:
            print("Please enter a phone number")

    def edit_contact(self, name=None, address=None, phone_number=None, email=None):
        if phone_number and phone_number in self.__data:
            if name:
                self.__data[phone_number][0] = name
            if address:
                self.__data[phone_number][1] = address
            if email:
                self.__data[phone_number][3] = email
            print("Data updated successfully")
        else:
            print("Phone number does not exist in the database")

    def search_contact(self, query=None, sort_field=None):
        if query:
            search_arr = [(key, val) for key, val in self.__data.items()]
            result = [val for key, val in search_arr if query.lower() in " ".join(val).lower()]
            
            if sort_field:
                sort_indices = {
                    "name": 0,
                    "address": 1,
                    "phone_number": 2,
                    "email": 3
                }
                if sort_field in sort_indices:
                    result.sort(key=lambda x: x[sort_indices[sort_field]])
            
            self.view_contacts(result)
        else:
            print("No query provided.")

    def view_contacts(self, data=None):
        if data is None:
            data = list(self.__data.values())
        
        table = BeautifulTable()
        table.columns.header = ["Name", "Address", "Phone Number", "Email"]
        
        for contact in data:
            table.rows.append(contact)

        print(table)

    def console(self):
        while True:
            try:
                print("\n1. Add Contact\n2. Delete Contact\n3. Edit Contact\n4. Search Contact\n5. View Contacts\n6. Stop")
                n = int(input("Enter your option: "))
                
                if n == 1:
                    name = input("Name: ")
                    address = input("Address: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    self.add_contact(name or None, address or None, phone_number or None, email or None)

                elif n == 2:
                    phone_number = input("Phone Number: ")
                    self.delete_contact(phone_number or None)
                
                elif n == 3:
                    name = input("Name: ")
                    address = input("Address: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    self.edit_contact(name or None, address or None, phone_number or None, email or None)
                
                elif n == 4:
                    query = input("Search: ")
                    sort_by = input("Sort by (name, address, phone_number, email): ")
                    self.search_contact(query or None, sort_by or None)

                elif n == 5:
                    self.view_contacts()
                
                elif n == 6:
                    print("Exiting Contact Book. Goodbye!")
                    break

                else:
                    print("Invalid option. Please enter a number between 1 and 6.")
            
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.console()
