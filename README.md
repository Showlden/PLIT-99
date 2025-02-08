# About the Project
This project is a web application developed for managing various aspects of our IT Lyceum. It includes features for handling news updates, staff management, study-related resources, and user management. The project is built using Django, following a modular structure to ensure scalability and maintainability.

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <repository-url>
cd <project-directory>
```

### 2. Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables (.env)
Create a `.env` file in the `core/` directory with the following content:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3

# Cloudinary Settings (for media storage)
CLOUDINARY_URL=YOUR_CLOUDINARY_URL
```
Replace the placeholders with your actual Cloudinary credentials.

### 5. Apply Migrations
```sh
python manage.py migrate
```

### 6. Create a Superuser
```sh
python manage.py createsuperuser
```

### 7. Run the Development Server
```sh
python manage.py runserver
```

### 8. Access the Application
Open `http://127.0.0.1:8000/` in your browser.

## Additional Information
- **Cloudinary Integration:** Cloudinary is used for media file storage. Ensure you set up the `.env` file correctly with your Cloudinary credentials.
- **Django Admin Panel:** Accessible at `http://127.0.0.1:8000/admin/`.

## License
This project is licensed under the MIT License.