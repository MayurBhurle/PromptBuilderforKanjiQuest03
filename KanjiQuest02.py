import streamlit as st
import requests

# API configuration
API_KEY = "CS2iq3kE5NTmtA97BjhkmprNEya6EuQH"
API_ENDPOINT = "https://api.mistral.ai/v1/chat/completions"

# Static long-context document (replace with your actual content)
static_context = """

These instructions guide the creation of prompts for text-to-image generation, based on a given mnemonic corresponding a Kanji character and various user inputs. The goal is to generate personalized images by incorporating both the mnemonic details and user preferences into the prompt. Below are comprehensive steps for constructing the prompt, along with examples for reference.
Guidelines:
Step 1: Identify Keywords/Objects
Extract the core keywords or objects from the given mnemonic. These are the visual elements that will be represented in the generated image. For instance, in a mnemonic for Tree, keywords could include “Tree”, "trunk," "bough," "roots," etc.
Step 2: Build the Prompt in a Structured Manner
Create the prompt by describing, in detail, how each keyword or object from the mnemonic will be visually represented in the image. This should be a step-by-step breakdown of the visual elements.
Step 3: Use a Step-by-Step and a Sequential Format
The prompt should be clearly structured, following a logical sequence. This helps ensure clarity and avoids ambiguity, making the image generation process more effective.
Step 4: Specify the View
After describing the objects, indicate the view of the image (e.g., front view, side view, or top view). Use your judgment for which view is most appropriate—typically, the front view is the most common.
Step 5: Incorporate User Preferences and demographic information
At the end of the prompt, include a line that says, "Following are the user preferences and demographic information; try to personalize the images using the user preferences and demographic information given below:" Then list the user preferences:
Art type: [user input]
Art color: [user input]
Age group: [user input]
Gender: [user input]
Nationality: [user input]
Region: [user input]
Hobbies: [user input]
Step 6: Craft Original Prompts
Do not simply replicate the examples provided. Instead, craft your own prompts by following the above steps, ensuring that the final prompt is unique and tailored to the given mnemonic and user inputs.

Example Input and Output:

Example 1:

Input: 
kanji_character = "Tree"
mnemonic =  
"Here we see a pictograph of a tree, showing the main trunk in the long vertical stroke and the boughs in the long
horizontal stroke. The final two strokes sweep down in both directions to indicate the roots. Although it may look
similar at first sight to the kanji for water (FRAME 137), the order in which it is written is completely different and this
affects its final appearance. [4]

As a primitive, this kanji can mean tree or wood. When the last two strokes are detached from the trunk, we
shall change its meaning to pole, or wooden pole"

Output: Create a graphic of a tree with:
A single, long trunk that extends vertically.
A long, horizontal bough extending from the trunk.
Two roots spreading outward from the base of the trunk in opposite directions.
View = Front view.
Following are the user preferences and demographic information; try to personalize the images using the user preferences and demographic information given below:
Art type: Line art
Art color: Black and white
Age group: 15 to 20
Gender: Female
Nationality: India
Region: North
Hobbies: Anime

"""  # Shortened for brevity

def call_mistral_api(prompt):
    """Calls the Mistral API's chat completions endpoint with the given prompt."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "open-mixtral-8x22b",  # Replace with the desired model ID
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result.get("choices", [])[0].get("message", {}).get("content", "")
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except (IndexError, KeyError) as e:
        return f"Unexpected response format: {e}"

def main():
    """Main function to run the Streamlit app."""
    # Centered Title and Subheader using Markdown + HTML
    st.markdown(
        """
        <h1 style='text-align: center;'>Prompt Builder for Kanji Illustrations</h1>
        <h3 style='text-align: center; font-weight: normal;'>Effortlessly Generate Detailed Prompts for Text-to-Image Generation Using Mnemonics</h3>
        """,
        unsafe_allow_html=True
    )

    # First Subsection: Enter Your Mnemonic
    st.markdown("---")
    st.header("Enter Your Mnemonic")
    st.write("Please copy and paste the entire mnemonic from the *Remembering the Kanji* book or type in your own mnemonic.")
    mnemonic = st.text_area("Enter your mnemonic:", placeholder="e.g., A tree with roots and branches...")

    # Second Subsection: Art Style
    st.markdown("---")
    st.header("Art Style")
    art_type = st.selectbox("Select Art Type:", ["Line Art(Preferred)", "Realistic"])
    art_color = st.selectbox("Select Art Color:", ["Black & White (Preferred)", "Vibrant Color"])

    # Third Subsection: Demographic Details
    st.markdown("---")
    st.header("Demographic Details")
    age_group = st.selectbox("Select Your Age Group:", ["10-14", "15-20", "21-25", "26-30", "30+"])
    gender = st.selectbox("Select Gender:", ["Male", "Female"])
    nationality = st.selectbox("Select Nationality:", ["India", "Japan", "USA", "China"])
    region = st.selectbox("Select Region:", ["North", "South", "East", "West"])
    hobbies = st.multiselect("Select Hobbies:", ["Anime", "Reading Comics", "Gaming", "Music", "Sports", "Cooking", "Other"])

    # Button to Generate Mnemonic
    if st.button("Generate Mnemonic"):
        if not API_KEY or not API_ENDPOINT:
            st.error("API key or endpoint is missing. Please check your .env file.")
            return
        
        # Combine static context and user data into a single plain text prompt
        prompt = (
            f"{static_context}\n\n"
            "User Inputs:\n"
            f"Mnemonic: {mnemonic}\n"
            f"Art Type: {art_type}\n"
            f"Art Color: {art_color}\n"
            f"Age Group: {age_group}\n"
            f"Gender: {gender}\n"
            f"Nationality: {nationality}\n"
            f"Region: {region}\n"
            f"Hobbies: {', '.join(hobbies)}\n"
        )
        st.write(call_mistral_api(prompt))

# Run the main function
if __name__ == "__main__":
    main()
