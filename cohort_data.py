"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.
    """
    file_opened = open(filename)
    
    house_list = []
    
    for line in file_opened:
      student_list = line.rstrip().split('|')
      
      #Unpacking student_list and assigning it the corresponding variables
      (student_f,
      student_l,
      houses,
      advisor,
      cohort) = student_list
      
      #Pulling student_list[houses] and removing the '' from house_list
      if houses != '':
        house_list.append(houses)

    file_opened.close()
    #Using set function to return unique houses in file  
    return set(house_list)


      # [student_list.pop(student_list[num]) 
      # if student_list[num] == '' 
      # else student_list[num]
      # for num in range(len(student_list)-1)

      #print(student_list)
      # Another way to write the list comprehension above:
        # for num in range(len(student_list)-1):
        #   if student_list[num] == '':
        #     student_list.pop(student_list[num])
        #   else:
        #     student_list[num]
  



def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.
    """

    students = []
    file_opened = open(filename)

    for line in file_opened:
      student_list = line.rstrip().split('|')
      
      #Unpacking student_list and assigning it the corresponding variables
      (student_f,
      student_l,
      houses,
      advisor,
      cohorts) = student_list
      #If statement to check for matching cohort in the second arg 
      # while removing fake names that don't have a cohort

      if houses != '' and cohort.lower() == cohorts.lower():
        students.append(student_f + " " + student_l)
      elif cohort == 'All' and houses != '':
        students.append(student_f + " " + student_l) 

    # TODO: Create lists for each student seperated by first name, last name, houses, advisors,and cohorts
    # TODO: If cohort matches the given arg then print the names of students
    file_opened.close()
    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    file_opened = open(filename)
  
    for line in file_opened:
      (student_f,
      student_l,
      houses,
      advisor,
      cohorts) = line.rstrip().split('|')

      name = student_f + ' ' + student_l
      #Unpacking student_list and assigning it the corresponding variables
      if houses.lower() == 'gryffindor':
        gryffindor.append(name)
      elif houses.lower() == 'hufflepuff':
        hufflepuff.append(name)
      elif houses.lower() == "dumbledore's army":
        dumbledores_army.append(name)
      elif houses.lower() == 'ravenclaw':
        ravenclaw.append(name)
      elif houses.lower() == 'slytherin':
        slytherin.append(name)
      elif cohorts == 'G': 
        ghosts.append(name)
      elif cohorts == 'I':
        instructors.append(name)
    #Sorting the names in each house/instructor
    dumbledores_army.sort()
    gryffindor.sort()
    hufflepuff.sort()
    ravenclaw.sort()
    slytherin.sort()
    ghosts.sort()
    instructors.sort()

    # TODO: check for houses corresponding name and check for cohorts for ghosts or instructors
    return [dumbledores_army, gryffindor, hufflepuff,
    ravenclaw,slytherin,ghosts,instructors]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    file_opened = open(filename)
  
    for line in file_opened:
      (student_f,
      student_l,
      houses,
      advisor,
      cohorts) = line.rstrip().split('|')

      #Tupling with full name 
      each_person = tuple([student_f + " " + student_l, houses, advisor, cohorts])

      all_data.append(each_person)

      #Can combine each person into 1 line with the append function 
      # but to easily read it
      #assigned it to each_person.

      
    # TODO: Split each line into a string
    # TODO: Combine first and last name
    # TODO: Tuple everything together

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    file_opened = open(filename)
  
    for line in file_opened:
      (student_f,
      student_l,
      houses,
      advisor,
      cohorts) = line.rstrip().split('|')

      if '{} {}'.format(student_f,student_l).lower() == name.lower():
        return cohorts

    




def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    file_opened = open(filename)
    last_names_list = []

    for line in file_opened:
      (student_f,
      student_l,
      houses,
      advisor,
      cohorts) = line.rstrip().split('|')

      last_names_list.append(student_l)
    
    return set(last_names_list)



    # TODO: replace this with your code


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
