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


git init
git add .
git commit -m "Initial commit"

To track and commit the file
git add helloworld.pygit commit -m "Initial commit"

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

