# Flaskr - A Flask Blog Application

A feature-rich blog application built with Flask, featuring user authentication, post management, and a rating system.

## Features

### ✅ Implemented Features
- **User Authentication**: Register, login, and logout functionality
- **Blog Posts**: Create, read, update, and delete blog posts
- **Post Details**: Individual post pages with full content display
- **Rating System**: Rate posts from 1-5 stars with average rating display
- **User Authorization**: Users can only edit/delete their own posts
- **Responsive Design**: Clean, modern UI with CSS styling

### 🚧 Planned Features (TODO)
- Comments system on posts
- Tags for categorizing posts
- Search functionality to filter posts
- Pagination (5 posts per page)
- Image upload support for posts
- Markdown formatting for post content
- RSS feed for new posts

## Project Structure

```
Flaskr/
├── flaskr/
│   ├── __init__.py          # Flask application factory
│   ├── auth.py              # Authentication blueprint
│   ├── blog.py              # Blog functionality blueprint
│   ├── db.py                # Database utilities
│   ├── schema.sql           # Database schema
│   ├── templates/
│   │   ├── base.html        # Base template
│   │   ├── auth/
│   │   │   ├── login.html   # Login page
│   │   │   └── register.html # Registration page
│   │   └── blog/
│   │       ├── create.html  # Create post form
│   │       ├── index.html   # Posts listing
│   │       ├── show.html    # Individual post view
│   │       └── update.html  # Edit post form
│   └── static/
│       └── style.css        # Application styling
├── tests/                   # Test suite
│   ├── conftest.py          # Test configuration
│   ├── data.sql             # Test data
│   ├── test_auth.py         # Authentication tests
│   ├── test_blog.py         # Blog functionality tests
│   ├── test_db.py           # Database tests
│   └── test_factory.py      # Application factory tests
├── pyproject.toml           # Project configuration
└── README.md               # This file
```

## Database Schema

The application uses SQLite with the following tables:

- **user**: Stores user accounts (id, username, password)
- **post**: Stores blog posts (id, author_id, title, body, created, rating_count, rating_total)
- **comment**: Reserved for future comment functionality

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Flaskr
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   ```

4. **Initialize the database**
   ```bash
   flask --app flaskr init-db
   ```

## Development

### Running the Application

**Development mode (with auto-reload):**
```bash
flask --app flaskr run --debug
```

**Production mode:**
```bash
flask --app flaskr run
```

The application will be available at `http://127.0.0.1:5000`

### Available Routes

- `/` - Home page with posts listing
- `/auth/login` - User login
- `/auth/register` - User registration
- `/auth/logout` - User logout
- `/create` - Create new post
- `/<id>/show` - View individual post
- `/<id>/update` - Edit post
- `/<id>/delete` - Delete post
- `/<id>/rate` - Rate a post

### Testing

**Run all tests:**
```bash
pytest
```

**Run tests with coverage:**
```bash
coverage run -m pytest
coverage report
coverage html  # Generates HTML report in htmlcov/
```

**Current test status:** 21 passing, 3 failing (form validation and display issues)

### Database Commands

**Initialize database:**
```bash
flask --app flaskr init-db
```

**View available commands:**
```bash
flask --app flaskr --help
```

## Production Deployment

### Building Distribution Package

**Create wheel package:**
```bash
python -m build --wheel
```

The package will be created in `dist/flaskr-1.0.0-py3-none-any.whl`

### Installing on Production Server

1. **Install the package:**
   ```bash
   pip install flaskr-1.0.0-py3-none-any.whl
   ```

2. **Initialize database:**
   ```bash
   flask --app flaskr init-db
   ```

3. **Configure production settings:**
   - Set `SECRET_KEY` environment variable
   - Configure database path
   - Set up reverse proxy (nginx, etc.)

## Current Status

### Working Features
- ✅ User registration and authentication
- ✅ Blog post CRUD operations
- ✅ Individual post detail pages
- ✅ Post rating system (1-5 stars)
- ✅ User authorization (users can only edit their own posts)
- ✅ Clean, responsive UI

### Known Issues
- ⚠️ Some tests failing due to form validation and display format issues
- ⚠️ Missing author/date display in post listings
- ⚠️ Form validation not properly implemented

### Next Steps
1. Fix failing tests
2. Implement comment system
3. Add search functionality
4. Implement pagination
5. Add image upload support
6. Add Markdown formatting
7. Create RSS feed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is part of the Flask tutorial and follows Flask's licensing terms.