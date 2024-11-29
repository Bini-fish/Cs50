import json
import sys
import re
from datetime import datetime
import requests
from tabulate import tabulate

NOTION_API_KEY = "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"
DATABASE_ID = "11ccdbea2113807ba68df5e7b037d446"
headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def main():
    print(f"1. View\n2. Add Client\n3. Edit Client\n4. Remove Client")
    try:
        option = int(input("Choose one of the options (1-4): "))
        if option not in range(1,5):
            sys.exit("Invalid input")
        else:
            menu(option)
    except ValueError:
        sys.exit("Invalid input")

def valid_date(date):
    format = "%Y-%m-%d"
    valid = bool(datetime.strptime(date, format))
    if valid:
        pass
    else:
        sys.exit("Invalid date format")
def is_name(name):
    if name.replace(" ", "").isalpha():
        pass
    else:
        sys.exit("Invalid name")
def is_phone_num(phone_num):
    pattern = r"^(\+2519|09)([0-9]{8})$"
    if re.search(pattern, phone_num):
        pass
    else:
        sys.exit("Invalid phone number")
def is_url(url):
    pattern = r"^(https?://)?(www\.)?(instagram\.com)/(.+)$"
    if re.search(pattern, url):
        pass
    else:
        sys.exit("Invalid url")

def menu(option: int):
    if option == 1:
        clients = get_client()
        print(format_client(clients))
    elif option == 2:
        client_name = input(f"1. Client's Name: \n")
        is_name(client_name)
        contact_info = input(f"2. Contact Info: \n")
        is_phone_num(contact_info)
        appointment_date = input(f"3. Appointment: (YYYY-MM-DD)\n")
        valid_date(appointment_date)
        completed = input(f"is the project completed? (yes/no)")
        if completed == "yes":
            url = input(f"4. URL: \n")
            is_url(url)
            published_date = input(f"5. Completed Date: (YYYY-MM-DD)\n")
            valid_date(published_date)
            data = {
        "Completed": {
                    "checkbox": True
                },
                "Contact Info": {
                    "phone_number": contact_info
                },
                "Photo Shoot Appointment": {
                    "date": {
                        "start": appointment_date,
                        "end": None
                    }
                },
                "URL": {
                    "url": url
                },
                "Date Published": {
                    "date": {
                        "start": published_date,
                        "end": None
                    }
                },
                "Client's Name": {
                    "title": [
                        {
                            "text": {
                                "content": client_name,
                            },
                            }
                    ]
                }
        }
            add_client(data)
        else:
            data = {
        "Completed": {
                    "checkbox": False
                },
                "Contact Info": {
                    "phone_number": contact_info
                },
                "Photo Shoot Appointment": {
                    "date": {
                        "start": appointment_date,
                        "end": None
                    }
                },
                "Client's Name": {
                    "title": [
                        {
                            "text": {
                                "content": client_name,
                            },
                            }
                    ]
                }
            }

            add_client(data)
    elif option == 3:
        edit_client()
    elif option == 4:
        client = get_client()
        remove_client(client)
    else:
        sys.exit("Invalid input")
def get_client():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    payload = {"page_size": 100}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        results = data["results"]
        # if you want to see what the json files looks like for the request uncomment the code below.
        '''
        with open('db.json', 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        '''
        return results
    except requests.exceptions.RequestException as err:
        sys.exit(f"An error occurred while fetching clients: {err}")
def add_client(data: dict):
    url = "https://api.notion.com/v1/pages"
    payload = {"parent":{"database_id": DATABASE_ID}, "properties": data}
    result = requests.post(url, headers=headers, json=payload)
    if result.status_code == 200:
        sys.exit("Successfully Added a Client")
        return result
    else:
        sys.exit("Unable to Add a Client")
def format_client(clients):
    final_table = {"Name": [], "Contact Info":[],"Appointement":[],"Completed":[],"Completed Date":[],"URL":[]}
    for client in clients:
        client_id = client["id"]
        prop = client["properties"]
        # checking if there's a client present
        if prop["Client's Name"]["title"] != []:
            client_name = prop["Client's Name"]["title"][0]["text"]["content"]
            completed = prop["Completed"]["checkbox"]
            contact_info = prop["Contact Info"]["phone_number"]
            url = prop["URL"]["url"]
            published_date = prop["Date Published"]["date"]
        # checking weather the required parameters appointment_date, published_date are present.
            if prop["Photo Shoot Appointment"]["date"] is not None:
                appointment_date = prop["Photo Shoot Appointment"]["date"]["start"]
            else:
                appointment_date = None
            if prop["Date Published"]["date"] is None:
                published_date = prop["Date Published"]["date"]
            else:
                published_date = prop["Date Published"]["date"]["start"]

            final_table["Name"].append(client_name)
            final_table["Contact Info"].append(contact_info)
            final_table["Appointement"].append(appointment_date)
            final_table["Completed"].append(completed)
            final_table["Completed Date"].append(published_date)
            final_table["URL"].append(url)
        else:
            sys.exit("No client was provided")
    return tabulate(final_table, headers="keys")
def edit_client():
    clients = get_client()
    print(format_client(clients))
    name = input("\nWhich Client do you want to edit? (client name) ")
    for client in clients:
        client_id = client["id"]
        prop = client["properties"]
        if prop["Client's Name"]["title"] != []:
            client_name = prop["Client's Name"]["title"][0]["text"]["content"]
            # checking if the client name in the database and the name the user entered are the same.
            if client_name.lower().strip() == name.lower().strip():
                client_id = client["id"]
                to_edit = int(input("1. Name\n2. Contact Info\n3. Appointement\n4. Completed\n5. Completed Date\n6. URL\nWhat do you want to edit (1-5)? "))
                url = f"https://api.notion.com/v1/pages/{client_id}"
                # storing the specific client to the filtered_client variable
                for item in clients:
                    if item["id"] == client_id:
                        filtered_client = item
                        break
                filtered_client = filtered_client["properties"]
                if to_edit == 1:
                    new_name = input("Enter The New Client's Name: ")
                    is_name(new_name)
                    # updating both the content and plain_text.
                    filtered_client["Client's Name"]["title"][0]["text"]["content"] = new_name
                    filtered_client["Client's Name"]["title"][0]["plain_text"] = new_name
                    filtered_client = {"Client's Name": filtered_client["Client's Name"]}
                elif to_edit == 2:
                    new_contact = input("Enter The New Contact Info: ")
                    is_phone_num(new_contact)
                    filtered_client["Contact Info"]["phone_number"] = new_contact
                    filtered_client = {"Contact Info": filtered_client["Contact Info"]}
                elif to_edit == 3:
                    new_appointement = input("Enter The New Appointement (YYYY-MM-DD): ")
                    valid_date(new_appointement)
                    filtered_client["Photo Shoot Appointment"]["date"]["start"] = new_appointement
                    filtered_client = {"Photo Shoot Appointment": filtered_client["Photo Shoot Appointment"]}
                elif to_edit == 4:
                    new_completed = input("is the task completed? (yes/no): ")
                    if new_completed == 'yes':
                        filtered_client["Completed"]["checkbox"] = True
                        filtered_client = {"Completed": filtered_client["Completed"]}
                    else:
                        filtered_client["Completed"]["checkbox"] = False
                        filtered_client = {"Completed": filtered_client["Completed"]}
                elif to_edit == 5:
                    new_published_date = input("Published Date (YYYY-MM-DD): ")
                    valid_date(new_published_date)
                    if filtered_client["Date Published"]["date"] == None:
                        filtered_client["Date Published"]["date"] = {"start": new_published_date}
                    else:
                        filtered_client["Date Published"]["date"]["start"] = new_published_date
                        filtered_client = {"Date Published": filtered_client["Date Published"]}
                elif to_edit == 6:
                    new_url = input("URL: ")
                    is_url(new_url)
                    filtered_client["URL"]["url"] = new_url
                    filtered_client = {"URL": filtered_client["URL"]}
                else:
                    sys.exit("Enter a valid input (1-6)")
                payload = {"properties": filtered_client}
                edit = requests.patch(url, json=payload, headers=headers)
                if edit.status_code == 200:
                    sys.exit("Successfully Updated")
                else:
                    sys.exit("Unable to make an edit")
            else:
                pass
        else:
            sys.exit(f"Client {name} Doesn't Exist")
def remove_client(clients):
    print(format_client(clients))
    name = input("\nWhich client do you want to Remove? (client name): ")
    is_name(name)
    conform = input(f"Are you sure you want to permanently remove \"{name}\"? (yes/no) ")
    if conform != "yes":
        sys.exit()
    else:
        for client in clients:
            client_id = client["id"]
            prop = client["properties"]
            if prop["Client's Name"]["title"] != []:
                client_name = prop["Client's Name"]["title"][0]["text"]["content"]
                if client_name.lower().strip() == name.lower().strip():
                    client_id = client["id"]
                    url = f"https://api.notion.com/v1/pages/{client_id}"
                    payload={"archived": True}
                    removed = requests.patch(url, json=payload, headers=headers)
                    if removed.status_code == 200:
                        sys.exit("Removed successfully")
                    else:
                        sys.exit("Unable to remove")
                else:
                    pass
            else:
                sys.exit(f"Client {name} Doesn't Exist")

if __name__ == "__main__":
    main()
