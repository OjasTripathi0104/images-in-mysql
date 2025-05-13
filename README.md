A simple project that allows you to upload images from a folder to a MySQL database (as BLOBs). Then, you can retrieve those images from the database and save them locally.

**Requirements:**
1) Python 3.7+
2) MySQL Server
3) pip (Python package manager)

**Setup Instructions:**
1) Install the python dependencies in your project folder: <br />
pip install mysql-connector-python python-dotenv
2) Open your MySQL client and run: <br />
CREATE DATABASE image_gallery; <br />
USE image_gallery; <br />
CREATE TABLE images ( <br />
    id INT AUTO_INCREMENT PRIMARY KEY, <br />
    image_name VARCHAR(255) NOT NULL, <br />
    image_data LONGBLOB NOT NULL <br />
); 
3) Create a file named .env in the root directory and add your MySQL credentials: <br />
DB_HOST=localhost <br />
DB_NAME=image_gallery <br />
DB_USER=root <br />
DB_PASSWORD=your_password_here <br />
4) Create a folder named Images/ in the project root and place the image files you want to upload there.

**Usage:**
1) Upload images to MySQL: <br />
python upload.py <br />
This will insert all valid images in the Images/ folder into the images table in your database.
2) Retrieve images from MySQL: <br />
python retrieve.py <br />
This will fetch all images from the database and store them in the OutputImages/ folder.
