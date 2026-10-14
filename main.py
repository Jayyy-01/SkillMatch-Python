from models import StudentProfile, JobDescription
from manager import Manager


student = StudentProfile(
    "Jayasree",
    ["Python","SQL"]
)

job = JobDescription(
    "Python Developer",
    "Cognizant",
    ["Python","SQL","Django","REST API","Git"],
    "Fresher"
) 

manager = Manager(student,job)
manager.run_analysis()


# TEST 1: No matching skills
print("\n========== TEST 1: NO MATCHING SKILLS ==========")

student1 = StudentProfile("Student A", ["Python", "Java"])
job1 = JobDescription(
    "Data Analyst", "ABC Company",
    ["SQL", "Django", "Git"], "Fresher"
)
manager1 = Manager(student1, job1)
manager1.run_analysis()


# TEST 2: All required skills present
print("\n========== TEST 2: ALL SKILLS PRESENT ==========")

student2 = StudentProfile("Student B", ["Python", "SQL", "Django"])
job2 = JobDescription(
    "Python Developer", "ABC Company",
    ["Python", "SQL", "Django"], "Fresher"
)
manager2 = Manager(student2, job2)
manager2.run_analysis()


# TEST 3: Partial match
print("\n========== TEST 3: PARTIAL MATCH ==========")

student3 = StudentProfile("Student C", ["Python", "SQL"])
job3 = JobDescription(
    "Python Developer", "ABC Company",
    ["Python", "SQL", "Django", "Git"], "Fresher"
)
manager3 = Manager(student3, job3)
manager3.run_analysis()


# TEST 4: Student has no skills
print("\n========== TEST 4: STUDENT HAS NO SKILLS ==========")

student4 = StudentProfile("Student D", [])
job4 = JobDescription(
    "Data Scientist", "ABC Company",
    ["Python", "Machine Learning", "SQL"], "Fresher"
)
manager4 = Manager(student4, job4)
manager4.run_analysis()


# TEST 5: Job has no required skills
print("\n========== TEST 5: JOB HAS NO REQUIRED SKILLS ==========")

student5 = StudentProfile("Student E", ["Python", "SQL"])
job5 = JobDescription(
    "Developer", "ABC Company", [], "Fresher"
)
manager5 = Manager(student5, job5)
manager5.run_analysis()


# TEST 6: Uppercase and lowercase variations
print("\n========== TEST 6: CASE-INSENSITIVE MATCHING ==========")

student6 = StudentProfile("Student F", ["PYTHON", "sql", "Java"])
job6 = JobDescription(
    "Developer", "ABC Company",
    ["Python", "SQL", "JAVA"], "Fresher"
)
manager6 = Manager(student6, job6)
manager6.run_analysis()


# TEST 7: Extra spaces
print("\n========== TEST 7: EXTRA SPACES ==========")

student7 = StudentProfile("Student G", [" Python ", " SQL "])
job7 = JobDescription(
    "Developer", "ABC Company",
    ["Python ", "  SQL", " Django "], "Fresher"
)
manager7 = Manager(student7, job7)
manager7.run_analysis()


# TEST 8: Duplicate student skills
print("\n========== TEST 8: DUPLICATE STUDENT SKILLS ==========")

student8 = StudentProfile(
    "Student H", ["Python", "SQL", "Python", "SQL"]
)
job8 = JobDescription(
    "Developer", "ABC Company",
    ["Python", "SQL", "Java"], "Fresher"
)
manager8 = Manager(student8, job8)
manager8.run_analysis()


# TEST 9: Duplicate job skills
print("\n========== TEST 9: DUPLICATE JOB SKILLS ==========")

student9 = StudentProfile("Student I", ["Python", "SQL"])
job9 = JobDescription(
    "Developer", "ABC Company",
    ["Python", "SQL", "Python", "SQL", "Java"], "Fresher"
)
manager9 = Manager(student9, job9)
manager9.run_analysis()


# TEST 10: Both skill lists empty
print("\n========== TEST 10: BOTH SKILL LISTS EMPTY ==========")

student10 = StudentProfile("Student J", [])
job10 = JobDescription(
    "Developer", "ABC Company", [], "Fresher"
)
manager10 = Manager(student10, job10)
manager10.run_analysis()
