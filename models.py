class StudentProfile:
    def __init__(self,student_name,student_skills):
        self._student_name = student_name.strip()
        self._student_skills = []
        self._display_skills = []
        for skill in student_skills:
            if skill.strip().lower() not in self._student_skills:
                self._student_skills.append(skill.strip().lower())
                self._display_skills.append(skill.strip())

    def get_name(self):
        return self._student_name
    
    def get_skills(self):
        return self._student_skills
    
    def get_display_skills(self):
        return self._display_skills

class JobDescription:
    def __init__(self,job_title,company_name,required_skills,experience):
        self._job_title = job_title.strip()
        self._company_name = company_name.strip()
        self._required_skills = []
        self._display_required_skills = []
        for skill in required_skills:
            if skill.strip().lower() not in self._required_skills:
                self._required_skills.append(skill.strip().lower())
                self._display_required_skills.append(skill.strip())
        self._experience = experience 

    def get_job_title(self):
        return self._job_title

    def get_company_name(self):
        return self._company_name

    def get_required_skills(self):
        return self._required_skills
    
    def get_display_required_skills(self):
        return self._display_required_skills

    def get_experience(self):
        return self._experience
    
    
    