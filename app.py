import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
from openai import OpenAI
client = OpenAI()

import streamlit as st
import cloudinary
from cloudinary import CloudinaryImage
import cloudinary.uploader
import cloudinary.api

config = cloudinary.config(
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key = os.getenv('CLOUDINARY_API_KEY'),
    api_secret = os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

st.title('CloudArtify')
st.markdown("""This project uses Cloudinary AI Background Removal add-on to remove the background of images and paired with OpenAI DALL-E, which prompts a user to type a text to generate a spooky or nightmarish image to replace the image's transparent cover, thereby transforming the image accordingly.
""")

def upload_user_image(image):
  try:
    upload_response = cloudinary.uploader.upload(image, unique_filename=True, overwrite=False)
    return upload_response['public_id']
  except Exception as err:
    st.error(f'Error uploading the image: {err}')
    return None

def generate_image(prompt=None, user_image=None):
  if not prompt:
    prompt = 'random nightmarish, weird, and spooky background for an image.'
  try:
    response = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size="1024x1024",
      quality="standard",
      n=1,
    )
    image_url = response.data[0].url
    generated_image_upload = cloudinary.uploader.upload(image_url, unique_filename=False, overwrite=True)
    generated_public_id = generated_image_upload['public_id']

    if user_image:
      user_uploaded_image_public_id = upload_user_image(user_image)
      transformed_image = CloudinaryImage(user_uploaded_image_public_id).build_url(transformation=[
        {'effect': "background_removal"},
        {'width': 700, 'crop': "scale"},
        {'underlay': generated_public_id},
        {'flags': "layer_apply", 'y': -200}
      ])
      st.markdown(f'<img src="{transformed_image}" width="700"/>', unsafe_allow_html=True)
        # st.image(transformed_image, width=700, caption="Transformed Image")
  except Exception as err:
    st.error(f'An error occured: {err}')


user_prompt = st.text_input('Enter a prompt to create a spooky background (optional): ')

upload_file_img = st.file_uploader('Choose an image file', type=['jpg', 'jpeg'])

if st.button('Generate and Transform image'):
  if upload_file_img is not None:
    generate_image(user_prompt, upload_file_img)
  else:
    st.stop()


# if upload_file_img is not None:
#   result = cloudinary.uploader.upload(upload_file_img)
#   st.image(result['url'])
# else:
#    st.error('Please upload an image file.')
