from faker import Faker
import csv
fake = Faker()
#print ("466203")

filename = "fake_data.csv"

columns = ['First Name', 'Last Name', 'Address', 'Phone Number']

rows = []

with open (filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(columns) 



#for i in range(1000):
#    print(fake.name())