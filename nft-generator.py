#!/usr/bin/env python
# coding: utf-8

# In[104]:


# code based on https://betterprogramming.pub/create-your-own-nft-collection-with-python-82af40abf99f
# original code in folder

from PIL import Image
from IPython.display import display
import random
import json
import os

# In[105]:


##GLOBAL CONFIG

assetsFolder = 'assets'
TOTAL_IMAGES = 100  # Number of random unique images we want to generate

# In[106]:


# Search for files in assets folder tree (carefful, use only png images here)

folderContent = os.listdir('./' + assetsFolder)

folder = {}

for f in folderContent:
    folder[f] = os.listdir('./' + assetsFolder + '/' + f)

# In[107]:


# Generate Traits

all_images = []


# A recursive function to generate unique image combinations
def create_new_image():
    new_image = {}  #

    for i in folder:
        new_image[i] = random.choices(folder[i])[0]

    # For each trait category, select a random trait based on the weightings    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES):
    new_trait_image = create_new_image()

    all_images.append(new_trait_image)


# print(all_images)


# In[108]:


# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)


print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

# In[109]:


# Get Trait Counts

counts = {}

for image in all_images:

    for i in folder:
        counts[i] = 0

for image in all_images:

    for i in folder:
        counts[i] += 1

# In[110]:


#### Generate Images

# Check whether the specified path exists or not
isExist = os.path.exists(f'./images_' + assetsFolder)

if not isExist:
    # Create a new directory because it does not exist
    os.mkdir(f'./images_' + assetsFolder)
    print("The new directory is created!")

images_img = {}

for item in all_images:

    for i in folder:
        # print(f'./{assetsFolder}/{i}/{item[i]}')
        images_img[i] = Image.open(f'./{assetsFolder}/{i}/{item[i]}').convert('RGBA')

    # Create each composite
    for ii in images_img:
        if 'com' in locals():
            com = Image.alpha_composite(com, images_img[ii])
        else:
            com = Image.alpha_composite(images_img[ii], images_img[ii])

    # Convert to RGB
    rgb_im = com.convert('RGBA')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save('./images_' + assetsFolder + '/' + file_name)
