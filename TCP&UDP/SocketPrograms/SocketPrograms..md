
# Computer Networks Lab – Socket Programming

This repository contains Python programs implemented as part of the Computer Networks Laboratory.

## Topics Covered

- TCP Client–Server Communication
- UDP Client–Server Communication
- Multi-User Chat Server
- Concurrent Servers using Multithreading
- Time and Date Servers
- Concurrent File Server
- TCP Matrix Processing
- UDP String Processing
- TCP Calculator Server
- Static Routing
- Dynamic Routing

---

## TCP Client–Server Programs

**Q1. Sum of Main Diagonal Elements**

The client generates an N × N matrix with random numbers in the range [1,50] and sends it to the server. The server calculates the sum of the main diagonal elements and sends the result back.

**Q2. Palindrome Checking**

The client sends a string to the server. The server checks whether the string is a palindrome and returns the result.

**Q3. Fibonacci Series**

The client sends an integer N. The server generates the first N Fibonacci numbers and sends them back.

**Q4. Count Vowels, Consonants, Digits and Spaces**

The client sends a sentence. The server counts vowels, consonants, digits and spaces and returns the counts.

**Q5. Symmetric Matrix Checking**

The client generates an N × N matrix with random numbers in the range [1,50]. The server checks whether the matrix is symmetric.

**Q6. Largest, Smallest and Average**

The client sends a list of integers. The server calculates the largest, smallest and average values.

---

## UDP Client–Server Programs

**Q7. Abbreviation Translator**

The client sends a sentence containing abbreviations such as u, ur, pls, thx, bcz and msg. The server replaces them with their formal English equivalents.

**Q8. Count Words and Characters**

The client sends a sentence. The server counts the number of words and characters.

**Q9. Prime or Composite**

The client sends an integer. The server determines whether the number is prime or composite.

**Q10. Celsius to Fahrenheit and Kelvin**

The client sends a temperature in Celsius. The server converts it into Fahrenheit and Kelvin.

**Q11. String Conversion**

The client sends a string. The server returns its uppercase, lowercase and reverse forms.

---

## Multi-User / Concurrent Server Programs

**Q12. Multi-User Chat Server using TCP**

Implement a TCP chat server that allows multiple clients to connect simultaneously. Each client provides a username, and the server displays the username along with every received message.

**Q13. Concurrent Number Server using TCP**

Implement a concurrent TCP server that accepts multiple clients. Each client sends an integer, and the server returns whether it is even or odd.

---

## Time Server Programs

**Q14. Concurrent Time Server using UDP**

The client sends a time request to the server. The server returns its current system date and time.

**Q15. UDP Date Server**

The client sends a request. The server returns the current date, day and time.

---

## Concurrent File Server Programs

**Q18. Concurrent File Server using TCP**

The client sends a filename to the server. If the file exists, the server sends its contents and file size. Otherwise, it sends an error message.

---

## TCP Matrix Processing

**Q19. Maximum Element in Each Row**

The client generates an N × N matrix with random values in the range [1,50]. The server finds the maximum element in each row and returns the resulting list.

**Q20. Matrix Classification**

The client sends a square matrix. The server determines whether it is diagonal, upper triangular, lower triangular or neither.

---

## UDP String Processing

**Q21. UDP Abbreviation Translator**

The client sends a sentence containing abbreviations such as tbh, ig, tbf, atm, irl, lol, asap, omg, ttyl, idk and nvm. The server replaces recognized abbreviations with their formal English meanings.

---

## TCP Concurrent Calculator

**Q22. Concurrent Calculator Server using TCP**

Implement a concurrent TCP calculator server. The client sends two numbers and an arithmetic operator (+, -, *, /). The server performs the operation and returns the result.

---

## UDP Reverse Server

**Q23. Reverse String and Palindrome Checking**

The client sends a string using UDP. The server reverses the string and checks whether the original string is a palindrome. Both results are returned to the client.

---



## Technologies Used

- Python
- Socket Programming
- TCP and UDP Protocols
- Multithreading


## How to Run

1. Clone the repository.
2. Open the project folder in VS Code.
3. Open two terminals.
4. Run the server program first:

   `python server.py`

5. Run the client program in another terminal:

   `python client.py`

## Purpose

To understand computer networking concepts through practical implementation of socket programming, client-server communication and multithreading.
