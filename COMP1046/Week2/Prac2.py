class SoccerTeam:
    def __init__(self, name):
        self.name = name
        self.__won = 0
        self.__lost = 0
        self.__draw = 0
        self.__score = 0
        self.__teamGoals = 0
        self.__oppositionGoals = 0

    def addResult(self, teamGoals, oppositionGoals):
        self.__teamGoals += teamGoals
        self.__oppositionGoals += oppositionGoals
        if teamGoals > oppositionGoals:
            self.__won +=1
            self.__score += 3
        elif oppositionGoals > teamGoals:
            self.__lost += 1
        else:
            self.__draw += 1
            self.__score += 1

    def getScore(self):
        return self.__score
    
    def goalDifference(self):
        return self.__teamGoals - self.__oppositionGoals
    
    def printReport(self):
        print(f"{self.name}: Won :{self.__won} Lost :{self.__lost} Draw : {self.__draw} Team Goals: {self.__teamGoals} Conceded : {self.__oppositionGoals} Goal Difference : {self.goalDifference()} Points: {self.__score} ")


    
    
        
