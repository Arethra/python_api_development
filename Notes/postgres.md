# Lil notes

### SQL
Tables - used to represent each part - subject, event - for an application  
Columns - attributes/fields of the subject or event  
Rows - records/entries into the table  

#### Data Types in PostgreSQL
| Data Type| Postgres                | Python     |  
|----------|-------------------------|------------|  
| Numeric  | Int, decimal, precision | Int, float |  
| Text     | Varchar, text           | string     |  
| Bool     | boolean                 | boolean    |   
| Sequence | array                   | list       |  

Primary Key - a column or et of columns that uniquely identify each row on a table.

#### Constraints
- `UNIQUE` constraint - applied to ensure that each entry in a field(column) is unique i.e., no duplicates.  
- `NULL` constraint - applied to ensure that the column is never blank on any record(row).  

