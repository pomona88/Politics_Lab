voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    voting_dict = {}
    for s in voting_data:
        strlist = s.split()
        voting_dict[strlist[0]] = [int(strlist[k]) for k in range(3,len(strlist))]
    return voting_dict
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    return sum([voting_dict[sen_a][i] * voting_dict[sen_b][i] for i in range(len(voting_dict[sen_a]))])


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    
    if list(voting_dict.keys())[0] != sen:
        most = list(voting_dict.keys())[0]
    else:
        most = list(voting_dict.keys())[1]
        
    for s in list(voting_dict.keys()):
        if s != sen and policy_compare(sen, s, voting_dict) > policy_compare(sen, most, voting_dict):
            most = s        
    return most
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    if list(voting_dict.keys())[0] != sen:
        least = list(voting_dict.keys())[0]
    else:
        least = list(voting_dict.keys())[1]
        
    for s in list(voting_dict.keys()):
        if s != sen and policy_compare(sen, s, voting_dict) < policy_compare(sen, least, voting_dict):
            least = s        
    return least
    
    

## Task 5

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    sum = 0
    counter = 0
    for s in sen_set:
        if s != sen:
            sum += policy_compare(sen, s, voting_dict)
            counter += 1
    return sum / counter

# dems = {s.split()[0] for s in voting_data if s.split()[1] == 'D'}
# D = {d:lab.find_average_similarity(d, dems, voting_dict) for d in dems}
# sorted(D, key=D.get)
    
most_average_Democrat = 'Smith'


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """

    sen_list = list(sen_set)
    vote_totals = [0 for k in range(len(voting_dict[sen_list[0]]))]
    for s in sen_list:
        for k in range(len(voting_dict[sen_list[0]])):
            vote_totals[k] = (vote_totals[k] + voting_dict[s][k])
    vote_totals = [vote_totals[k] / len(sen_list) for k in range(len(voting_dict[sen_list[0]]))]
    return vote_totals

    

democrats = {s.split()[0] for s in voting_data if s.split()[1] == 'D'}
voting_dict = create_voting_dict()
average_Democrat_record = find_average_record(democrats, voting_dict)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    comp = {(s1, s2): policy_compare(s1, s2, voting_dict) for s1 in voting_dict.keys() for s2 in voting_dict.keys() if s1 < s2}
    
    return sorted(comp, key=comp.get)[0]

