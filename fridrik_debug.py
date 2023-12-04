from data.customer_data import Customer_Data

data_class = Customer_Data()
result = data_class.read_all_customers()
for elem in result:
    print(elem)