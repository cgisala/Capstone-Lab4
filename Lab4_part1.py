"""
This allows the user to do tfollowing:
- adds new records
- delete records
- update records
- search the database by name
to the chainsaw juggling database
"""
import sqlite3

db= 'chainsaw_juggling.sqlite'  # Assumes the table record_holders have already been created.

def main():
    choice = True

    while choice:
        print('\nMENU: \n'
        '1: add new record\n'
        '2: update record\n'
        '3: delete record\n'
        '4: search database\n')

        # Prompts the user to enter the choice form the menu
        menuOption = input('What is your choice? ')

        if menuOption == '1':
            add_record(db)
        elif menuOption == '2':
            update_record(db)
        elif menuOption == '3':
            delete_record(db)
        elif menuOption == '4':
            search_database(db)
        else:
            print('\nYour choice is not in the menu')

        # Asks the user of he or she wants to continue 
        userChoice = input('\nDo you wish to continue? y or n: ')
        if userChoice.lower() == 'y':
            choice = True
        else:
            choice = False

            # Prints all the data in the table
            conn = sqlite3.connect('chainsaw_juggling.sqlite')
            cur = conn.execute('select * from record_holders')

            print('\n**Chainsaw Juggling Record Holders**\n')
            for row in cur:
                print(row)

            # Close connection
            conn.close()

            

def add_record(db):
    conn = sqlite3.connect(db) # Creates or opens connection to db file

    #Ask the user for information about the juggler
    name = input('Enter the name of the juggler: ')
    country = input('Enter the name of the country the juggler is from: ')
    numOfCatches = input('Enter the number of catches of the juggler: ')

    # Parameters
    conn.execute('insert into record_holders values (?,?,?)', (name, country, numOfCatches))
    conn.commit()  # Saves changes to database
    conn.close()  # Close connection

def update_record(db):
    
    # User enters the name of the jugglers
    name = input('\nEnter the name of the juggler: ')
    numOfCatches = int(input('\nEnter the number of catches: '))

    conn = sqlite3.connect(db)  # Creates or opens connection to db file

    # Updates the number of catches of a juggler
    conn.execute('''Update record_holders SET number_of_catches = ? WHERE name = ?''',(numOfCatches, name))
    conn.commit() # Saves changes to database
    conn.close() # Close connection

def delete_record(db):

    #Prompts the user for the name to delete from record
    name = input('\nEnter the name to be deleted: ')

    conn = sqlite3.connect(db)   # Creates or opens connectiion to db file
    curs = conn.cursor()
    curs.execute("DELETE FROM record_holders WHERE name = (?)", (name,))
    conn.commit() #Saves changes to database
    conn.close() #Close Connection
    



def search_database(db):

    # User enters the data to be searched by name
    name = input('\nEnter the name of the juggler: ')

    get_record_by_name = "SELECT name, * FROM record_holders WHERE name = ?"

    conn = sqlite3.connect(db)  # Creates or opens connection to db file

    conn.row_factory = sqlite3.Row # This row_factory allows access to data by row name
    rows = conn.execute(get_record_by_name, (name,) )
    juggler_data = rows.fetchone() #Get first result

    print('\nJuggler Data:')

    # Prints the jugglers data
    print(juggler_data['name'], juggler_data['country'], juggler_data['number_of_catches'])
    conn.close()     # Close connection

if __name__=='__main__':
    main()