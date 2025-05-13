from dotenv import load_dotenv
import mysql.connector
import os
load_dotenv()

def insert_images_from_folder(folder_path):
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        cursor = connection.cursor()
        
        sql_query = """ INSERT INTO images (image_name, image_data)
                        VALUES (%s, %s)"""

        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                image_path = os.path.join(folder_path, filename)
                with open(image_path, 'rb') as file:
                    binary_data = file.read()
                
                image_name = filename  
                insert_tuple = (image_name, binary_data)
                cursor.execute(sql_query, insert_tuple)

        connection.commit()
        print("All images from the folder inserted successfully")

    except mysql.connector.Error as error:
        print(f"Failed to insert images into MySQL table: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Folder containing images to be uploaded
folder_path = r'./Images' 

insert_images_from_folder(folder_path)
