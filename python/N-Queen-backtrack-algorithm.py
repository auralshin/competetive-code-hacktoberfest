# The basic approach of this alogorithm is to rollback to previous step if the current step is not going to give you a correct solution

def can_be_extended_to_solution(perm):
    """This function checks whether the solution is correct i.e if any the queen placed in current step is attacked by previously placed queens

    Args:
        perm (list): it takes the list of available permutations

    Returns:
        boolean: Either True(can be extended to solution) or False(cannot be extended to a solution)
    """

    # check if last queen is attacked by previous queens
    # for this store index of queens excpet last one
    i = len(perm) - 1

    # loop through the index of queens
    for j in range(i):
        # if they're in diagonal then it can't be extended to a solution so return False
        if i - j == abs(perm[i] - perm[j]):
            return False
            
    # if all no queens are in diagonal or attack the last queen then the solution is correct i.e return True
    return True


def extend(perm, n):
    """This function uses recursion to check if the solution is correct if the solution is correct prints the solution and exits


    Args:
        perm (list): list containing the permutations
        n (int): integer that store the no of square in each side of a board 
    """
    # if length of the permutations is equal to the length of the board i.e n then no longer to extend solution 
    # print the result and return 
    if len(perm) == n: 
        print(perm)
        return           # in this case we print all the available solutions
        exit()           # breaks out of loop to print only one solution
        
    # loop through the index n
    for k in range(n):
        # if the index already presents then we don't want to add again to the list 
        # so check if the index is in list or not 
        if k not in perm:
            # if index not in list append it to the list
            perm.append(k)

            # call ca_be_extended_to_solution with current list to see if it is correct 
            # if no conflict occurs proceed otherwise remove that element and check the previous step for solution
            if can_be_extended_to_solution(perm):
                extend(perm, n)
            perm.pop()


print(extend(perm = [], n = 8))