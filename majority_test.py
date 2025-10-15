
"""
Tenzin Choeni
tenzin.choeni60@myhunter.cuny.edu
October 15
makes a true or false
"""



def majority3(in1, in2, in3):
    """
    Returns True if at least two of the three inputs are True (or 1).
    """
    return (in1 and in2) or (in1 and in3) or (in2 and in3)

def test_majority3():
    print("All False (0,0,0):", majority3(0, 0, 0))   
    print("All True  (1,1,1):", majority3(1, 1, 1))  

   
    print("Inputs (1,1,0):", majority3(1, 1, 0))      
    print("Inputs (1,0,1):", majority3(1, 0, 1))    
    print("Inputs (0,1,1):", majority3(0, 1, 1))      


    print("Inputs (1,0,0):", majority3(1, 0, 0))     
    print("Inputs (0,1,0):", majority3(0, 1, 0))    
    print("Inputs (0,0,1):", majority3(0, 0, 1))     


test_majority3()
