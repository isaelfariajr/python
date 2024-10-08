def import_and_create_dictionary(fileName):
    """This function is used to create an expense dictionary from a file.
    Every line in the file should be in the format:
      key, value
    The key is a user's name and the value is an expense to update the user's
    total expense with.
    The value should be a number, however, it is possible that there is no value,
    that the value is an invalid number, or that the entire line is blank."""

    #create empty dictionary
    expenses = {}
    #Open file in read mode and read all line into a list
    f = open(fileName, "r")
    lines = f.readlines()

    for line in lines:
        #Strip whitespace from beginning and end of line
        #split into a list based on comma separator
        lst = line.strip().split(",")
        #skipt line if missing value (expense amount)
        if len(lst) <= 1:
            continue
        #get key (name) and value (expense amount) from list
        key = lst[0].strip()
        value = lst[1].strip()

        try:
            #Cast value to float
            value = float(value)
            # add new expense amount to current total expense amount
            # associated with key (name), or 0
            # associate the new total expense amount with key (name)
            expenses[key] = expenses.get(key,0) + value
        except:
            #otherwise go to top for loop, to next line in list of lines
            continue
    f.close()
    return expenses

def main():
    expenses = import_and_create_dictionary('Mod 4 Code Files/Module 4 Code Files/expenses.txt')
    print('expenses:', expenses)

if __name__ == '__main__':
    main()