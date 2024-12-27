questions = [
    ["What is the square root of 144?", "10", "12", "14", "16", 2],
    ["Which element has the chemical symbol 'O'?", "Oxygen", "Gold", "Iron", "Silver", 1],
    ["What is the largest ocean on Earth?", "Indian", "Atlantic", "Arctic", "Pacific", 4],
    ["Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "J.K. Rowling", "Mark Twain", 2],
    ["Which country is known as the Land of the Rising Sun?", "China", "Japan", "Thailand", "South Korea", 2],
    ["Who developed the theory of general relativity?", "Isaac Newton", "Galileo Galilei", "Albert Einstein", "Niels Bohr", 3],
    ["What is the longest river in the world?", "Amazon", "Nile", "Yangtze", "Mississippi", 2],
    ["What is the chemical formula of table salt?", "H2O", "NaCl", "CO2", "KCl", 2],
    ["What year did the Titanic sink?", "1912", "1913", "1911", "1914", 1],
    ["What is the capital of Iceland?", "Helsinki", "Oslo", "Reykjavik", "Stockholm", 3],
    ["Who deciphered the Rosetta Stone?", "Jean-François Champollion", "Thomas Young", "Howard Carter", "Napoleon Bonaparte", 1],
    ["What is the smallest country in the world by land area?", "Monaco", "Vatican City", "San Marino", "Liechtenstein", 2],
    ["Which mathematical conjecture remained unsolved for over 350 years until 1994?", "Goldbach's Conjecture", "Riemann Hypothesis", "Fermat's Last Theorem", "Collatz Conjecture", 3],
    ["What is the rarest blood type?", "A-", "B-", "AB-", "O-", 3],
    ["Who is credited with inventing the first mechanical computer?", "Charles Babbage", "Alan Turing", "John von Neumann", "Ada Lovelace", 1]

]
Money = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

for i, question in enumerate(questions):
    Correct_answer = question[-1]

    print(f"\nQuestion for RS {Money[i]}")


    print(question[0])
    print(f"1.{question[1]}               2.{question[2] }")
    print(f"3.{question[3] }              4.{question[4]} ")
    
    Answer = input("\nEnter correct answer(1-4)\nEnter 'e' for Exit: ")

    while Answer not in ["e","1","2","3","4"]:
        print("Enter correct choices")
        Answer = input("\nEnter correct answer(1-4)\nEnter 'e' for Exit: ")


    if Answer == "e":
        print(f"You won RS.{Money[i-1]}")
        break
    
    if int(Answer) == Correct_answer:
        print(f"Correct Answer! You have won RS {Money[i]}")
        


    else:

        if Money[i] <  10000:

            print("To won minimum prize you have to reach Qn 6 ")
            break


        elif  Money[i] < 320000 and Money[i] > 10000:
            print("You won RS 10,000")
            break

        elif Money[i] >= 320000 and Money[i] < 10000000:
            print("You won RS 320,000")
            break

        else:
            print("You won 10000000")
            break


print("Thank you for your time.")



        


        


            


        

        



    



    


            

        




    
