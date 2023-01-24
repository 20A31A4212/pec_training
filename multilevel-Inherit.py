###################MULTI-LEVEL-INHERITANCE#######################

class AcademicDean:
    print("order the principal to do the work")


class Principal(AcademicDean):
    print("do the work given by academic dean")



class Teachers(Principal):
    print("do the work given by principal")



class Students(Teachers):
    print("do the work given by teachers")

obj1=Students()