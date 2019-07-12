o = open('invoice.html', 'r')
s = o.read()

name = input("Name: ")
tel = input("Phone number: ")
add1 = input("Address line 1: ")
add2 = input("Address line 2: ")
add3 = input("Address line 3: ")
bank = input("Bank: ")
account = input("Account number: ")
routing = input("Routing number: ")
attention = input("Attention: ")
position = input("Attention's position: ")
company = input("Company: ")
cadd1 = input("Company address line 1: ")
cadd2 = input("Company address line 2: ")
task = input("Task: ")
date = input("Date: ")

filled_form = (s.replace("{{ NAME }}", name)
               .replace("{{ TEL }}", tel)
               .replace("{{ ADD1 }}", add1)
               .replace("{{ ADD2 }}", add2)
               .replace("{{ ADD3 }}", add3)
               .replace("{{ BANK }}", bank)
               .replace("{{ ACCOUNT }}", account)
               .replace("{{ ROUTING }}", routing)
               .replace("{{ ATTENTION }}", attention)
               .replace("{{ POSITION }}", position)
               .replace("{{ COMPANY }}", company)
               .replace("{{ CADD1 }}", cadd1)
               .replace("{{ CADD2 }}", cadd2)
               .replace("{{ TASK }}", task)
               .replace("{{ DATE }}", date)
              )

invoices = 0

try:
    invoices = int(input("How many invoices would you like to enter? "))
except:
    invoices = 0
    
rows = []

for i in range(invoices):
    row = '''<tr>
    <td>{{ DATE }}</td>
    <td>{{ TASK }}</td>
    <td>{{ HOURS }}</td>
    <td>{{ PAY }}</td>
    </tr>
    '''
    idate = input("Date: ")
    itask = input("Task: ")
    ihours = input("Hours: ")
    ipay = input("Pay: ")
    rows.append(row.replace("{{ DATE }}", idate)
           .replace("{{ TASK }}", itask)
           .replace("{{ HOURS }}", ihours)
           .replace("{{ PAY }}", ipay)
          )
    
row = '''<tr>
<th>Total</th>
<th></th>
<th>{{ THOURS }}</th>
<th>{{ TPAY }}</th>
</tr>
'''
thours = input("Total hours: ")
tpay = input("Total pay: ")
rows.append(row.replace("{{ THOURS }}", thours)
            .replace("{{ TPAY }}", tpay)
           )
table = "\n".join(rows)

sp = filled_form.split("</table>")

final = sp[0] + "\n" + table + "\n            </table>\n" + sp[1]

f = open('../final.html', 'w')
f.write(final)