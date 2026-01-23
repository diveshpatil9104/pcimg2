import os
import json

# Configuration
ASSETS_DIR = 'assets'
OUTPUT_FILE = 'imagelist.json'
# Add any other extensions you need
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.webp')

def create_image_json():
    # 1. Check if assets folder exists
    if not os.path.exists(ASSETS_DIR):
        print(f"❌ Error: Folder '{ASSETS_DIR}' not found.")
        return

    images = []

    # 2. Loop through files in the assets folder
    print(f"Scanning '{ASSETS_DIR}'...")
    
    try:
        # sorted() ensures the order is consistent every time you run it
        for filename in sorted(os.listdir(ASSETS_DIR)):
            if filename.lower().endswith(VALID_EXTENSIONS):
                images.append(filename)
                print(f"  - Found: {filename}")
    except Exception as e:
        print(f"Error reading directory: {e}")
        return

    # 3. Write the list to a JSON file
    try:
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(images, f, indent=2) # indent makes it readable
        
        print(f"\n✅ Success! Saved {len(images)} images to '{OUTPUT_FILE}'")
        print("You can now fetch this file in your JavaScript.")
        
    except IOError as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    create_image_json()