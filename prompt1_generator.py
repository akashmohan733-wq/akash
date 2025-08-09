def generate_image_prompt(user_description, llm_model="Mistral"):
    """
    Generates an image prompt based on user input, using an LLM.

    Args:
        user_description (str): The user's description of the picture.
        llm_model (str):  The name of the LLM to use (e.g., "Mistral", "GPT-3.5").

    Returns:
        str: The generated prompt.
    """

    if llm_model == "Mistral":
        base_prompt = f"""
        Generate a highly detailed and evocative prompt for an image generation model, like Midjourney or Stable Diffusion. 
        Include specific artistic keywords and details to guide the generation.
        Here's the description:
        {user_description}
        Specifically, include:
        - Art Style (e.g., photorealistic, impressionistic, anime, digital painting)
        - Lighting (e.g., soft, dramatic, golden hour, volumetric lighting)
        - Composition (e.g., rule of thirds, leading lines, symmetrical)
        - Key Details and elements to include
        """
    elif llm_model == "GPT-3.5":
        base_prompt = f"""
        Create a detailed prompt for an image generation model. The user has provided a description of a picture.

        User Description:
        {user_description}

        The prompt should specify:
        - Art Style (e.g., realistic, abstract, cartoon)
        - Lighting conditions (e.g., warm, cool, dark, bright)
        - Camera angle or composition (e.g., wide shot, close-up)
        - Key elements and details to emphasize.
        """
    else:
        base_prompt = f"""
        Generate an image prompt based on the following description:
        {user_description}
        """

    final_prompt = base_prompt
    return final_prompt


# Get user input
user_input = input("Enter a description of the picture: ")

# Generate the prompt
generated_prompt = generate_image_prompt(user_input)

# Print the prompt
print(generated_prompt)
