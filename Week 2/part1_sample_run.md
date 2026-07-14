# Part 1 — Sample Test Runs

## Test 1: Score boundary 90 and correct login

```text
Enter score between 0 and 100: 90
Grade: A

Enter username: student
Enter password: python123
Login successful
```

## Test 2: Score boundary 89 and wrong password

```text
Enter score between 0 and 100: 89
Grade: B

Enter username: student
Enter password: wrongpass
Login failed. Username or password is incorrect.
```

## Test 3: Invalid score

```text
Enter score between 0 and 100: 120
Invalid score. Please enter a score between 0 and 100.

Enter username: student
Enter password: python123
Login successful
```

## Boundary values tested

- 90 gives A
- 89 gives B
- 80 gives B
- 79 gives C
- 70 gives C
- 69 gives D
- 60 gives D
- 59 gives F
- -5 gives invalid score
- 120 gives invalid score
