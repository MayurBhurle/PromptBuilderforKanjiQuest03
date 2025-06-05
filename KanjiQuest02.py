here I want to make only one Changecanges:

I wan to increase the size of the text in the input boxes, basically all the things that we fill as input and also the out put that we get at least by three points:

here is the code , please give which lines I should change, I dont want tany other changes:

(
import streamlit as st
import requests

# API configuration
API_KEY = "CS2iq3kE5NTmtA97BjhkmprNEya6EuQH"
API_ENDPOINT = "https://api.mistral.ai/v1/chat/completions"

# Static long-context document (replace with your actual content)
static_context = """

Guidelines to write prompt from Mnemonics, with examples:

The following guidelines should help you understand how to generate the desired output, using the given input. It is a very long and detailed set of guidelines, go through it line by line and make sure to follow all the guidelines and explanations.

What is your task ?
Answer:
 <
Your task is to create a prompt that the user/student can use later to create a personalized image (using a text to image generation tool). The prompt must be created in such a way that all the keywords in the given mnemonic (mnemonic is a user input) are clearly mentioned in the prompt , and the prompt should clearly describe the scenario given in the mnemonic. Also, the prompt should be written in such a way that, a clear association can be made between the shape of the Kanji character and the image generated using the prompt so that using the image the student can easily remember the meaning of the Kanji character
>

What is the input and output?
Ans:
Input:
<
There two different types of inputs
1)	First input is the mnemonic that will be given by the user.
A student uses this mnemonic to make an association between the shape of the Kanji character and some real life object/scenario to help him/her remember the meaning of the Japanese Kanji character.                
2)	The second input is the Art style:
Within this input category the user selects whether he/she wants a “line art” or “realistic art”, the color of the art, that is  “black and white” or “color” and the temperature, the temperature indicates creativity. 0 temperature indicates low creativity while 1 and 2 represent medium and high creativity respectively. If the user inputs temperature as 2 then the user expects a very creative image, similarly if the user inputs temperature as 0 that the user does not expect the image to be creative.

>

Output:
<
Output is a step by step prompt that the user/student can use later to create a personalized image (using a text to image generator tool). The prompt must meet the following requirements.
0) Start with the sentence asking the model to wait and take time to think before generating an illustration, then generate the illustration.
1)	Now focus on the first category of user input that is the “mnemonic”.
2)	It should be a detailed step by step prompt, please make sure that the prompt is given in steps.
4)	It must contain the keywords or objects from the given mnemonic.
5)	Make sure to not just mention the keywords in the prompt, it is very important that a scenario is mentioned in the prompt that utilizes the keywords and highlights them in the scenario.
6)	Focus on the adjectives such as “long”, “tall”, “short” etc mentioned in the mnemonic and use them in the prompt. So if the mnemonic mentions “long roots of a tree” then you must highlight in the prompt that the tree image to be generated must have “really long roots”, 
7)	The adjectives mentioned in the mnemonic such as “long”, “tall”, “short” etc needs to slightly exaggerated in the image so that the user can easily correlate the image  and the shape of the kanji that he/she is trying to learn. So if the mnemonic says that the tree has long roots and long horizontal branches then you must slightly ‘exaggerate’ these adjectives and must mention in the prompt that the tree image to be generated has to have 1) ‘really’ long roots, 2) horizontal branches, 3) those horizontal branches should be ‘really’ long.


8)	Once this step-by-step prompt is generated then mention the second category of input that is the art style that is “line art” or “realistic art”, color of the art, that is  “black and white” or “color” and temperature (creativity).

9) There are multiple examples given below explaining how a prompt needs to be generated. In these examples I have also given reasoning, but in the output only focus on the prompt, no need to give reasoning.

10) Safety: Most important, make sure that the images that you generate are age appropriate, as the students or users of images that will be generated using the prompt that you will give, will be under 18 years of age.

>

Example of Input and Output:
 The examples of input and desired outputs are provided with angle brackets( <  >  )  along with reasoning behind the desired output as well. Please read the explanation behind the prompt as well so that you understand why I wrote the prompt like this.

Example 1: 
Input: 
 
Mnemonic:
<
"Here we see a pictograph of a tree, showing the main trunk in the long vertical stroke and the boughs/branches in the long horizontal stroke. The final two strokes sweep down in both directions to indicate the roots. Although it may look similar at first sight to the kanji for water , the order in which it is written is completely different and this affects its final appearance. 
>

This Mnemonic is for which Kanji character:    <Tree>
Art-style:
<
Art type: Line art
Art color: vibrant color
Temperature = 1
>





How to build the prompt given the mnemonic and the user preferences  details:

<
1) First from the mnemonic you have to understand the shape of the Kanji character, keywords in the mnemonic and also what the corresponding kanji character means, here the character for which the mnemonic is given means “Tree” and the mnemonic suggest that the overall shape is also that of a Tree..
All the keywords identified from the mnemonic such as tree, trunk, boughs, and roots need to be mentioned in the prompt.
2) In the mnemonic, there is a line that says “ the main trunk in the long vertical stroke” , so start the prompt with a line “ represent a single, really long trunk that extends vertically”. Please note that I have used the word “really long” because I want to exaggerate the length of the trunk so that the user can easily associate the trunk and the shape in the Kanji character.
3) Use similar logic for next line of the prompt, note that there is a line in the mnemonic that says “the boughs in the long horizontal stroke”, so the next line in the prompt should be, “represent a really long and horizontal bough/branch extending from the trunk, make sure that there is only one horizontal branch”, here also i am trying to exaggerate the length of the boughs hence I have used the word “really”. 
4) Since the mnemonic mentions long roots, the next line in the prompt can be about the roots , that is “represent two very long roots spreading outward from the base of the trunk in opposite directions, make sure there are only two very long and thick roots.”

In the prompt you can also mention that the “the image generated will be used by the user to associate with the word Tree”.

5) Lastly mention the art type, art color and the temperature.
Temperature basically means creativity, 0 temperature means “little creativity”, 1 temperature means, “medium” creativity and a temperature of 2 means “high creativity”.
6) Safety: Mention in the prompt to make sure the images created are age appropriate as the users are mostly under 18 years old.
>

So using the instructions given above the following prompt was built:
Prompt:
<
Generate a graphic using the following instructions. Also wait and take time to think before generating an illustration.


Step 1) Represent a single, really long trunk that extends vertically.
Step 2) Represent a really long and horizontal bough extending from the trunk, make sure that there is only one horizontal bough.
Step 3) Represent two very long roots spreading outward from the base of the trunk in opposite directions, make sure there are only two very long and thick roots.
The image generated will be used to help the user associate it with the concept of "Tree."


Step 4) The following are the user preferences regarding the art style; try to incorporate these into the image:
Art type: Line art;
Art color: Vibrant color;
Creativity = Medium (temperature = 1) 

Step 5) Make sure the images created are age appropriate as the users are mostly under 18 years old.
>


Example 2:
Input:
Mnemonic:
<This kanji, also a primitive, is one of the clearest instances we have of a complex pictograph. The top line is the sky, the next 3 strokes a pair of clouds, and the final 4 dots the rain collected there and waiting to fall. As a primitive it can mean either rain or weather in general. Because it takes so much space, it usually has to be contracted into a crown by shortening the second and third strokes into a crown>
This Mnemonic is for which Kanji character: <rain>
Art-style:
<Art type: Line art
Art color: vibrant color
Temperature = 1>



How to build the prompt given the mnemonic and the user preferences  details:

<
1) First from the mnemonic you have to understand the shape of the Kanji character, keywords in the mnemonic and also what the corresponding kanji character means, here the character for which the mnemonic is given means “rain” and the mnemonic suggest that the overall shape is that of a crown.
All the keywords identified from the mnemonic such as clouds and rain drops need to be mentioned in the prompt.
2) From the mnemonic, we can identify that there is a top line representing the sky. So, write in the prompt to represent the sky in the form of a horizontal line at the top.
3) Not much information is given about the shape of clouds and rain drops, so write in the prompt to “represent the clouds and the raindrops under the sky.” You have to use your own reasoning to understand that the clouds and the raindrops will be placed underneath the sky.
4) The mnemonic says that the overall shape is like a crown, so you can write in the prompt to “make the shape of the sky, clouds, and raindrops together appear like a crown overall.”. You must mention clearly in the prompt  to “not show a crown only show the sky, rain and clouds in the shape of crown”.
5) This image will be used by the user to associate with the word “rain”.

7) Lastly mention the art type, art color and the temperature.
Temperature basically means creativity, 0 temperature means “little creativity”, 1 temperature means, “medium” creativity and a temperature of 2 means “high creativity”.
8) Safety: Mention in the prompt to make sure the images created are age appropriate as the users are mostly under 18 years old.
>

So using the instructions given above the following prompt was built:
Prompt:
<
Generate a graphic using the following instructions. Also wait and take time to think before generating an illustration.

Step 1) Represent the sky as a horizontal line at the top.
Step 2) Depict clouds and raindrops below the sky.
Step 3) Combine the sky, clouds, and raindrops to form the shape of a crown. Do not simply draw a crown; creatively arrange the sky, clouds, and raindrops so that together they resemble a crown.
This image will be used to help the user associate it with the concept of "rain."


Step 4) The following are the user preferences regarding the art style; try to incorporate these into the image:
Art type: Line art;
Art color: Vibrant color;
Creativity = Medium (temperature = 1) 

Step 5) Make sure the images created are age appropriate as the users are mostly under 18 years old.
>

Example 3:
Input:
Mnemonic:
<   The elements that compose the character for see are the eye firmly fixed to a pair of human legs. Surely, somewhere in your experience, there is a vivid image just waiting to be dragged up to help you remember this character >.
This Mnemonic is for which Kanji character: <see>
Art-style:
<Art type: realistic
Art color: vibrant color
Temperature = 2 >

How to build the prompt given the mnemonic and the user preferences  details:


<
1) First from the mnemonic you have to understand the shape of the Kanji character, keywords in the mnemonic, and also what the character means, here the character for which the mnemonic is given means “see” and the mnemonic suggests that the shape is an imaginary shape of an eye fixed to a pair of human legs.
All the keywords identified from the mnemonic such as eye and human legs need to be mentioned in the prompt.
2) From the mnemonic, we can identify that there is an eye in the graphic. So, write in the prompt to represent an eye in the graphic.
3) After that, the mnemonic says that the eye is attached to human legs so write in the prompt to attach a pair of human legs to the bottom of the eye.
4) Also you can mention that the image generated will be used by the user to associate with the word “see”.
5) Lastly mention the art type, art color and the temperature.
Temperature basically means creativity, 0 temperature means “little creativity”, 1 temperature means, “medium” creativity and a temperature of 2 means “high creativity”.
6) Safety: Mention in the prompt to make sure the images created are age appropriate as the users are mostly under 18 years old.

>

So using the instructions given above the following prompt was built:
Prompt:
<
Generate a graphic using the following instructions. Also wait and take time to think before generating an illustration.

Step 1) Represent an eye in the graphic.
Step 2) Attach a pair of human legs to the bottom of the eye.
The image generated will be used by the user to associate with the word “see”.


Step 3) The following are the user preferences regarding the art style; try to incorporate these into the image:
Art type: Line art;
Art color: Black and White;
Creativity =  High (temperature = 2) 

Step 4) Make sure the images created are age appropriate as the users are mostly under 18 years old.
>


Example 4:


Input:
Mnemonic:
<Among nature’s bright lights, there are two that the biblical myth has God set in the sky: the sun to rule over the day and the moon to rule the night. Each of them has come to represent one of the common connotations of this key word: the sun, the bright insight of the clear thinker, and the moon, the bright intuition of the poet and the seer.>
This Mnemonic is for which Kanji character: <bright>
Art-style:
<Art type: Line art
Art color: Black and White
Temperature = 2>



How to build the prompt given the mnemonic and the user preferences  details:


1) First from the mnemonic you have to understand the shape of the Kanji character, keywords in the mnemonic and also what the character means, here the character for which the mnemonic is given means “bright” and the mnemonic suggests that the shape is a combination of two Kanji characters that is the kanji character for sun and the kanji character for moon. A particular shape for the Kanji of “bright” cannot be determined because it is simply a combination of the two different Kanji characters.

2) Now since Sun and Moon are the keywords that can be identified from the mnemonic , write in the prompt to represent  a sun and moon in the image side by side.
3) Since the meaning of the given Kanji character is bright, also write in the prompt to represent the bright rays coming from the sun and the moon.
The image generated will be used by the user to associate with the word “bright”.

4) Lastly mention the art type, art color and the temperature.
Temperature basically means creativity, 0 temperature means “little creativity”, 1 temperature means, “medium” creativity and a temperature of 2 means “high creativity”.
5) Safety: Mention in the prompt to make sure the images created are age appropriate as the users are mostly under 18 years old.

>

So using the instructions given above the following prompt was built:
Prompt:

<
Generate a graphic using the following instructions. Also wait and take time to think before generating an illustration.
 Step 1) Represent a sun and moon separately in the image side by side. 
Step 2) Represent bright rays coming from the sun and the moon. 
Step 3) I want to emphasize that I do not want unnecessary faces in the image. 
Step 4) The following are the user preferences regarding the art style; try to incorporate these into the image: 
Art type: Line art;
 Art color: Black and White; 
Creativity = high (temperature = 2) 
Step 5) Make sure the images created are age appropriate as the users are mostly under 18 years old.
>


Example 5:


Input:
Mnemonic:
<
The cold air from the north is so strong that we see two people sitting on the ground back to back, their arms interlocked so they don’t blow away. >
This Mnemonic is for which Kanji character: <north>
Art-style:
<Art type: Line art
Art color: Black and White
Temperature = 2>


How to build the prompt given the mnemonic and the user preferences  details:


<
1) First from the mnemonic you have to understand the shape of the Kanji character, keywords in the mnemonic and also what the character means, here the character for which the mnemonic is given means “north”. A particular shape for the Kanji of “north” cannot be determined because the mnemonic gives a scenario instead of a shape.
All the keywords identified from the mnemonic such as sitting, back to back and cold air needs to be mentioned in the prompt.
2) Then write in the prompt that it has to represent two people sitting on the ground back to back, and emphasize that the individuals are sitting back to back.
3) Next as mentioned in the mnemonic, write in the prompt that both the persons have their arms interlocked or folded.
4) Now since the mnemonic mentions cold air from the north, write in the prompt to “Add cold air breezing through, and the individuals are sitting back-to-back with their arms folded, trying to stay warm”.
You can also mention that the image generated will be used by the user to associate with the word “north”.
5) Lastly mention the art type, art color and the temperature.
Temperature basically means creativity, 0 temperature means “little creativity”, 1 temperature means “medium” creativity and a temperature of 2 means “high creativity”.
6) Safety: Mention in the prompt to make sure that the images created are age appropriate as the users are mostly under 18 years old.

>

So using the instructions given above the following prompt was built:
Prompt:

<
Generate a graphic using the following instructions. Also wait and take time to think before generating an illustration.
 Step 1) Represent two people sitting on the ground back to back, please make sure that the individuals are sitting back to back.
Step 2) Make sure both individuals have their arms interlocked or folded
step 3) Add cold air breezing through, and the individuals are sitting back-to-back with their arms folded, trying to stay warm.


Step 4) The following are the user preferences regarding the art style; try to incorporate these into the image: 
Art type: Line art; 
Art color: Black and White; 
Creativity: high (temperature = 2) 
Step 5) Make sure the images created are age appropriate as the users are mostly under 18 years old.

>

Example 6:

Input:
Mnemonic: 
<
When a tree has not yet finished growing, it produces fruit with a full flavor. When the official taster (the professional mouth to the left) determines that full flavor has been reached, the tree is pruned back so that it remains permanently not yet grown. A neat little agricultural trick and an easy way to see the sense of flavor hidden in this character.
>

This Mnemonic is for which Kanji character: <flavour>

Art-style:
<Art type: Line art
Art color: Vibrant color
Temperature = 0>


How to build the prompt given the mnemonic and the user preferences  details:


<
1) First from the mnemonic you have to understand the shape of the Kanji character, what the character means and also what are the keywords in the mnemonic. Here the Kanji character for which the mnemonic is given means “flavour”. A particular shape for the Kanji of “flavour” cannot be determined from the mnemonic because the mnemonic gives an imaginary story/scenario instead of a shape.
2) The identified keywords in the mnemonic are flavour, not yet, pruned tree, fruit, official taster.
Now you have to write the prompt highlighting all these keywords and also while making sure that it overall describes the scenario mentioned in the mnemonic.
3) You can start the prompt by writing to represent the pruned tree which is being associated with the word “not yet”, also the mnemonic emphasizes that the tree is pruned, so you have to emphasize that in the prompt as well.
4) Now mention to show few fruits on the pruned tree.
5) After which you should write in the prompt to show an official taster who is tasting a fruit beside a pruned tree.
6) You must also mention in the prompt that all these elements together should convey the story that there is a pruned tree beside which there is an official taster who is tasting a fruit from the pruned tree and this whole story is being associated with the word “flavor”.
7) Lastly mention the art type, art color and the temperature.
Temperature basically means creativity, 0 temperature means “little creativity”, 1 temperature means “medium” creativity and a temperature of 2 means “high creativity”.
8) Safety: Mention in the prompt to make sure that the images created are age appropriate as the users are mostly under 18 years old.

>


Prompt:

<
Generate a graphic using the following instructions. Also wait and take time to think before generating an illustration.

 Step 1) start with representing the pruned tree make sure its a pruned tree not a normal tree.
Step 2) Now show few fruits on the pruned tree
step 3) Now show an official taster who is tasting a fruit beside a pruned tree, this entire story is being associated with the word “flavor”.
step 4) All these elements together should convey the story that there is a pruned tree beside which there is an official taster who is tasting a fruit from the pruned tree and the fruit has good ‘flavour’.

Step 5) The following are the user preferences regarding the art style; try to incorporate these into the image: 
Art type: Line art; 
Art color: Vibrant color; 
Creativity: low (temperature = 0) 
Step 6) Make sure the images created are age appropriate as the users are mostly under 18 years old.

>
Example 7:

Input:
Mnemonic:
<
Soil and a scorpion (an “earth animal”). This is, of course, the full character from which the primitive for ground derives.
>
This Mnemonic is for which Kanji character: <ground>

Art-style:
<Art type: Line art
Art color: Vibrant color
Temperature = 0>


How to build the prompt given the mnemonic and the user preferences  details:
<
1) First from the mnemonic you have to understand the shape of the Kanji character, what the character means and also what are the keywords in the mnemonic. Here the Kanji character for which the mnemonic is given means “ground”. A particular shape for the Kanji of “ground” cannot be determined from the mnemonic because the mnemonic talks about two elements soil and scorpion which can be combined to associate with the word  “ground”.
2) The identified keywords in the mnemonic are flavour, not yet, pruned tree, fruit, official taster.
Now you have to mention these keywords in the prompt such that it overall represents the scenario described  in the mnemonic.
3) You can start the prompt by writing to represent the pruned tree which is being associated with the word “not yet”, also the mnemonic emphasizes a pruned tree so you have to emphasize that in the prompt as well.
4) Next write in the prompt to show few fruits on the pruned tree.
5) Next write in the prompt to show an official taster who is tasting a fruit beside a pruned tree.
6) Then you must explain what the overall image should look like in the prompt. You can write “All these elements together should convey the story that there is a pruned tree beside which there is an official taster who is tasting a fruit from the pruned tree. This whole story is being associated with the word ‘flavor’ ”.

7) Lastly mention the art type, art color and the temperature.
Temperature basically means creativity, 0 temperature means “little creativity”, 1 temperature means “medium” creativity and a temperature of 2 means “high creativity”.
8) Safety: Mention in the prompt to make sure that the images created are age appropriate as the users are mostly under 18 years old.

>


Prompt:

<
Generate a graphic using the following instructions. Also wait and take time to think before generating an illustration..
 Step 1) start with representing the pruned tree make sure its a pruned tree not a normal tree.
Step 2) Now show few fruits on the pruned tree
step 3) Now show an official taster who is tasting a fruit beside a pruned tree, this entire story is being associated with the word “flavor”.
step 4) All these elements together should convey the story that there is a pruned tree beside which there is an official taster who is tasting a fruit from the pruned tree and the fruit has good ‘flavour’.


Step 5) The following are the user preferences regarding the art style; try to incorporate these into the image: 
Art type: Line art; 
Art color: Vibrant color; 
Creativity: low (temperature = 0) 
Step 6) Make sure the images created are age appropriate as the users are mostly under 18 years old.
>
################################
Example 8:
Input: 
Mnemonic:
<
Turn this character 45o either way and you have the X used for the Roman numeral ten. 
>
This Mnemonic is for which Kanji character: <Ten>

Art-style:
<Art type: Line art
Art color: Vibrant color
Temperature = 1 >


How to build the prompt given the mnemonic, the  user preferences  details:
<
1) First from the mnemonic you have to understand the shape of the Kanji character, what the character means and also what are the keywords in the mnemonic. Here the Kanji character for which the mnemonic is given means the number “Ten”. 
All the keywords identified from the mnemonic such as roman numeral X , 45 degrees and Ten need to be mentioned in the prompt.
2) According to the mnemonic, we get the kanji character for Ten by rotating the roman numeral X by 45 degrees.
Now in the prompt you have to write ,“show roman numeral X” 
3) After that you have to write, “ show a curved  arrow that indicates rotation by 45 degrees”.
4) Now write that “The complete picture will be used by the user to associate it with the number ten.”
5) Lastly mention the art type, art color and the temperature.
Temperature basically means creativity, 0 temperature means “little creativity”, 1 temperature means “medium” creativity and a temperature of 2 means “high creativity”.
6) Safety: Mention in the prompt to make sure that the images created are age appropriate as the users are mostly under 18 years old.

>
Using the above instructions, the following prompt has been made.
Prompt:
<
Generate a graphic using the following instructions. Also wait and take time to think before generating an illustration.

 Step 1) start with representing the roman numeral X.
Step 2) Now show a curved  arrow that indicates rotation by 45 degrees.
The complete picture will be used by the user to associate it with the number ten.

Step 3) The following are the user preferences regarding the art style; try to incorporate these into the image: 
Art type: Line art; 
Art color: Vibrant color; 
Creativity: medium (temperature = 1) 
Step 4) Make sure the images created are age appropriate as the users are mostly under 18 years old.
>


Example 9:
Input :
Mnemonic:
<
Here we see our famous miraculous magic wand hanging, all on its own, below the ceiling, as you probably already guessed would happen. In addition to giving us two new kanji, the two shapes given in this and the preceding frame also serve to fix the use of the primitives for ceiling and floor, by drawing our attention successively to the line standing above and below the primitive element to which it is related.>

This Mnemonic is for which Kanji character: <Below>

Art-style:
<Art type: Line art;
Art color: Black and White;
Temperature = 1 >



How to build the prompt given the mnemonic, the  user preferences  details:
<
1) First from the mnemonic you have to understand the shape of the Kanji character, what the character means and also what are the keywords in the mnemonic. Here the Kanji character for which the mnemonic is given means the word “Below”. 
All the keywords identified from the mnemonic such as magic wand,  ceiling and below  need to be mentioned in the prompt.
2)Start the prompt with the ceiling, you can write in the prompt, to show a flat ceiling.
3) After that you can write, “show a magic wand hanging below the ceiling”, emphasizin the word below.
4) Now write that “The complete picture will be used by the user to associate it with the word below.”
5) Lastly mention the art type, art color and the temperature.
Temperature basically means creativity, 0 temperature means “little creativity”, 1 temperature means “medium” creativity and a temperature of 2 means “high creativity”.
6) Safety: Mention in the prompt to make sure that the images created are age appropriate as the users are mostly under 18 years old.
>
Using the above instructions, the following prompt has been made.
Prompt:
<
Generate a graphic using the following instructions. Also wait and take time to think before generating an illustration.
 Step 1) Start with representing  a flat ceiling.
Step 2) Now show a magic wand hanging below the flat ceiling, please note that the wand is hanging below the ceiling.
The complete picture will be used by the user to associate it with the word below.

Step 3) The following are the user preferences regarding the art style; try to incorporate these into the image: 
Art type: Line art; 
Art color: Black and White;
Creativity: medium (temperature = 1) 
Step 4) Make sure the images created are age appropriate as the users are mostly under 18 years old.






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
        <h1 style='text-align: center;'>Prompt Builder for Mnemonic Illustrations</h1>
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
    kanji_character = st.text_input("Enter the english meaning of the kanji character:", placeholder="e.g., 木 (Tree)")

    # Third Subsection: Art Style
    st.markdown("---")
    st.header("Art Style")
    art_type = st.selectbox("Select Art Type:", ["Line Art(Preferred)", "Realistic"])
    art_color = st.selectbox("Select Art Color:", ["Black & White (Preferred)", "Vibrant Color"])
    temperature = st.selectbox("Select Temperature; Temperature represents creativity of the image to be generated (0-Low, 1-Medium, 2-High):", [0, 1, 2])

    # Button to Generate Prompt
    if st.button("Generate Prompt"):
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
        )
        st.write(call_mistral_api(prompt))

# Run the main function
if __name__ == "__main__":
    main()
)
