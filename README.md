# Poligraph

A modern dashboard application built with Reflex for analyzing and visualizing BlueSky social media data.

## Technologies

- **Frontend Framework**: [Reflex](https://reflex.dev/) - Python framework for building web apps
- **Data Source**: [BlueSky API](https://atproto.com/) via bsky-sdk
- **Backend**: FastAPI for API endpoints
- **Language**: Python 3.9+
- **Package Management**: pip/requirements.txt

## Project Structure

```
poligraph/
├── assets/               # Static assets (images, CSS)
├── poligraph/           # Main package directory
│   ├── components/      # Reusable UI components
│   │   ├── navbar.py
│   │   ├── sidebar.py
│   │   └── dashboard_widgets.py
│   ├── pages/          # Page definitions
│   │   └── dashboard.py
│   ├── state/          # State management
│   │   └── base_state.py
│   ├── styles/         # Style definitions
│   │   └── styles.py
│   └── main.py         # Application entry point
├── tests/              # Test files
├── requirements.txt    # Project dependencies
└── setup.py           # Package configuration
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tyree88/poligraph.git
cd poligraph
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
reflex run
```

The application will be available at http://localhost:3000

## Git Development Workflow

### Branch Structure

- `main` - Production-ready code
- `develop` - Main development branch
- `feature/*` - Feature branches
- `bugfix/*` - Bug fix branches
- `release/*` - Release preparation branches

### Creating a New Feature

1. Start from develop branch:
```bash
git checkout develop
git pull origin develop
```

2. Create a new feature branch:
```bash
git checkout -b feature/your-feature-name
```

3. Push the branch and set upstream:
```bash
git push -u origin feature/your-feature-name
```

### Development Best Practices

1. **Commit Guidelines**
   - Write clear, descriptive commit messages
   - Use present tense ("Add feature" not "Added feature")
   - Keep commits focused and atomic
   - Example: `git commit -m "Add BlueSky authentication component"`

2. **Stay Updated**
```bash
# Update your feature branch with develop
git checkout develop
git pull origin develop
git checkout feature/your-feature-name
git merge develop
```

3. **Before Pushing**
   - Run tests if available
   - Check code formatting
   - Verify the application runs locally

### Merging Features

1. Update your feature branch:
```bash
git checkout develop
git pull origin develop
git checkout feature/your-feature-name
git merge develop
```

2. Push your changes:
```bash
git push origin feature/your-feature-name
```

3. Create a Pull Request:
   - Base branch: `develop`
   - Compare branch: `feature/your-feature-name`
   - Include description of changes
   - Request review if required

4. After merge, cleanup:
```bash
git checkout develop
git pull origin develop
git branch -d feature/your-feature-name
```

## Development Guidelines

### Component Structure
- Keep components small and focused
- Use proper typing for props and state
- Document component props and behavior

### State Management
- Use Reflex State for global state
- Keep state updates atomic
- Document state changes

### Styling
- Use the defined style constants in `styles.py`
- Follow the existing component styling patterns
- Keep styles modular and reusable

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- Your Name - [tyreepearson88@gmail.com](mailto:tyreepearson88@gmail.com)
- Project Link: [https://github.com/tyree88/poligraph](https://github.com/tyree88/poligraph)
