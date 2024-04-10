import sys

while True:
    
    file_variable=input('''
    what file would you like to search for?:
    a) 60s-music file
    b)  athletes file  
    x)   to exit                
    ''')

    if file_variable == 'x':
        sys.exit()
    elif file_variable =='a':
        file_variable ='60s-music.csv'
    elif file_variable == 'b':
        file_variable ='athletes.csv' 
    else:
        print('invalid option. Please select a,b,or x.')
        continue

    
    search_variable = input(f'Enter the search term for {file_variable} file:')
    search_variable = search_variable.title()

    
    def find(file_variable,search_variable): 
        with open(file_variable,'r') as file:
            content = file.read()

            if search_variable in content:

                print(f' your search term {search_variable} exists in the {file_variable} file!')
                see_entries = input('would you like to see the entries? (y or n)?')

                if see_entries.lower() == 'y':
                    print(f'here are all of the entries with the term{search_variable}:')
                    with open(file_variable, 'r') as file:
                        for line in file:
                            if search_variable in line:
                                print(line.strip())

                elif see_entries.lower()== 'n':
                    print('Goodbye')
                    sys.exit()  

                else:
                    print("invalid option. please enter y or n")

            else:
                print(f'{search_variable} does not exist in {file_variable}')

    find(file_variable, search_variable)  