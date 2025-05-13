from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

def retrieve_images(output_folder):
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        cursor = connection.cursor()
        sql_query = "SELECT id, image_name, image_data FROM images"
        cursor.execute(sql_query)
        records = cursor.fetchall()
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for record in records:
            image_id, image_name, image_data = record
            base_name = os.path.basename(image_name)
            output_path = os.path.join(output_folder, f"output_{image_id}_{base_name}")

            with open(output_path, 'wb') as file:
                file.write(image_data)
            print(f"Image {base_name} retrieved and saved as {output_path}")

    except mysql.connector.Error as error:
        print(f"Failed to retrieve images from MySQL table: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Folder to save retrieved images
output_folder = r'./OutputImages'

retrieve_images(output_folder)
