# Basic SQL QUERIES

## INSERT-ing Database Table (TODOS)

```sql
INSERT INTO todos (title, description, priority, complete) VALUES ('GO To store', 'To pickup eggs', 4 ,False);
INSERT INTO todos (title, description, priority, complete) VALUES ('Haircut', 'Need to get length 1mm', 3 ,False);
INSERT INTO todos (title, description, priority, complete) VALUES ('Feed dog', 'Make sure to use new food brand', 5 ,False);
INSERT INTO todos (title, description, priority, complete) VALUES ('Water plant', 'Inside and outside plants', 4 ,False);
INSERT INTO todos (title, description, priority, complete) VALUES ('Learn something new', 'Learn to program', 5 ,False);
INSERT INTO todos (title, description, priority, complete) VALUES ('Shower', 'You have not showered for few days', 5 ,False);
```

## WITHDRAW DATA [SELECT]
```sql
SELECT * FROM todos;
SELECT title FROM todos;
```

## WHERE
```sql
SELECT * FROM todos WHERE priority = 5;
SELECT * FROM todos WHERE title = 'Feed dog';
SELECT * FROM todos WHERE id = 2;
```

## UPDATE
```sql
UPDATE todos SET complete= True WHERE id=5;
UPDATE todos SET complete=True WHERE title='Learn something new';
```

## DELETE
```sql
DELETE FROM todos WHERE id=5;
DELETE FROM todos WHERE complete=0;
```