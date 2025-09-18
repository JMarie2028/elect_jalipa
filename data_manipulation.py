aqi_values = [50, 65, 55, 80, 70, 65, 90, 100]  
average_aqi = sum(aqi_values) / len(aqi_values)
unique_aqi = set(aqi_values)
aqi_count = {
    50: aqi_values.count(50),
    65: aqi_values.count(65),
    55: aqi_values.count(55),
    80: aqi_values.count(80),
    70: aqi_values.count(70),
    90: aqi_values.count(90),
    100: aqi_values.count(100)
}

print("AQI Values (List):", aqi_values)
print("Average AQI:", average_aqi)
print("Unique AQI Values (Set):", unique_aqi)
print("AQI Frequency (Dictionary):", aqi_count)

students = [("Jay", 15, "10th", "Photon"),("Johnica", 15, "9th", "Photon"),
("Janel", 15, "11th", "Tau"),("Mraye", 15, "10th", "Graviton"),
("Adi", 15, "12th", "Tau")]


third = students[2]
print("Info of the 3rd Student:")
print("Name:", third[0])
print("Grade Level:", third[2])
print("Section:", third[3])
print()  

grades = {
    "Jay": 85,
    "Johnica": 78,
    "Janel": 92,
    "Mraye": 88,
    "Adi": 81
}

print("Grade of first student (Jay):", grades["Jay"])

grades["Jay"] = 90
print("Grade of first student (Jay) [UPDATED]:", grades["Jay"])

print()
students.append(("Scott", 15, "10th", "Photon"))
grades["Scott"] = 100
print("Added new student named Scott with grade:", grades["Scott"])
git init
git add .
git commit -m "Initial commit"

To track and commit the file
git add helloworld.py

git commit -m "Initial commit: Added main.py"

Step 4 – Push to GitHub
On GitHub, create a new repository named CS_Elective.


Copy the remote link provided by GitHub.


In the terminal, run:

	git remote add origin <repository-link>
git branch -M main
git push -u origin main


Example: 


Step 5 – Verification
Open your GitHub repository and check if your code is there.

Step 6 – Modify your Python file
print("Hello, GitHub! Now this is version 2.")

Step 7 – Commit the changes
git add helloworld.py
git commit -m "Updated greeting to version 2"

Step 8 – View version history
git log --oneline

Step 9 – Check the GitHub 

Step 10 – Run your Python file
python helloworld

