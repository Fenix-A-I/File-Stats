'''
Author: Alexandr Iapara
Description: Program shows information about the file contents and prints them.
'''

from padding import pad_left, pad_right
import os

def file_contents_info():
    '''
    Prompts the user to enter a filename, validates its existence, and processes the file to compute statistics.

    Args:
        None

    Returns:
        int: Returns 0 if the user exits immediately by entering a blank filename.

    Example:
        file_contents_info()
    '''
    # Prompt user for filename
    file_name = input("\nEnter filename (blank to exit): ")
    if file_name == '':
        print("Exiting program.\n")
        return 0
    # Add .txt extension if not provided
    if '.' not in os.path.basename(file_name):
        file_name += '.txt'
    # Loop until a valid filename is entered or blank to exit
    while not os.path.exists(file_name):
        print("Invalid filename:", file_name)
        file_name = input("\nEnter filename (blank to exit): ")
        if file_name == '':
            return 0
        if '.' not in os.path.basename(file_name):
            file_name += '.txt'
    numbers_file = open(file_name, 'r')
    comments = 0
    count = 0
    total = 0
    # Process each line in the file
    for lines in numbers_file:
        line = lines.strip()
        if not line:
            continue
        # Count comment lines
        if line[0] == '#':
            comments += 1
        else:
            # Convert line to integer and update counters
            try:
                value = int(line)
                count += 1
                total += value
            except ValueError:
                pass
    # Calculate average
    avg = total / count if count > 0 else 0
    label_spacing = 10
    # Print statistics with padding
    print(pad_right("Count:", label_spacing + 1) + str(count))
    print(pad_right("Comments:", label_spacing) + str(comments))
    print(pad_right("Total:", label_spacing) + str(total))
    print(pad_right("Average:", label_spacing - 3) + str(avg))
    numbers_file.close()
    # Repeat for next file
    file_contents_info()

def main():
    file_contents_info()

if __name__ == "__main__":
    main()
