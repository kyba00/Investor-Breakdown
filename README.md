# Investor-Breakdown
This is a part of my Master's thesis from York University in which I explain how this program works:

This algorithm first reads the Org_Name, MR_USD, and INVS_Names from the funding
round datasheet and puts them in a list called “biglist”, as such, “biglist” is a list of lists. I
separated the investors in each round that were previously in the same field and put them in
another list called “investors_list”. Then I created a function called “share” that divides and
rounds up the investment amounts based on the number of investors in that round, the length of
“investors_list”. If there are too many investor records, as we are rounding up to 4 digits after
zero (10000th of a dollar), the accuracy falls, which is why I included a warning for accumulative
error in the code as a comment; however, the accuracy is sufficient for our purposes.
To query the data, I defined a dictionary called “db”- short for database. Then, I created a
loop. It starts by reading organization names (startups) in the funding rounds. When it encounters
a new organization, it creates a dictionary key and inputs the investors and the amount they
contributed to the organization in that funding round in the form of another dictionary as its
value. If the loop encounters an organization that it had previously seen, it will call up its key and
open its investors’ dictionary. Then it will check the investors in the new funding round against
the investors in the previous rounds. If the investor is new, it will add it as a new key with its
share of the investment as the value. If the investor is already a key in the dictionary, it will add
the amount it contributed in the new funding rounds to the amount it had invested in the previous
rounds.
After the process, each startup that had received funding (org_name) is a key in the
dictionary. The value for that key is another dictionary in which its Investors are the keys, and
the amounts they contributed throughout all the funding rounds are the values; thus, we have a
dictionary of dictionaries. The last part of the code exports the “db” dictionary into a CSV file.
That CSV file is now a replacement for the funding rounds, and it allowed me to define new
relationships in the database and make location queries. 

You can read my complete thesis at : https://yorkspace.library.yorku.ca/xmlui/bitstream/handle/10315/39141/Babashahiashtiani_Kasra_2021_Masters.pdf?sequence=2&isAllowed=y
