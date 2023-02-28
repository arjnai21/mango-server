import json
import openai

f = open("content.json", "r")
str = f.read()
data = json.loads(str)

openai.api_key = "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"

# characteristics = [ "Location", "Age", "Generation", "Gender", "Language", "Education level", "Field of study","School", "Ethnic affinity", "Income"]

geographic_boundaries = data["geographic_boundaries"] # Use python api to get city from coordinates
country = data["country"]
carrier_list = data["carrier_list"]
operating_system = data["operating_system"]
device_type = data["device_type"]
make = data["make"]
model = data["model"]

def generate_prompt(country, geographic_boundaries, carrier_list, operating_system, device_type, make, model):
    prompt = "I am a marketer for Blendr. Blendr sells premium blenders. Write a high-quality, 200 word ad that would convince the individual to buy the blender."
    
    prompt += f'The individual is from  {country}. '
    prompt += f'The individual may reside at these coordinates: {geographic_boundaries}. '
    prompt += f'This is the carrier list: {carrier_list}. '
    prompt += f'These are the possible operating systems: {operating_system}. '
    prompt += f'These are the possible device types: {device_type}. '
    prompt += f'This is the individuals make: {make}, and the possible models are {model}.'

    print(prompt)
    return prompt
    # return "Write a good clever 300 word blender ad that would convince the following individual to buy the blender.The individual's age is 2, he is from the North east, he is a male, and he is Indian."
    # return "I am a 5 year old who wants to buy a blender. I am from the Northeast. Write an ad that would convince me to buy a blender."
    # return "Write a good clever 300 word blender ad that would convince the following individual to buy the blender.The individual's age is 90 and is from Mexico "


# Looking for a blender that can do it all? Look no further than the versatile and powerful blender from BlenderX. Whether you're making a smoothie, a frozen drink, or a soup, our blender can handle it all with ease. Plus, our blender is designed for easy cleanup, so you can spend more time enjoying your creation and less time scrubbing pots and pans.
def main(name):
    file = open("results.txt", "w")
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(country, geographic_boundaries, carrier_list, operating_system, device_type, make, model),
        temperature=0.7,
        max_tokens=400
    )
    print(response)


if __name__ == '__main__':
    main('PyCharm')
