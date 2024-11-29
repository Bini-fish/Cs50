# Click and Track

## Description

    This is a final project for CS50's Introduction to programming in python course.
    Photography has been my hobby for a long time and I recently started getting requests to take portrait photos of people, and I've made this python program to be able to keep track of the photoshoot appointement dates, and previous clients.
    This program uses the Notion_Api, enabeling the user to manupilate the client's information in a notion database remotely.

## Libraries used

### Built-in modules (python 3.5+)

1. import json
2. import sys
3. import re
4. from datetime import datetime

### User-defined modules (installations)

5. import requests

```bash
pip install requests
```

6.  from tabulate import tabulate

```bash
pip install tabulate
```

# Initial Setup

For the project to work properly you need to have `NOTION_API_KEY = "Your Notion API"` and `DATABASE_ID = "Database ID"`

1. [Setting up database](https://developers.notion.com/docs/working-with-databases)
2. [Setting up NOTION_API_KEY and DATABASE_ID](https://developers.notion.com/docs/create-a-notion-integration)

3. Make sure the names of the rows are as below (`Case-sensitive`):

   ![An image of the header rows](https://ibb.co/5vRwHD7)

   **| Client's Name | Contact Info | Photo Shoot Appointment | Completed | Date Published | URL |**

# How does the program `function`

### main()

![Main function](https://ibb.co/mCMZqCy)

When the `main()` function is excuted it displays the list of options, if the user enters the values (1-5) the program proceeds to the menu function.

### menu(int: option)

![menu](https://ibb.co/DCQtx12)

The `menu(option)` function acts as a bus terminal controling **what function should be excuted next** according to the input.

**e.g.** if the input is `1` format_client() gets excuted.

### get_client()

![get_client](https://ibb.co/thDDj0b)

This function fetchs the data from our `Notion database` and returns a dictionary where we use this dictionary as an input to our format_client() functioin.

### format_client(dict: data)

![format_client](https://ibb.co/Cv14jGR)

This function takes dictionary as an input and uses the `tabulate` library to format our dictionary (matching the rows and columns in our Notion database).

### add_client(dict: data)

![add_client](https://ibb.co/fDqkbxS)

This function checks if our dictionary is in the proper format to be added (posted) to our notion database, then proceeds to add it.

### edit_client()

This function checks weather the **change** we want to make to the database is in the correct format (e.g. phone_number is in number form, name is in letter etc.) and updates the value accordingly.

### remove_client()

![remove_client](https://ibb.co/r7K6Qm8)

This function checks weather the `name of the client` we want to remove is correct (exists), then proceeds to remove it from our database.

# Demo

#### Video Demo: [Video_URL](https://youtu.be/Vxpc-fA8Iro)

when first running the program with `python .\project.py` you'll be prompted to enter one of the following options do you want.

1. view
2. Add Client
3. Edit Client
4. Remove Client

> You enter the number that contains the option, not the name.

## Option 1 (View)

A list of previous clients (in tabular from) will be displayed.

## Option 2 (Add Client)

### Prompt 1

Enter the `client's name`

> numbers and other characters are automatically rejected by the program.

### Prompt 2

Enter the `contact information`

> accepts only ethiotelecom phone_number (starting with +251 or 09 followed by 8 digits).

### Prompt 3

Enter `appointment date`

> The format should be (YYYY-MM-DD).

### Prompt 4

was the photoshoot `completed`

if you answer `no` the program exits and the new appointement will be added to the list.

if you answer `yes` Two more prompts follows.

### Prompt 5

Link of the uploaded picture (`URL`).

> the link should be an instagram link or else the program will reject it.

### Prompt 6

The `date` it was uploaded to instagram.

> the date format should be (YYYY-MM-DD).

if all the inputs are correct the program should exit with the message `"Successfully Added a Client"`

## Option 3 (Edit client)

### Prompt 1

The `client's name` whom you want to edit.

### Prompt 2

Which info do you want to edit.

1. Name
2. Contact Info
3. Appointement
4. Completed
5. Completed Date
6. URL

Then, edit the one you want (following the guidelines outlied in the `Add client` section)

## Option 4 (Remove client)

### Prompt 1

The `client's name` whom you want to remove.
