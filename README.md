# CodeNex-RECRUITMENT-TASK
The Given Task Was To Make A Student Grade Calculator.
The Working Of The Code:
1) First was to make a function which would take in the average of the marks of the subjects and return the Grade accoring to the average marks.
2) Then the second function helps eliminate any random/wrong values that the user has inputted ( anything else than marks from range 0 - 100 ). This function works by the concept of while loop, try - except and if else statements. " while True: " ensure the loop keeps on running where as the "return score" is the only way to escape the loop. "excpet ValueError: " make sure that the code doesnt crash when any string/char etc are being inputted by the user when recieving the marks.
3) The main function calls the get_mark function by sending the name of the subjects into the get_mark function. It also does the calculation of total, average and calls the marks function. Finally It prints out the values and the ends the main function by calling it "main()".
