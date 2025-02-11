import streamlit as st
import requests

# API configuration
API_KEY = "CS2iq3kE5NTmtA97BjhkmprNEya6EuQH"
API_ENDPOINT = "https://api.mistral.ai/v1/chat/completions"

# Static long-context document (replace with your actual content)
static_context = """

The following guidelines should help you understand how to generate the desired output, using the given input. It is a very long and detailed set of guideline, go through it line by line and make sure to follow all the guidelines…………..

""" 

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

    # Second Subsection: Specify Kanji Character
    st.markdown("---")
    st.header("This Mnemonic is for which Kanji Character")
    kanji_character = st.text_input("Enter the Kanji Character:", placeholder="e.g., 木 (Tree)")

    # Third Subsection: Art Style
    st.markdown("---")
    st.header("Art Style")
    art_type = st.selectbox("Select Art Type:", ["Line Art(Preferred)", "Realistic"])
    art_color = st.selectbox("Select Art Color:", ["Black & White (Preferred)", "Vibrant Color"])
    temperature = st.selectbox("Select Temperature; Temperature represents creativity of the image to be generated (0-Low, 1-Medium, 2-High):", [0, 1, 2])

    # Fourth Subsection: Demographic Details
    st.markdown("---")
    st.header("Demographic Details")
    age_group = st.selectbox("Select Your Age Group:", ["10-14", "15-20", "21-25", "26-30", "30+"])
    gender = st.selectbox("Select Gender:", ["Male", "Female"])
    nationality = st.selectbox("Select Nationality:", ["India", "Japan", "USA", "China"])
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
            f"Kanji Character: {kanji_character}\n"
            f"Art Type: {art_type}\n"
            f"Art Color: {art_color}\n"
            f"Temperature: {temperature}\n"
            f"Age Group: {age_group}\n"
            f"Gender: {gender}\n"
            f"Nationality: {nationality}\n"
            f"Hobbies: {', '.join(hobbies)}\n"
        )
        st.write(call_mistral_api(prompt))

# Run the main function
if __name__ == "__main__":
    main()
