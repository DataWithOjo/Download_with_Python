import requests
import zipfile
import os
from io import BytesIO

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

# Create a 'downloads' directory
download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)


def main():
    # Process each URL
    for uri in download_uris:
        print(f"\nProcessing: {uri}")
        try:
            # Download the ZIP file
            response = requests.get(uri)
            response.raise_for_status()

            # Open the ZIP file
            with zipfile.ZipFile(BytesIO(response.content)) as thezip:
                for file_info in thezip.infolist():
                    if file_info.filename.endswith(".csv"):
                        print(f"  Extracting {file_info.filename}...")
                        thezip.extract(file_info, path=download_dir)

            print("  Done.")
        except requests.exceptions.RequestException as e:
            print(f"  Failed to download: {e}")
        except zipfile.BadZipFile as e:
            print(f"  Failed to unzip file from {uri}: {e}")

    print(f"\nAll done. CSV files are in: {download_dir}")


if __name__ == "__main__":
    main()
