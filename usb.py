import subprocess

out = subprocess.check_output('wmic logicaldisk get DriveType, caption', shell=True)
flag=True
for drive in str(out).strip().split('\\r\\r\\n'):
    if '2' in drive:
        drive_letter = drive.split(':')[0]
        drive_type = drive.split(':')[1].strip()
        if drive_type == '2':
            flag=False
            print('USB connected')
            break
            
if flag:
    print('USB not connected')
