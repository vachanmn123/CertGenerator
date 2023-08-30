# CertGenerator

The Particiaption certificate generator website for **UnoStruct: An Introduction to Structures and Unions**, conducted at [Bapuji Institute of Engineering and Technology](https://bietdvg.edu) on 28th August 2023.

## Installation and Running

To run this project, you need to have python3. Use pip to install the dependencies

```bash
python3 -m pip install -r requirements.txt
```

Make a new folder called `certificates/` to store the certificates
```bash
mkdir certificates
```

Create a .env file and add the `MONGODB_URI` field
```bash
touch .env
```

```env
MONGODB_URI=<YOUR-MONGODB-URI>
```

To run the project, run the `app.py` file.

```bash
python3 app.py
```

## How it works

The project utilizes Flask, and the main routing logic is stored in the `app.py` file. The primary route, accessible via `/`, serves the `templates/index.html` page. This page contains an HTML form that triggers a POST request to the `/submitform` route on the Flask server. Within the `app.py` file, this route is responsible for both storing the feedback in a dictionary and uploading it to MongoDB. Additionally, this route invokes the `write_name()` function, which resides in `utils.py`.

The `write_name()` function follows these steps:

1. It begins by loading the appropriate certificate image based on the branch and stores this image.
2. The loaded image is then transformed into a drawing area using the `ImageDraw.Draw()` function from the PIL (Python Imaging Library) package.
3. Location information for the text is pre-calculated and hardcoded for this specific group of certificates.
4. The desired font is loaded, and an appropriate font size is established.
5. Using the collected information, the function writes the specified text onto the image and saves it within the `certificates/` directory.

Once the certificate generation is complete, the filename is returned. Subsequently, the Flask server renders the `templates/submitform.html` page. This page showcases the generated image by making a request to another custom-defined route: `/certificates/<name>`, where `name` corresponds to the certificate's name. By utilizing Flask's `send_file()` function, the certificate image is transmitted. 

Furthermore, the page features a "Share" button that employs a JavaScript function enclosed within a `<script>` tag. This JavaScript function utilizes the browser API's `navigator.share()` function to facilitate image sharing. Before sharing, the image is fetched through the `fetch()` function and converted to the appropriate format for seamless sharing.
