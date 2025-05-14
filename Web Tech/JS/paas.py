import subprocess

# Get metadata about all saved Wi-Fi profiles
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

# Decode metadata and split into lines
data = meta_data.decode('utf-8', errors="backslashreplace").split('\n')

# Extract Wi-Fi profile names
profiles = []
for line in data:
    if "All User Profile" in line:
        # Extract the profile name after the colon
        profile_name = line.split(":")[1].strip()
        profiles.append(profile_name)

# Print table header
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("----------------------------------------------")

# For each profile, extract the password
for profile in profiles:
    try:
        # Run command to get Wi-Fi profile details with key
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
        results = results.decode('utf-8', errors="backslashreplace").split('\n')

        # Look for the line containing "Key Content"
        password = ""
        for line in results:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break

        # Print Wi-Fi name and password
        print("{:<30}| {:<}".format(profile, password))

    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(profile, "Error retrieving password"))
