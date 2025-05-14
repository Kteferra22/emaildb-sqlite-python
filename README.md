📬 Email Domain Frequency Tracker

This Python script reads an email log file, extracts domain names from sender addresses, and stores domain counts in a SQLite database.

🔧 Features
1. Parses lines starting with From: in a text file.
 
2. Extracts domain names from email addresses.

3. Creates a SQLite database with a Counts table:
   - org: domain name
   - count: number of occurrences

4. Updates domain counts incrementally.

5. Outputs the top 10 domains by frequency.
   

📁 File Structure

email_counts.sqlite      #Generated SQLite database

mbox.txt                 #Sample input file (or user-provided)

email_count_script.py    #Main script


🧪 Example Input (mbox.txt)

From: alice@umich.edu   (@umich)

From: bob@gmail.com   (@gmail)

From: alice@umich.edu   (@umich)


🚀 Getting Started
Prerequisites

1. Python 3.x
   
2. Email log file (e.g., mbox.txt) in the same directory

Running the Script

1. python email_count_script.py
   
- When prompted, enter the input file name. If left blank, it defaults to mbox.txt.
  

🗃️ Database Schema

Counts(org TEXT, count INTEGER)


🧩 Sample Output

umich.edu 2

gmail.com 1


📌 Notes
1. The script will overwrite email_counts.sqlite if it already exists.

2. Only domains from lines starting with From: are counted.

3. The script displays the top 10 domains sorted by frequency.
