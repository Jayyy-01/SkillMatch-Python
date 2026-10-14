
from abc import ABC, abstractmethod


class SkillAnalyzer(ABC):
    @abstractmethod
    def analyze(self, student, job):
        pass


class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self, student, job):
        student_skills = student.get_skills()
        required_skills = job.get_required_skills()
        display_required_skills = job.get_display_required_skills()

        matching_skills = []

        for i in range(len(required_skills)):
            if required_skills[i] in student_skills:
                matching_skills.append(display_required_skills[i])

        total_matching_skills = len(matching_skills)
        total_required_skills = len(required_skills)

        if total_required_skills == 0:
            matching_percentage = 0.0
        else:
            matching_percentage = (
                total_matching_skills / total_required_skills
            ) * 100

        return matching_skills, matching_percentage


class MissingSkillDetector(SkillAnalyzer):
    def analyze(self, student, job):
        student_skills = student.get_skills()
        required_skills = job.get_required_skills()
        display_required_skills = job.get_display_required_skills()

        missing_skills = []

        for i in range(len(required_skills)):
            if required_skills[i] not in student_skills:
                missing_skills.append(display_required_skills[i])

        return missing_skills
