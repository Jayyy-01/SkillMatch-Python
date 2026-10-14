from analyzers import MatchScoreCalculator, MissingSkillDetector

class Manager:
    def __init__(self,student,job):
        self.student = student
        self.job = job
        self.analyzers = [MatchScoreCalculator(),MissingSkillDetector()]
    
    
    def run_analysis(self):
        matching_skills = []
        matching_percentage = 0.0
        missing_skills = []

        for analyzer in self.analyzers:
            result = analyzer.analyze(self.student, self.job)

            if isinstance(analyzer, MatchScoreCalculator):
                matching_skills, matching_percentage = result

            elif isinstance(analyzer, MissingSkillDetector):
                missing_skills = result

        required_skills = self.job.get_required_skills()

        print("\nSTUDENT-JOB SKILL ANALYSIS REPORT\n")

        print("Student Name:", self.student.get_name())
        print("Job Title:", self.job.get_job_title())
        print("Required Skills:", len(required_skills))

        print("\nMatching Skills:")
        for skill in matching_skills:
            print("-", skill)

        print("\nMissing Skills:")
        for skill in missing_skills:
            print("-", skill)

        print("\nMatch Score:", f"{matching_percentage:g}%")

        print("\nExplanation:")
        print(
            "The student matches",
            len(matching_skills),
            "out of",
            len(required_skills),
            "unique required skills. Therefore, the skill match percentage is",
            f"{matching_percentage:g}%."
        )

