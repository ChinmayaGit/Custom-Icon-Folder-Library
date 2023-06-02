import os
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import imghdr

# Ask for the root directory path
root_directory = input("Enter the root directory path: ")

max_attempts = 5

# Iterate over folders in the root directory
for folder_name in os.listdir(root_directory):
    folder_path = os.path.join(root_directory, folder_name)
    if os.path.isdir(folder_path):
        print("Processing folder:", folder_name)

        # Perform a Google search for the folder name
        query = folder_name + " image"
        search_results = search(query, num_results=max_attempts)

        attempts = 1

        for search_result in search_results:
            print("Downloading image from:", search_result)

            # Send a request to the URL and parse the HTML
            response = requests.get(search_result)
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the first image in the HTML and extract the source URL
            image_element = soup.find("img")
            if image_element and "src" in image_element.attrs:
                image_url = image_element["src"]

                # Check if the image URL is downloadable
                response = requests.get(image_url, stream=True)
                content_type = response.headers.get("content-type")
                if "image" in content_type:
                    # Validate image format using imghdr
                    image_data = response.content
                    image_format = imghdr.what(None, h=image_data)
                    if image_format and image_format.lower() in ["jpg", "jpeg", "png", "webp"]:
                        # Download the image
                        image_filename = folder_name + "." + image_format.lower()
                        image_filepath = os.path.join(folder_path, image_filename)
                        with open(image_filepath, "wb") as file:
                            file.write(image_data)
                        print("Image downloaded successfully:", image_filepath)
                        break
                    else:
                        print("Invalid or unsupported image format.")
                else:
                    print("URL does not point to a downloadable image.")
            else:
                print("No image found.")

            attempts += 1

        if attempts > max_attempts:
            print("Exceeded maximum number of search attempts.")

        print("---------------------")
