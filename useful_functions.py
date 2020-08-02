def find_in_list_of_list(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return (mylist.index(sub_list), sub_list.index(char))
    raise ValueError("'{char}' is not in list".format(char = char))
    """
        Input: mylist: list , char: searchterm
        Output: Tuple with index of Value
        Description: Find a value inside of nested lists and return it's value
    """

#def does_value_exist(cursor, list, column, value):
#    cursor.execute("SELECT * FROM ? WHERE ? = ?", (list, column, value))
#    data=cursor.fetchone()
#    if data is None:
#        return 0
#    else:
#        return 1
#    """
#        Input: cursor: the cursor object for the db
#               list: the list name
#               column: in which column to search for
#               value: the value to search for
#        Output: 0 if value is not in the column
#                1 if value is in column
#    """
