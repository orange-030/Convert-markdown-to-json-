import json
import os


def parse_markdown_to_json(md_content):
    # Split the markdown content into question and answer parts
    parts = md_content.split("\nAnswer:")
    question = parts[0].replace("Question:", "").strip()
    answer = parts[1].strip()

    # Return the JSON representation of the question and answer
    return {"content": question, "summary": answer}


def convert_md_to_json(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r', encoding='utf-8') as md_file:
                md_content = md_file.read()

                # Parse the markdown content and convert it to JSON
                json_obj = parse_markdown_to_json(md_content)

                # Construct the new file name and path
                json_filename = filename.replace('.md', '.json')
                json_path = os.path.join(folder_path, json_filename)

                # Save the JSON file
                with open(json_path, 'w', encoding='utf-8') as json_file:
                    json.dump(json_obj, json_file, ensure_ascii=False, indent=4)


# Replace with the actual path to your markdown folder
folder_path = 'path/to/your/markdown/folder'
convert_md_to_json(folder_path)

