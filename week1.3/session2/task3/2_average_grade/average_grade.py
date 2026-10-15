# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
with open("student_data.csv", "r") as infile:
    with open("report.txt", "w") as outfile:
        for i in infile.readlines()[1:]:
            x = i.strip().split(",")
            average = (int(x[2]) + int(x[3]) + int(x[4])) / 3
            with open("report.txt", "a") as outfile:
                outfile.write(f"{x[1]}'s average grade is {round(average, 2)} \n")

            




# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
