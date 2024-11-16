from database import MongoDBClient
from utils import generate_content, generate_gif, text_to_speech

if __name__ == "__main__":
    client = MongoDBClient()
    print("Databases:", client.list_databases())

    document = {"name": "John Doe", "age": 30, "city": "New York"}
    inserted_id = client.insert_document("test_db", "test_collection", document)
    print("Inserted Document ID:", inserted_id)

    documents = client.find_documents("test_db", "test_collection", {"name": "John Doe"})
    print("Found Documents:", documents)

    updated_count = client.update_document(
        "test_db", "test_collection", {"name": "John Doe"}, {"age": 31}
    )
    print("Number of Documents Updated:", updated_count)

    deleted_count = client.delete_document("test_db", "test_collection", {"name": "John Doe"})
    print("Number of Documents Deleted:", deleted_count)

    topic = input("Enter a topic: ")
    script, keywords = generate_content(topic)
    text_to_speech(script)

    for idx, keyword in enumerate(keywords):
        keys = [key.strip() for key in keyword.split(",")]

        for key in keys:
            url = generate_gif(key)
            if url is None:
                continue

            response = requests.get(url)
            with open(f"./{idx}_{key}.gif", "wb") as f:
                f.write(response.content)

