class TechWorld:
    def __init__(self, name: str, skills: list, experience: float, average_feedback: float):
        self.__name = name
        self.__skills = skills
        self.__experience = experience
        self.__average_feedback = average_feedback
    
    def get_details(self):
        return self.__name, self.__skills, self.__experience, self.average_feedback
    
    def check_eligibility(self):
        if self.__experience > 3 and self.__average_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__average_feedback >= 4:
            return True
        else:
            False
    
    def allocate_course(self, technology):
        if not self.check_eligibility():
            return False
        if technology in self.__skills:
            return True
        else:
            False

obj1 = TechWorld(
    name = "Dexter",
    skills = ['C++', 'Python', 'Java'],
    experience = 5,
    average_feedback = 4.5
)
print(obj1.allocate_course(technology = "C++"))