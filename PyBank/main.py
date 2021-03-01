
import os
import csv
import math

csvpath = os.path.join("..", "Documents", "PyBank.csv")

with open("PyBank.csv", 'r', newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        csv_header = next(rows)
        
        
        Months = []
        profit_loss_changes = []
        
        count_months = 0
        net_profit_loss = 0
        previous_month_profit_loss = 0
        current_month_profit_loss = 0
        profit_loss_change = 0
        sum_profit_loss_change = 0
        highest_change = 0
        lowest_change = 0
        average_profit_loss_change = 0
        total_rev = 0
        greatest_profit_month = 0
        greatest_loss_month = 0
        
        # calculating the total revenue and change in revenue and max and min profit:
        for row in rows:
            count_months += 1
            total_rev += int(row[1])
            current_month_profit_loss= (int(row[1]))
            net_profit_loss += current_month_profit_loss
            
            if(count_months == 1):
                previous_month_profit_loss = current_month_profit_loss
                continue
            
            else:
                Months.append(row[0])
                profit_loss_change = current_month_profit_loss-previous_month_profit_loss            
                profit_loss_changes.append(profit_loss_change)
                previous_month_profit_loss = current_month_profit_loss
                 
sum_profit_loss_change = sum(profit_loss_changes)
average_profit_loss_change = round(sum_profit_loss_change/(count_months - 1), 2)
                         
highest_change = max(profit_loss_changes)
lowest_change = min(profit_loss_changes)

greatest_profit_month = profit_loss_changes.index(highest_change)
greatest_loss_month = profit_loss_changes.index(lowest_change)

print("\nFinancial Analysis\n---------------------")
print(f"Total Months: {count_months}")
print(f"Total Revenue: ${total_rev}")
print(f"Average change in profit/loss: ${average_profit_loss_change}")
print(f"Greatest Increase in Profits: {Months[greatest_profit_month]} ${highest_change}")
print(f"Greatest Decrease in Profits: {Months[greatest_loss_month]} ${lowest_change}")
                
#  To Export text file with results.
budget_file = os.path.join("Output", "budget_data.txt")
with open("budget_data", "w") as outfile:
    
    outfile.write("Financial Analysis\n")
    outfile.write("-----------------------\n")
    outfile.write(f"Total Months: {count_months}\n")
    outfile.write(f"Total Revenue: ${total_rev}\n")
    outfile.write(f"Average change in Profit/Loss: ${average_profit_loss_change}\n")
    outfile.write(f"Greatest Increase in Profits: {Months[greatest_profit_month]} ${highest_change}\n")
    outfile.write(f"Greatest Decrease in Profits: {Months[greatest_loss_month]} ${lowest_change}\n")

                               
                
         