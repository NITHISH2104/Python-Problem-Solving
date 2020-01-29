def printPascal(n):  
  
    for line in range(1, n + 1):  
        C = 1; 
        for i in range(1, line + 1):  
            print C,
            C = int(C *(line - i) / i)  
        print("\n");  
    
n = 5;  
printPascal(n); 





'''output


1 

1 1 

1 2 1 

1 3 3 1 

1 4 6 4 1 '''
