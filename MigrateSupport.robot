*** Settings ***
Library    migrate.py    
Library    Insertdata.py    
*** Variables ***
${temp}    

*** Keywords ***

Migrate data from PostgreSQL with username as "${username}" and password as "${password}"
    Postgresql Db    ${password}      ${username}    

Migrate data from specific "${database}"
    Postgresql Onlydb    ${database}
    
Insert the data from excel sheet to Postgres Database into the table "${table}" from "${path}" 
    Insert Data Into Postgres    ${table}    ${path}
    