-- CREATE TABLE Departments (
--     ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     NAME VARCHAR (40)
-- );
--
-- CREATE TABLE Employee (
--     ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     NAME VARCAR (30),
--     ROLE VARCHAR (40),
--     MANAGER_ID INTEGER,
--     DEPARTMENT_ID INTEGER,
--     FOREIGN KEY (DEPARTMENT_ID) REFERENCES Departments(ID)
-- );

-- INSERT INTO Departments (NAME) VALUES ('Management');
-- INSERT INTO Departments (NAME) VALUES ('HRs');
-- INSERT INTO Departments (NAME) VALUES ('Sales');
-- INSERT INTO Departments (NAME) VALUES ('Software Development');
-- INSERT INTO Departments (NAME) VALUES ('Support');
-- INSERT INTO Departments (NAME) VALUES ('RND');
--
-- INSERT INTO Employee (NAME, ROLE, DEPARTMENT_ID)
-- VALUES ('James Smith', 'CEO', 1);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Sarah Goldman', 'CFO', 1, 1);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Wayne Ablet', 'CIO', 1, 1);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Michelle Carey', 'HR Manager', 1, 2);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Chris Matthews', 'Sales Manager', 2, 3);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Andrew Judy', 'Development Manager', 3, 4);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Danielle McLeon', 'Support Manager', 3, 5);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Matthew Swan', 'HR Representative', 4, 2);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Stephanie Richardson', 'Salesperson', 5, 2);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Tony Stark', 'Salesperson', 5, 3);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Jenna Lockett', 'Front-End Developer', 6, 4);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Michael Dunstall', 'Back-End Developer', 6, 4);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Jane Voss', 'Back-End Developer', 6, 4);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID)
-- VALUES ('Anthony Hird', 'Support', 7);
-- INSERT INTO Employee (NAME, ROLE, MANAGER_ID, DEPARTMENT_ID)
-- VALUES ('Natalie Rocca', 'Support', 7, 5);

SELECT Employee.NAME, Employee.ROLE, Departments.NAME FROM Employee
JOIN Departments ON Employee.DEPARTMENT_ID = Departments.ID;

SELECT Employee.NAME FROM Employee WHERE Employee.ID =
(SELECT MANAGER_ID FROM Employee WHERE Employee.NAME = 'Tony Stark');

SELECT Departments.NAME, Employee.NAME
FROM Departments OUTER LEFT JOIN Employee ON Departments.ID = Employee.DEPARTMENT_ID;