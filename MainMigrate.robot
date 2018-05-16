*** Settings ***
Documentation    Data Migration and Validation from Postgresql to MongoDB
Resource   MigrateSupport.robot

*** Test Cases ***
Migrate data 
    Migrate data from PostgreSQL with username as "postgres" and password as "balaji1212"
    
# Migate from below mentioned database
    # Migrate data from specific "dbname"   
    
# Data injection into source database
    # Insert the data from excel sheet to Postgres Database into the table "superstore" from "F:\\Mongo\\test.xlsx"