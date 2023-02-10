cost = float(input("Cost of the meal: "))
service_charge = float(input("Service Charge amount:"))
GST = float(input("GST amount: "))

service_charge_cost = service_charge/100 * cost
gst_cost = GST/100 * cost
total_cost = cost + service_charge_cost + gst_cost
print("Service Charge Amount: ", service_charge_cost)
print("Gst Amount: ", gst_cost)
print("Total cost:", total_cost)
no_people = int(input("How many people is sharing the cost?: "))
one_person = total_cost/no_people
print("How much one person needs to pay:", one_person)