import json
import openai
from geopy.geocoders import Nominatim

f = open("content.json", "r")
s = f.read()
data = json.loads(s)

openai.api_key = ""

# characteristics = [ "Location", "Age", "Generation", "Gender", "Language", "Education level", "Field of study","School", "Ethnic affinity", "Income"]

geographic_boundaries = data["geographic_boundaries"] # Use python api to get city from coordinates
country = data["country"]
carrier_list = data["carrier_list"]
operating_system = data["operating_system"]
device_type = data["device_type"]
make = data["make"]
model = data["model"]
company_name = data["company_name"]
industry = data["industry"]
description = data["description"]

def pull_city(geographic_boundaries):
    string = ""
    geolocator = Nominatim(user_agent="App")
    for i in geographic_boundaries:
        Latitude = str(i["lat"])
        Longitude = str(i["long"])

        location = geolocator.reverse(Latitude+","+Longitude)
        address = location.raw['address']

        string +=  f"within {i['range']} meters of {address.get('county', '')}, {address.get('state', '')}; "
    
    chomp = string[:-2]
    return chomp

def generate_prompt(country, geographic_boundaries, carrier_list, operating_system, device_type, make, model, company_name, industry, description):
    prompt = f"I am a marketer for {company_name} in the {industry} industry. {description} Write a high-quality, 200 word ad for {company_name}. "
    
    prompt += f'The individual that will see this ad is from  {country}. '
    prompt += f'The individual may reside at these places: {pull_city(geographic_boundaries)}. ' #Find tune this, kinda creepy
    prompt += f'This is the carrier list: {carrier_list}. '
    prompt += f'These are the possible operating systems: {operating_system}. '
    prompt += f'These are the possible device types: {device_type}. ' #A little weird
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
        prompt=generate_prompt(country, geographic_boundaries, carrier_list, operating_system, device_type, make, model, company_name, industry, description),
        temperature=0.7,
        max_tokens=400
    )
    print(response)


if __name__ == '__main__':
    main('PyCharm')
