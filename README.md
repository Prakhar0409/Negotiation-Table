#Negotiation Table

## How to set it up on your laptop?

Setting up the application on your laptop is as easy as abc. Steps are as follows:
1. Install `python3` using any of the standard method on your computer.
2. Install `django 1.10.1` or later. (Application is compatible with older versions as well but newer are recommended)
3. Enter the project parent directory (where you can find manage.py)
4. Create a database in mysql named ```tmpDB```
5. Run `python3 manage.py migrate`
6. python `python3 manage.py createsuperuser`
7. Run `python3 manage.py runserver`

## Using application prototype?
Visit `localhost:8000/admin` and login using the superuser credentials you created above. 
Following tables stand for the following things in the application.

1. Material : Product to be traded during the game play
2. Company : Entries for companies
3. Nation : Entries for Countries
4. Bank : Entry for banks
  * You can actually stop after populating these and continue onto the next step (or may read the following to understand the terminology)
5. Bank nations : Represent relation between each bank with each country (for example how much veto power each country has in each bank etc)
6. Com banks : (not being used in current state of application) Represent relation between Companies and banks - Was a fallback  
7. Com mat : represent relation between Company and Materials. So as to which company owns how much of which material and stuff
8. Com relations : (not currently used) was intended to store the transactions between the companies. This is now done by `Prod transs`
9. Loan Trans : Stores loan transactions (bank-company)
10. Prod req : maintains history of the production request
11. Prod trans : maintains a history of product transaction
12. Transferss : I don't remember why I had made this :P

```All of the above things can be used to view history or undo and manually do a transaction in case of urgent need```

To start using the application:
1. Create a super user
  1. To set subsidy, factor of production and capacity of each production house: Goto mysite/netIITD/views.py. Search for the quantities and change the values in front to set those.
1. Login to admin panel and add materials, banks, nations, comapnies
3. go to `serverip:8000/net/relate`
4. go to `serverip:8000/net/showall`
5. Here onwards ame is very intuitive
6. go to `serverip:8000/net/reset` to reset everything back to intial values.

Note: The urls may be different with a prefix added after `serverip:portno` if a production server is configured in such a way.


## Load/Store data from the database

 Store: ```python3 manage.py dumpdata > db.json``` ; 
 Load: ```python3 manage.py loaddata db.json```


## Contributions:

Encouraged to take this further from here. Do let me know if you want some other help. I will respond, not immediately, but definitely :p

##License:
MIT :D
