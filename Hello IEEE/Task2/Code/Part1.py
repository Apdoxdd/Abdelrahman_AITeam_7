import numpy as np
def p1():

    data = [
      [85,78,92,88],
      [70,76,80,65],
      [90,88,94,91],
      [60,65,58,62],
      [100,95,98,97]
     ]
    grades = np.array(data)
    


    
    print("The grades shape: ",grades.shape)
    mean_student = np.mean(grades,1)
    mean_student=mean_student[:,np.newaxis]
    print("Each Student mean: ",mean_student)

    mean_subject= np.mean(grades,0)
    mean_subject= mean_subject[np.newaxis,:]
    print("Each Subject mean: ",mean_subject)

    greater_85 = mean_student[mean_student>85]
    print("Each student who's grade above 85", greater_85)
    grades_p_5 = grades + 5
    print("Grades with broadcasting 5", grades_p_5)
    maxes = np.max(grades,0)
    mins = np.min(grades,0)
    nomalized_arr = (grades-mins)/(maxes-mins)
    print("Normalized Grades: ",nomalized_arr)
    flattened = grades.flatten()
    print("Flattened Grades: ",flattened)



if __name__ == "__main__":
    p1()