#!/bin/bash

# Define the password
PASSWORD="automation"

# Prompt the user for the password
read -sp "Enter the password to edit main.py: " input_password
echo

# Check if the entered password matches
if [ "$input_password" == "$PASSWORD" ]; then
    # If the password is correct, open the file with the editor
    nano main.py
else
    # If the password is incorrect, print an error message
    echo "Incorrect password. Access denied."
    exit 1
fi

