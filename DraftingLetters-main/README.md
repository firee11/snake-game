# Drafting Emails Project

This project is designed to help students learn about file systems and relative file paths in Python. The task involves reading data from text files, manipulating strings, and writing the output to new text files.
Project Structure

The project has the following directory structure:

```
.
├── Contacts
│   └── names.txt
├── Email
│   └── draft.txt
└── Send
```

- `Contacts`: This directory contains a file called `names.txt` which lists the names of the contacts to whom emails need to be sent.
- `Email`: This directory contains a file called `draft.txt` which serves as a template for the emails to be sent.
- `Send`: This directory will contain the final output of the project, i.e., the individual email drafts for each contact.

## Instructions

1. Read the names from the `names.txt` file located in the `Contacts` directory. Each line in the file contains a single name.

2. For each name, create an individual email using the `draft.txt `file located in the `Email` directory. The `draft.txt` file contains the text of the email with a placeholder, `[name]`, which should be replaced with the actual name.

3. Save each personalized email in the `Send` directory. The file should be named `Letter_for_<name>.txt`, where `<name>` is the name of the contact.

## Tips

Remember that Python strings are immutable, which means you need to assign the result of the `replace()` function to a new variable.
Be mindful of the case when replacing text. The `replace()` function is case-sensitive.
Make sure to use relative file paths when opening files. This makes your program more portable and easier to run on different machines.

- Hint 1 (Reading lines in a file): https://www.w3schools.com/python/ref_file_readlines.asp
- Hint 2 (Replace a string with another string): https://www.w3schools.com/python/ref_string_replace.asp
- Hint 3 (remove whitespaces): https://www.w3schools.com/python/ref_string_strip.asp
