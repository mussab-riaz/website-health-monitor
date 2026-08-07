import requests
import time
import csv

# Read websites from file
with open("websites.txt", "r") as file:
    websites = file.readlines()

# Create CSV report
with open("reports/health_report.csv", "w", newline="") as report:
    writer = csv.writer(report)

    # CSV Header
    writer.writerow(["Website", "Status", "Status Code", "Response Time"])

    # Loop through each website
    for website in websites:
        website = website.strip()

        # Skip empty lines
        if not website:
            continue

        try:
            # Start timer
            start = time.time()

            # Send HTTP request
            response = requests.get(website, timeout=5)

            # End timer
            end = time.time()

            # Calculate response time
            response_time = end - start

            # Determine website status
            status = "UP ✅" if response.status_code < 500 else "DOWN ❌"
            # Print results
            print("--------------------------------")
            print(f"Website: {website}")
            print(f"Status: {status}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Time: {response_time:.2f} seconds")

            # Save to CSV
            writer.writerow([
                website,
                status,
                response.status_code,
                f"{response_time:.2f}"
            ])

        except requests.exceptions.RequestException as e:
            print("--------------------------------")
            print(f"Website: {website}")
            print("Status: DOWN ❌")
            print(f"Error: {e}")

            # Save failed check to CSV
            writer.writerow([
                website,
                "DOWN ❌",
                "N/A",
                "N/A"
            ])