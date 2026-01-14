if subject not in self.__enroll:
            return "Not Found"
        if grade == 'A':
            self.__totle += 4.0 * subject.number
            self.__credit += subject.number
        elif grade == 'B':
            self.__totle += 3.0 * subject.number
            self.__credit += subject.number
        elif grade == 'C':
            self.__totle += 2.0 * subject.number
            self.__credit += subject.number
        else:
            return "Invalid Grade"
        return "Done"