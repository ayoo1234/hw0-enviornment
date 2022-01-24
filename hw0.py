from faker import Faker
import csv
fake = Faker()
fake.seed(466203)


filename = 'fake_data.csv'

columns = ['First Name', 'Last Name', 'Address', 'Phone Number']
rows = []

for i in range(1000):
    newRow = []
    firstName = fake.first_name()
    lastName = fake.last_name()
    address = fake.address()
    phoneNumber = fake.phone_number()

    newRow.append(firstName)
    newRow.append(lastName)
    newRow.append(address)
    newRow.append(phoneNumber)

    rows.append(newRow)


with open (filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(columns) 

    csvwriter.writerows(rows) 




