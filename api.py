'''2
_
_
.
'''
from openai import OpenAI
import json

# Set up the OpenAI API client
client = OpenAI(api_key=os.env.APIkey)

def generate_content(prompt):
    try:
        # Make a request to the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates explanatory scripts and extracts keywords."},
                {"role": "user", "content": f"Generate a script explaining the following topic: {prompt}. After the script, provide a list of important words from the topic."}
            ],
            max_tokens=500
        )
        
        # Extract the generated content
        content = response.choices[0].message.content
        
        # Split the content into script and keywords
        parts = content.split("Keywords:", 1)
        script = parts[0].strip()
        keywords = parts[1].strip() if len(parts) > 1 else "No keywords found."
        
        return script, keywords
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None, None

# Example usage
topic = input("Enter a topic: ")
script, keywords = generate_content(topic)

if script and keywords:
    print("\nGenerated Script:")
    print(script)
    print("\nKeywords:")
    print(keywords)