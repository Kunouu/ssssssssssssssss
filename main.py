import psycopg2
import csv
conn = psycopg2.connect(host = 'localhost',
                        database = 'gitbd',
                        user = 'postgres',
                        password = 123456)

fields = ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address']



with open('gitbd', 'w') as file:
    
    write = csv.writer(file)
    write.writerow(fields)