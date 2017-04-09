program binary_to_text
  implicit none
  INTEGER(2) :: input_array(1000000)
  INTEGER :: stat                    !Error message when opening files
  INTEGER :: unit                    !Dummy variable for opening files
  
  unit = 5 !read from stdin
  OPEN (UNIT=unit, STATUS="old", ACTION="read", IOSTAT=stat, FORM="binary") 
  IF (stat .NE. 0) THEN 
     PRINT *, "ERROR: reading input data..."
  ELSE
     READ (unit, END=8) input_array
8    CONTINUE     
  END IF
  PRINT *, input_array
end program binary_to_text
