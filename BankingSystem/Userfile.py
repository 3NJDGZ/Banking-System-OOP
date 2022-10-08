import csv

class User:
    all = []
    def __init__(self, FirstName: str, LastName: str, Email: str, Gender: str, Age: int):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Gender = Gender
        self.Age = Age

        User.all.append(self)

    @classmethod
    def identify_user(cls, queried_name):
        with open('table.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
     
        for item in items:
            found = False
            full_name = (item["FirstName"]).lower() + " " + (item["LastName"]).lower()
            if queried_name.lower() == full_name:
                print(f"\nSuccessfully found!\n_______Details_______ \nName: {full_name.title()}\nEmail: {item['Email']}\nGender: {item['Gender']}\nAge: {item['Age']}\nPasscode: {item['Passcode']}")
                found = True
                break
        
        if not found:
            print(f"\nUnsucessful. The User ('{queried_name.title()}') cannot be found within our database.")
    
    @classmethod
    def register_user(cls, firstname, lastname, email, gender, age: int, bankname, balance: float, passcode: int):
        new_row = [firstname, lastname, email, gender, age, bankname, balance, passcode]
        with open('table.csv', 'a', newline='') as f:
            writer_obj = csv.writer(f)
            # next(writer_obj)
            writer_obj.writerow(new_row)
            f.close()

    def __repr__(self):
        return f"User('{self.FirstName}', {self.LastName}, {self.Email}, {self.Gender}, {self.Age})"
    
    
