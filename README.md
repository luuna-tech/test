You need to create a django project to manage admins of our admin panel.

The objective of the project is to provide the users a means to use the same platform in a restricted manner.
Only users with a permission to modify or view data will be able to modify or view it.

1. You need to creat 2 db tables. Use mysql/mariadb:
```
  i. Users table: It will contain all the users
  ii. Addresses table: It will contain addresses of users
```

2. You need to create 3 different users:
```
  i. Admin user: He is going to have all the accesses to CRUD both the tables 
 ii. Staff user: He can view both user and adresses views but can only CRUD addresses.
iii. Customer service user: He can view just the addresses table, but cannot do anything else.
```

PS: There is no need to beautify the project. It should be simple and functional.
