Assignment 

Task 1 : 

Considered following assumption and provided the solution accordingly
Assumption: 
1.	Database is on Cloud environment e.g Relational Database Service (Postgress) . As the database is on cloud, we can take advantage of horizontal and vertical scaling very quickly as compared to on-premise infrastructure.
Horizontal Scaling is normally used for read heavy operations. Vertical Scaling can be used to process higher loads.  In this way we can keep the existing pool of computing resource online while adding more to what we already have.
2.	Database is already setup with proper credentials and access.
3.	Tables structures are already created in database.
4.	File is in correct format and there is no need for any cleanup activities and there no duplicates and no filtering are required All records are valid ones. 
5.	File is in uncompressed format. 


Task 2 
We had a similar situation where we had to compare internal and external data for given customer and merge some of the columns.
The first step is to ensure that the Account Name is matching. In order to ensure it is matching there were couple of additional columns used for Country / State / City / Postal Code / Latitude / Longitude


