# SkillMatch-Python

A beginner-friendly, object-oriented Python application that evaluates how well a student's technical skills align with job requirements. The system identifies matching and missing skills, calculates a skill match percentage, and generates a structured analysis report.

## Overview

SkillMatch-Python helps students understand how their existing technical skills compare with the requirements of a particular job role.

The application accepts a student profile and a job description, compares their skill sets, and generates a report containing:

- Student and job information
- Total number of unique required skills
- Matching technical skills
- Missing technical skills
- Overall skill match percentage
- A summary explaining the matching result

The project demonstrates core Python Object-Oriented Programming (OOP) concepts through a modular and maintainable code structure.

## Key Features

- **Skill Matching:** Identifies technical skills shared by the student and the job description.
- **Missing Skill Detection:** Highlights the required skills that the student does not currently possess.
- **Match Percentage Calculation:** Calculates the percentage of required skills matched by the student.
- **Skill Normalization:** Handles uppercase and lowercase variations and removes unnecessary leading and trailing spaces.
- **Duplicate Handling:** Removes duplicate skills without affecting the matching calculation.
- **Case-Insensitive Comparison:** Compares skills without considering letter case.
- **Edge Case Handling:** Supports empty skill lists, zero matches, complete matches, and other input variations.
- **Modular Architecture:** Separates data models, analysis logic, and report management into individual Python modules.

## Project Structure

```text
SkillMatch-Python/
│
├── main.py
├── models.py
├── analyzers.py
├── manager.py
├── README.md
└── .gitignore
```

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python 3 |
| Programming Paradigm | Object-Oriented Programming |
| Core Concepts | Inheritance, Encapsulation, Polymorphism, Abstraction |
| Data Structures | Lists |
| Version Control | Git |
| Code Hosting | GitHub |

**Dependencies:** No external Python libraries are required. The project uses Python's built-in functionality.

## System Architecture

The application follows a modular architecture with four primary Python modules.

### 1. `models.py` - Data Models

Defines the two main classes:

- **StudentProfile:** Stores the student's name and technical skills.
- **JobDescription:** Stores the job title, company name, required skills, and experience level.

Both classes normalize skill names and remove duplicates while preserving readable skill names for the final report.

### 2. `analyzers.py` - Analysis Components

Contains an abstract base class and two specialized analyzers:

- **SkillAnalyzer:** Defines the common analysis interface through an abstract `analyze()` method.
- **MatchScoreCalculator:** Identifies matching skills and calculates the match percentage.
- **MissingSkillDetector:** Identifies the required skills that are missing from the student's profile.

### 3. `manager.py` - Analysis Management

The `Manager` class coordinates the analysis process.

It maintains a collection of analyzer objects, invokes their common `analyze()` method, collects the results, and generates the final report.

### 4. `main.py` - Application Entry Point

Creates student profiles and job descriptions, initializes the manager, and executes the analysis.

It also contains test scenarios covering different matching conditions and edge cases.

## Skill Matching Logic

The system compares normalized student skills with normalized job requirements.

**Match Percentage Formula:**

```text
Match Percentage = (Matching Skills / Total Required Skills) × 100
```

For example:

- Total required skills: 5
- Matching skills: 2
- Missing skills: 3

```text
Match Percentage = (2 / 5) × 100 = 40%
```

If the job description contains no required skills, the system returns a match score of `0%` to avoid division by zero.

## Matching Rules

The application follows these rules when comparing skills:

1. Skill comparison is case-insensitive.
2. Leading and trailing spaces are removed.
3. Only complete skill-name matches are considered.
4. Duplicate student skills are counted only once.
5. Duplicate job requirements are counted only once.
6. Original readable skill names are retained in the generated report.

For example:

```text
Student Skills:  ["PYTHON", " SQL ", "Java"]
Required Skills: ["Python", "SQL", "JAVA"]
```

**Result:** All three skills match, giving a score of `100%`.

## Sample Output

```text
STUDENT-JOB SKILL ANALYSIS REPORT

Student Name: Jayasree
Job Title: Python Developer
Required Skills: 5

Matching Skills:
- Python
- SQL

Missing Skills:
- Django
- REST API
- Git

Match Score: 40%

Explanation:
The student matches 2 out of 5 unique required skills.
Therefore, the skill match percentage is 40%.
```

## Object-Oriented Programming Concepts

This project demonstrates the following OOP principles:

| Concept | Implementation |
|---|---|
| Encapsulation | Profile data is maintained using internal attributes and accessed through getter methods. |
| Abstraction | `SkillAnalyzer` defines a common abstract analysis interface. |
| Inheritance | `MatchScoreCalculator` and `MissingSkillDetector` inherit from `SkillAnalyzer`. |
| Polymorphism | The Manager invokes the same `analyze()` method on different analyzer objects, each performing a different operation. |

## Test Scenarios

The application includes test scenarios to evaluate its behavior under different conditions.

| Test Case | Expected Result |
|---|---:|
| No matching skills | 0% |
| All required skills present | 100% |
| Partial skill match | 50% |
| Student has no skills | 0% |
| Job has no required skills | 0% |
| Uppercase and lowercase variations | 100% |
| Skills containing extra spaces | 66.67% |
| Duplicate student skills | 66.67% |
| Duplicate job requirements | 66.67% |
| Both skill lists are empty | 0% |

These scenarios are included in `main.py` to demonstrate the application's handling of normal and edge-case inputs. The expected percentages should be verified against the actual test data.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Git installed on your system (optional, for cloning the repository).

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Jayyy-01/SkillMatch-Python.git
```

**2. Navigate to the project directory**

```bash
cd SkillMatch-Python
```

**3. Run the application**

```bash
python main.py
```

The application executes the student-job skill analysis and displays the generated reports in the terminal.

## Current Scope and Limitations

- Skill matching is based on exact skill-name comparison after normalization.
- The application uses manually provided student skills and job requirements.
- The match percentage represents skill overlap, not an overall measure of job suitability.
- The current implementation uses an in-memory approach and does not persist profiles or job descriptions.

## Future Enhancements

Potential improvements for future versions include:

- Interactive input for student profiles and job descriptions.
- Support for uploading resumes and extracting skills.
- Automated extraction of required skills from job descriptions.
- Skill recommendations based on missing requirements.
- A graphical user interface for easier interaction.

## Author

**Jayyy-01**

GitHub: [@Jayyy-01](https://github.com/Jayyy-01)


This project is available for learning and educational purposes. A formal open-source license can be added to the repository if redistribution or reuse permissions are required.
