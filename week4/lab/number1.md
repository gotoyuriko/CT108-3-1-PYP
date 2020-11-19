Design an algorithm using pseudocode and flowchart that will prompt for and receive a person’s age in years and months and calculate and display the age in months. If the calculated months figure is more than 500, three asterisks should also appear beside the month figure. Your program is to continue processing until a sentinel ‘n’ is entered.

```
Sample input-output:
Enter ‘n’ to stop or any letter to continue
y
Enter your age in year and month
Year: 50
Month: 3
Your age in month: 603 ***
Enter ‘n’ to stop or any letter to continue
n
```

```pseudocode
BEGIN
  PRINT "Enter `n` to stop or any letter to continue"
  GET choice
  DOWHILE (choice != n) THEN
      PRINT "Enter your age in year and month"
      READ year 
      READ month
      age = month + (year * 12)

      IF month > 500 THEN
          remarks = "***"
      ELSE 
          remarks = " "
      ENDIF

      PRINT "Your age in month:", month, remarks

      PRINT "Enter `n` to stop or any letter to continue"
      READ choice
  ENDDO
END
```

![flowchart1](./flowchart1.svg)