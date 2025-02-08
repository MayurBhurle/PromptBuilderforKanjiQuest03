import streamlit as st
import requests

# API configuration
API_KEY = "CS2iq3kE5NTmtA97BjhkmprNEya6EuQH"
API_ENDPOINT = "https://api.mistral.ai/v1/chat/completions"

# Static long-context document (replace with your actual content)
static_context = """

The following guidelines should help you understand how to generate the desired output, using the given input. It is a very long and detailed set of guideline, go through it line by line and make sure to follow all the guidelines.
What is your job?
Your job is to create a prompt that the user/student can use later to create a personalized image (using a text to image generator tool). The prompt must be created in such a way that a clear association can be made between the shape of the Kanji character and the image generated using the prompt so that using the image the student can easily remember the meaning of the Kanji character.
What is the input and output: 
Input:
There three different types of inputs
1)	First input is the mnemonic that will be given by the user.
Here Mnemonic is used to make association between the shape of the Kanji character and a real life object or an imaginary scenario. A student uses this mnemonic to make association between the shape of the Kanji character and some real life object/scenario to help him/her remember the meaning of the Japanese Kanji character.                
2)	The second input is the Art style:
Within this input category the user selects whether he/she wants a “line art” or “realistic art” along with the color of the art, that is  “black and white” or “color”.
3)	The third input type is the demographic information of the user such as the age, gender, nationality and the hobbies, so that these inputs can be put into the prompt to generate a personalized image using this prompt in a text to image generator tool.
Output:
Output is a step by step prompt that the user/student can use later to create a personalized image (using a text to image generator tool). The output that is the prompt must meet the following requirements.
1)	Start with the first category of user input that is the “mnemonic”.
2)	It should be a step by step prompt.
3)	Its should be a detailed prompt.
4)	It must contain the keywords or objects from the given mnemonic.
5)	Make sure to not just mention the keywords in the prompt, it is very important that a scenario is mentioned in the prompt that utilizes the keywords and highlights them in the scenario.
6)	Must focus on the adjectives such as “long”, “tall”, “short” etc mentioned in the mnemonic and must use them in the prompt. So if the mnemonic mentions “long roots of a tree” then you must highlight in the prompt that the tree image to be generated must have “really long roots”.
7)	The adjectives mentioned in the mnemonic such as “long”, “tall”, “short” etc needs to slightly exaggerated in the image so that the user can easily correlate the image  and the shape of the kanji that he/she is trying to learn. So if the mnemonic says that the tree has long roots and long horizontal branches then you must slightly ‘exaggerate’’ these adjectives and must mention in the prompt that the tree image to be generated has to have 1) ‘really’ long roots, 2) ‘very’ horizontal branches, 3) those horizontal branches should be ‘really’ long.
8)	Now read the demographic details of the user which are age, gender, nationality and the hobbies, and you must add some element into the prompt using these demographic details so that the image becomes personalized to the user.
9)	Whenever a girl or woman is mentioned in the prompt you must add a line in the prompt that the woman or girl should be dressed in traditional Japanese clothing.
10)	Now  indicate the view of the image in the prompt (e.g., front view, side view, or top view). Use your judgment for which view is most appropriate—typically, the front view is the most common.

11)	Once this step-by-step prompt is generated then mention the second category of input that is the art style that is “line art” or “realistic art” along with the color of the art, that is  “black and white” or “color”.

Example of Input and Output:
 the examples of input and desired outputs are provided under doble strokes ("" )  along with reasoning behind the desired output as well. Please read the reasoning as well so that you understand why I wrote the output like this.
Example 1: 
Input: 
""   
mnemonic =  
"Here we see a pictograph of a tree, showing the main trunk in the long vertical stroke and the boughs/branches in the long horizontal stroke. The final two strokes sweep down in both directions to indicate the roots. Although it may look similar at first sight to the kanji for water (FRAME 137), the order in which it is written is completely different and this
affects its final appearance. 
As a primitive, this kanji can mean tree or wood. When the last two strokes are detached from the trunk, we shall change its meaning to pole, or wooden pole.

Art-style:
Art type: Line art
Art color: Black and white
Demographic Details:
Age group: 15 to 20
Gender: Female
Nationality: India
Hobbies: watching Anime

"" 

Output: 
"" 
Create a graphic of a tree with:
•	A single, really long trunk that extends vertically.
•	A really long and horizontal bough/branch extending from the trunk.
•	Two very long roots spreading outward from the base of the trunk in opposite directions.
•	The user is a female in the age group “15 to 20” so design the elements in the image so that they are more appealing to a female who is “15 to 20” years old.
•	View = Front view.
•	
Following are the user preferences; try to personalize the images using the user preferences given below:
Art type: Line art
Art color: Black and white

"" 
Reasoning behind the output:

"" 
Note that in the line “A really long and horizontal bough/branch extending from the trunk” from the prompt I have used the word ‘really long’ because in the mnemonic as well they have mentioned “the long horizontal stroke” so as per the instructions I have added the word ‘really’, so that image created has a really long branch, with this really long branch it will be easier for the user to correlate the shape of the Kanji character and the image, eventually helping the user to remember the meaning of the Kanji character. Now similarly in another line of the output I have mentioned “The user is a female in the age group “15 to 20” so design the elements in the image so that they are more appealing to a female who is “15 to 20” years old” because as per instrauction the output must add some element into the prompt using these demographic details so that the image becomes personalized to the user.
"" .

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
    #region = st.selectbox("Select Region:", ["North", "South", "East", "West"])
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
            #f"Region: {region}\n"
            f"Hobbies: {', '.join(hobbies)}\n"
        )
        st.write(call_mistral_api(prompt))

# Run the main function
if __name__ == "__main__":
    main()
