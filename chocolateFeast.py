def chocolateFeast(n, c, m):
    # Write your code here
    num_choc = n // c
    choc_counter = num_choc
    number_wrappers = num_choc

    while number_wrappers >= m:
        num_choc = number_wrappers//m
        choc_counter += num_choc

        remaining_wrappers = number_wrappers % m
        number_wrappers = remaining_wrappers + num_choc


    return choc_counter
