shop_name= "Lower Manhattan"
drink_price= 3.0
drinks_sold= 143
pastries_price= 3.5
pastry_sold= 33

#compute revenue
drink_revenue= drinks_sold*drink_price
pastry_revenue=pastry_sold*pastries_price
total_revenue= drink_revenue+pastry_revenue

#check the numbers
print("shop:", shop_name)
print("dirink revenue:",drink_revenue)
print("pastry revenue:", pastry_revenue)
print("total:", total_revenue)

#check total >=500
if total_revenue >= 500:
    print("yes,at least $500")
else:
    print("no,less than $500")

#save results to a file
file = open("sales_report.txt","w")
file.write("Shop: " + shop_name + "\n")
file.write("Total revenue: $" + str(total_revenue)+"\n")
file.close()