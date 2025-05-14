import sqlite3 #imports sqlite functions

connection_to = sqlite3.connect('email_counts.sqlite') #connects to the sql database file or creates it if not already.
cursor_hand = connection_to.cursor() #creates a cursor object to send SQL commands

cursor_hand.execute('DROP TABLE IF EXISTS Counts') #deletes 'Counts' table if it exists

cursor_hand.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''') #creates new table with 2 columns, one for email, and one for counts. 

file_name = input('Enter file name: ').strip().lower() #ask user to enter a file name
if(len(file_name) < 1): file_name = 'mbox.txt' #if no file name is entered, use 'mbox.txt' by default.

file_reader = open(file_name) #open the file_name

for line in file_reader: #go through each line in the file 
    if not line.startswith('From: '): #if line doesn't start with 'From: ', skip it
        continue #skip rest of the code in this loop and go to the next line

    words = line.split() #splits the line into individual words
    full_email = words[1] #get the second word (the email address) from the list
    org = full_email.split('@')[1] #this only gets the part after @, like 'umich.edu'

    cursor_hand.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) #asking sql to find count of specific email 

    email_record = cursor_hand.fetchone() #check if the email is already in the database
    if email_record is None:
        cursor_hand.execute(''' INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org,)) #add new email to the database starting its count at 1
        
    else:   
        cursor_hand.execute('''UPDATE Counts SET count = count + 1 
                            WHERE org = ?''', (org,)) #Find this email in the table and add 1 to its current count
    
    connection_to.commit() #saves everything we just did in the database

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10' #builds sql command to get the top 10 emails with the highest counts 

for email_record in cursor_hand.execute(sqlstr): #runs command through each row(email_record) = email and count
    print(str(email_record[0]), email_record[1]) #prints results of email addresses and their corresponding counts

cursor_hand.close() #closes up retreival of data resources 
