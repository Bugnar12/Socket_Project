# Sockets Project

:arrow_right: Created TCP socket server and client for the Computer Networks class.

:arrow_right: The server is written in Python, while the client is multi-language(Python and PHP).

:arrow_right: Concurrent approach using processes : server can wait for multiple clients to connect.

:arrow_right: Clients create 3 arrays (sorted, random, reverse sorted), which will be given to the server when the connection is established.

:arrow_right: Server prints when a client connects and it uses 3 sorting algorithms(Bubble, Merge, Recursive Selection) to count the steps made by each algorithm (with the data sent by the client).

:arrow_right: Afterwards, it returns to the client the number of steps of all sorting methods for each array, thus observing exactly how many steps each algorithm makes in Best Case, Average Case, Worst Case.

:arrow_right: The client does a detailed pretty print with all the processed information and its connection to the server stops.

