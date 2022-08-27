import csv
import matplotlib.pyplot as plt

try:
    with open('Cupcakeinvoices.csv', 'r', newline='') as file:
        allreader = csv.reader(file, delimiter=',', quotechar='|')
        #for row in allreader:
        #    print(' --> '.join(row))

        typesreader = csv.DictReader(file)
        all_types = [row['type'] for row in typesreader]
        unique_types = list(set(all_types))
        #print(unique_types)

        #sum_invoices = []

        #for row in typesreader:
            #print(f"{row['name']} {row['surname']}`s invoice is {int(row['amount']) * float(row['price']):.2f}")

            #invoice = int(row['amount']) * float(row['price'])
            #sum_invoices.append(invoice)
        
        #print(sum(sum_invoices))

        #sum_invoices = [int(row['amount']) * float(row['price']) for row in typesreader]
        #print(sum(sum_invoices))

        
        sum_invoices_chocolate = 0
        sum_invoices_vanilla = 0
        sum_invoices_strawberry = 0

        for row in typesreader:
            if row['type'] == 'Chocolate':
                sum_invoices_chocolate += int(row['amount']) * float(row['price'])
            elif row['type'] == 'Vanilla':
                sum_invoices_vanilla += int(row['amount']) * float(row['price'])
            elif row['type'] == 'Strawberry':
                sum_invoices_strawberry += int(row['amount']) * float(row['price'])

        #print(sum_invoices_chocolate)
        #print(sum_invoices_vanilla)
        #print(sum_invoices_strawberry)

        total_invoices = [sum_invoices_chocolate, sum_invoices_vanilla, sum_invoices_strawberry]

        plt.bar(unique_types, total_invoices, color = 'g', width = 0.72, label = "Invoices")
        plt.xlabel('Type')
        plt.ylabel('Amount')
        plt.title('Invoices')
        plt.legend()
        plt.show()


except:
    print('ERROR opening the file')