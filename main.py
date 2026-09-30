import os
import re
import shutil
import logging
from pathlib import Path

# Setup logging configuration for professional tracking
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def organize_jpg_files(source_dir: str, target_dir: str) -> None:
    """
    Moves all .jpg and .jpeg files from source_dir to target_dir.
    """
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    if not source_path.exists():
        logging.error(f"Source folder does not exist: {source_dir}")
        return

    # Create target folder if it doesn't exist
    target_path.mkdir(parents=True, exist_ok=True)

    moved_count = 0
    for file_path in source_path.glob("*"):
        if file_path.suffix.lower() in [".jpg", ".jpeg"]:
            destination = target_path / file_path.name
            try:
                shutil.move(str(file_path), str(destination))
                moved_count += 1
                logging.info(f"Moved: {file_path.name} -> {target_dir}")
            except Exception as e:
                logging.error(f"Failed to move {file_path.name}: {e}")

    logging.info(f"Task Complete: {moved_count} image(s) moved successfully.")


def extract_emails(input_file: str, output_file: str) -> None:
    """
    Extracts all unique email addresses from a text file and saves them to an output file.
    """
    input_path = Path(input_file)

    if not input_path.is_file():
        logging.error(f"Input file not found: {input_file}")
        return

    # Regex pattern for email extraction
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    try:
        with open(input_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Find all matching emails and remove duplicates using set
        emails = sorted(set(re.findall(email_pattern, content)))

        if not emails:
            logging.warn("No email addresses found in the specified file.")
            return

        with open(output_file, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(f"{email}\n")

        logging.info(f"Successfully extracted {len(emails)} email(s) into '{output_file}'.")

    except Exception as e:
        logging.error(f"Error processing file: {e}")


if __name__ == "__main__":
    print("=" * 50)
    print(" Python Task Automation Suite")
    print("=" * 50)
    print("1. Organize .jpg files into a specific folder")
    print("2. Extract email addresses from a text file")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == "1":
        src = input("Enter source folder path: ").strip()
        dest = input("Enter destination folder path: ").strip()
        organize_jpg_files(src, dest)

    elif choice == "2":
        input_txt = input("Enter input text file path (e.g., sample.txt): ").strip()
        output_txt = input("Enter output file path (e.g., extracted_emails.txt): ").strip()
        extract_emails(input_txt, output_txt)

    else:
        print("Invalid choice. Exiting script.")