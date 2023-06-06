# usb_checker using python subprocess module
#Importing the subprocess module: This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

#Executing the wmic command: The subprocess.check_output() function is used to run the wmic logicaldisk get DriveType, caption command. This command retrieves information about logical disks on the system, including their drive type (1 for a fixed disk, 2 for a removable disk like a USB) and drive caption (drive letter).

#Processing the output: The output from the wmic command is obtained as a byte string. It is then converted to a regular string and processed line by line. The lines are split based on the \\r\\r\\n delimiter, which represents the Windows line ending.

#Checking for USB drives: The code iterates over each line of the output. If a line contains the character '2', it means a removable disk (USB) is connected. In that case, it extracts the drive letter and checks if the drive type is indeed '2' (USB).

#Printing the result: If a USB drive is found, it prints "USB connected." Otherwise, if no USB drives are detected, it prints "USB not connected."

##It's important to note that this code specifically targets Windows systems because it relies on the wmic utility. If you run this code on a non-Windows system, it will likely raise an error or produce unexpected results.
