Design an algorithm using pseudocode and flowchart that will read student information (Name, Gender, Age). Your program is to continue processing until a sentinel -1 is entered. At the end of the program, total number of students entered with gender breakdown will be displayed.
```
Sample input-output:
Enter ‘-1’ to stop or any number to continue
1
Enter student information
Name: David
Gender (M for Male, F for Female): M
Age: 19
Enter ‘-1’ to stop or any number to continue
1
Enter student information
Name: Mary
Gender (M for Male, F for Female): F
Age: 23
Enter ‘-1’ to stop or any number to continue
-1
Number of students entered: 2
Gender breakdown: 1 Male, 1 Female
```

```psuedocode
START
  male = 0
  female = 0
  student = 0

  PRINT "Enter ‘-1’ to stop or any number to continue"
  READ choice

  DOWHILE choice != -1
    PRINT "Enter student information"
    PRINT "Name: "
    READ name
    PRINT "Gender (M for Male, F for Female): "
    READ gender
    PRINT "Age: "
    READ age

    IF gender == "M"
      male ++
    ELSEIF gender == "F"
      female ++
    ELSE 
      PRINT "Wrong Input"
      BREAK
    ENDIF

    student++
    PRINT "Enter ‘-1’ to stop or any number to continue"
    READ choice
  ENDDO

  PRINT "Number of students entered:", student
  PRINT "Gender breakdown:", male, "Male", female, "Female"
END
```

![flowchart2](./flowchart2.svg)