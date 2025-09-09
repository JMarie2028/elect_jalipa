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

students.append(("Scott", 15, "10th", "Photon"))
grades["Scott"] = 100
print("Added new student named Scott with grade:", grades["Scott"])
