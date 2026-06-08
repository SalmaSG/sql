

# INNER JOIN Queries

### 1. Display employee names with department names


SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;


---

### 2. Show employee name and job title

```sql
SELECT e.first_name, e.last_name, j.job_title
FROM employees e
INNER JOIN jobs j
ON e.job_id = j.job_id;
```

---

### 3. Display employee salary with department name

```sql
SELECT e.first_name, e.salary, d.department_name
FROM employees e
JOIN departments d
ON e.department_id = d.department_id;
```

---

### 4. List employees working in London


SELECT e.first_name, d.department_name, l.city
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
JOIN locations l
ON d.location_id = l.location_id
WHERE l.city = 'London';

---

### 5. Show employees with their manager names


SELECT e.first_name AS Employee,
       m.first_name AS Manager
FROM employees e
JOIN employees m
ON e.manager_id = m.employee_id;


---

### 6. Display departments and their location names


SELECT d.department_name, l.city
FROM departments d
JOIN locations l
ON d.location_id = l.location_id;


---

### 7. Show employee name, department, and city

```sql
SELECT e.first_name,
       d.department_name,
       l.city
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
JOIN locations l
ON d.location_id = l.location_id;
```

---

### 8. Display employees and country names

```sql
SELECT e.first_name,
       c.country_name
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
JOIN locations l
ON d.location_id = l.location_id
JOIN countries c
ON l.country_id = c.country_id;
```

---

### 9. Show all employees with region names

```sql
SELECT e.first_name,
       r.region_name
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
JOIN locations l
ON d.location_id = l.location_id
JOIN countries c
ON l.country_id = c.country_id
JOIN regions r
ON c.region_id = r.region_id;
```

---

### 10. Display employee and previous job history

```sql
SELECT e.first_name,
       jh.start_date,
       jh.end_date,
       j.job_title
FROM employees e
JOIN job_history jh
ON e.employee_id = jh.employee_id
JOIN jobs j
ON jh.job_id = j.job_id;
```

---

# LEFT JOIN Queries

### 11. Show all employees and department names


SELECT e.first_name,
       d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;


---

### 12. Display all departments even without employees

```sql
SELECT d.department_name,
       e.first_name
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id;
```

---

### 13. Show employees with or without managers

```sql
SELECT e.first_name AS Employee,
       m.first_name AS Manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.employee_id;
```

---

### 14. List all locations with department names

```sql
SELECT l.city,
       d.department_name
FROM locations l
LEFT JOIN departments d
ON l.location_id = d.location_id;
```

---

### 15. Display countries and locations

```sql
SELECT c.country_name,
       l.city
FROM countries c
LEFT JOIN locations l
ON c.country_id = l.country_id;
```

---

# RIGHT JOIN Queries

### 16. Show all departments and employees

```sql
SELECT e.first_name,
       d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;
```

---

### 17. Display all jobs and employees

```sql
SELECT e.first_name,
       j.job_title
FROM employees e
RIGHT JOIN jobs j
ON e.job_id = j.job_id;
```

---

# SELF JOIN Queries

### 18. Show employee-manager hierarchy

```sql
SELECT e.first_name AS Employee,
       m.first_name AS Manager
FROM employees e
JOIN employees m
ON e.manager_id = m.employee_id;
```

---

### 19. Find coworkers in same department

```sql
SELECT e1.first_name AS Employee1,
       e2.first_name AS Employee2
FROM employees e1
JOIN employees e2
ON e1.department_id = e2.department_id
AND e1.employee_id <> e2.employee_id;
```

---

# MULTIPLE JOIN Queries

### 20. Employee, department, job, and city

```sql
SELECT e.first_name,
       d.department_name,
       j.job_title,
       l.city
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
JOIN jobs j
ON e.job_id = j.job_id
JOIN locations l
ON d.location_id = l.location_id;
```

---

### 21. Employees working in Asia region

```sql
SELECT e.first_name,
       r.region_name
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
JOIN locations l
ON d.location_id = l.location_id
JOIN countries c
ON l.country_id = c.country_id
JOIN regions r
ON c.region_id = r.region_id
WHERE r.region_name = 'Asia';
```

---

### 22. Count employees in each department

```sql
SELECT d.department_name,
       COUNT(e.employee_id) AS TotalEmployees
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;
```

---

### 23. Average salary by department

```sql
SELECT d.department_name,
       AVG(e.salary) AS AvgSalary
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name;
```

---

### 24. Highest salary in each department

```sql
SELECT d.department_name,
       MAX(e.salary) AS HighestSalary
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name;
```

---

### 25. Employees hired after manager

```sql
SELECT e.first_name AS Employee,
       m.first_name AS Manager
FROM employees e
JOIN employees m
ON e.manager_id = m.employee_id
WHERE e.hire_date > m.hire_date;
```

---

# ADVANCED JOIN Queries

### 26. Employees who changed jobs

```sql
SELECT e.first_name,
       COUNT(jh.job_id) AS TotalJobs
FROM employees e
JOIN job_history jh
ON e.employee_id = jh.employee_id
GROUP BY e.first_name;
```

---

### 27. Department with maximum employees

```sql
SELECT d.department_name,
       COUNT(e.employee_id) AS TotalEmployees
FROM departments d
JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY TotalEmployees DESC
LIMIT 1;
```

---

### 28. Show employees earning more than department average

```sql
SELECT e.first_name,
       e.salary,
       d.department_name
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
WHERE e.salary >
(
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = e.department_id
);
```

---

### 29. Display employees and department manager

```sql
SELECT e.first_name AS Employee,
       m.first_name AS DepartmentManager
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
JOIN employees m
ON d.manager_id = m.employee_id;
```

---

### 30. Find departments located in specific country

```sql
SELECT d.department_name,
       c.country_name
FROM departments d
JOIN locations l
ON d.location_id = l.location_id
JOIN countries c
ON l.country_id = c.country_id
WHERE c.country_name = 'United States of America';
```

---

## Types of JOINs Covered

* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* SELF JOIN
* MULTIPLE JOIN
* JOIN with GROUP BY
* JOIN with Subquery
* Aggregate JOIN Queries
