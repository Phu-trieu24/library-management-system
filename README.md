# library-management-system
This is a Library Management System implemented using Python and Tkinter for the graphical user interface (GUI). The system allows users to perform various simple tasks such as adding books, adding members, lending books to members, and viewing statistics.
**Features**
- Add Book
Allows users to add a new book to the library database.
Users can enter details such as book name, author, page count, and language.
Validates input fields to ensure none of them are empty.
Displays success or error messages upon adding a book.

- Add Member
Enables users to add a new member to the library database.
Requires inputs such as member name, phone number, and email address.
Validates input fields to ensure none of them are empty.
Shows success or error messages upon adding a member.

- Lend Book
Facilitates the process of lending a book to a library member.
Allows users to select a book from available books and a member from the existing members.
Updates the database to reflect the borrowed book and changes the book status to 'Not Available'.
Validates input fields to ensure none of them are empty.
Displays success or error messages upon lending a book.

- View Books and Statistics, Search following given filters.
Displays a list of all books available in the library.
Provides options to filter books by all, in stock, or borrowed.
Shows statistics such as the total number of books, total members, and the number of books currently borrowed.
Updates statistics dynamically when changes occur in the database.
