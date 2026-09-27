import csv

# Create a CSV file
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Salary"])
    writer.writerow(["Sandeep", 30000])
    writer.writerow(["Rahul", 25000])
    writer.writerow(["Aman", 40000])
    writer.writerow(["Priya", 35000])
    writer.writerow(["Neha", 28000])

# Read the CSV file
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    salaries = []

    for row in reader:
        salary = float(row["Salary"])
        salaries.append(salary)

# Calculate results
total = sum(salaries)
average = total / len(salaries)
highest = max(salaries)
lowest = min(salaries)

# Display report
print("----- CSV SUMMARY REPORT -----")
print("Total Employees:", len(salaries))
print("Total Salary:", total)
print("Average Salary:", average)
print("Highest Salary:", highest)
print("Lowest Salary:", lowest)