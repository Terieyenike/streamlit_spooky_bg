# CloudArtify

CloudArtify is a web application that utilizes Cloudinary's AI Background Removal add-on and OpenAI's DALL-E to transform images. Users can upload an image and generate a spooky or nightmarish background based on a text prompt, which is then applied to the uploaded image.

![generated image](dane-wetton-t1NEMSm1rgI-unsplash.jpeg)

## Features

- Upload an image file (JPG, JPEG).
- Generate a spooky background using a text prompt.
- Remove the background of the uploaded image and replace it with the generated background.
- Display the transformed image in the web application.

## Technologies Used

- Python
- Streamlit
- Cloudinary
- OpenAI DALL-E
- dotenv for environment variable management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Terieyenike/streamlit_spooky_bg
   cd streamlit_spooky_bg
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add your Cloudinary and OpenAI API keys:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
   CLOUDINARY_API_KEY=your_cloudinary_api_key
   CLOUDINARY_API_SECRET=your_cloudinary_api_secret
   ```

## Usage

1. Run the application:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an image and enter a prompt to generate a spooky background.

4. Click the "Generate and Transform image" button to see the result.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Cloudinary](https://cloudinary.com/) for their powerful image management and AI capabilities.
- [OpenAI](https://openai.com/) for providing the DALL-E model for image generation.

## Author

- [Teri](https://x.com/unicodebyte)
