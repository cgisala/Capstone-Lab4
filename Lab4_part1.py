"""
This allows the user to do tfollowing:
- adds new records
- delete records
- update records
- search the database by name
to the chainsaw juggling database
"""
import sqlite3

# db_url = 'chainsaw_juggling.sqlite'  # Assumes the table record_holders have already been created.

def main():
    choice = True

    while choice:
        print('\nMENU: \n'
        '1: add new record\n'
        '2: update record\n'
        '3: delete record\n'
        '4: search database\n')

        menuOption = input('What is your choice? ')

        if menuOption == '1':
            add_record()
        elif menuOption == '2':
            search_database()
        elif menuOption == '3':
            pass
        elif menuOption == '4':
            pass
        else:
            print('\nYour choice is not in the menu')

        userChoice = input('\nDo you wish to continue? y or n: ')
        if userChoice.lower() == 'y':
            choice = True
        else:
            choice = False
            conn = sqlite3.connect('chainsaw_juggling.sqlite')
            cur = conn.execute('select * from record_holders')

            for row in cur:
                print(row)

            # Close connection
            conn.close()

            

def add_record():
    # Creates or opens connection to db file
    conn = sqlite3.connect('chainsaw_juggling.sqlite')

    #Ask the user for information about the juggler
    name = input('Enter the name of the juggler: ')
    country = input('Enter the name of the country the juggler is from: ')
    numOfCatches = input('Enter the number of catches of the juggler: ')

    # Parameters
    conn.execute('insert into record_holders values (?,?,?)', (name, country, numOfCatches))

    # Saves changes to database
    conn.commit()

    # Close connection
    conn.close()



def update_record():
    pass

def delete_record():
    pass

def search_database():

    # User enters the data to be searched by name
    name = input('\nEnter the name of the juggler: ')

    get_record_by_name = "SELECT name, * FROM record_holders WHERE name = ?"

    # Creates or opens connection to db file
    conn = sqlite3.connect('chainsaw_juggling.sqlite')

    conn.row_factory = sqlite3.Row # This row_factory allows access to data by row name
    rows = conn.execute(get_record_by_name, (name,) )
    juggler_data = rows.fetchone() #Get first result

    print('\nJuggler Data:')

    # Prints the jugglers data
    print(juggler_data['name'], juggler_data['country'], juggler_data['number_of_catches'])

    # Close connection
    conn.close()

if __name__=='__main__':
    main()