import reflex as rx


config = rx.Config(
    app_name="poligraph",
    
    # Tailwind CSS configuration file.
    # tailwind: Any = {'plugins': ['@tailwindcss/typography']}
    
    # Connect to your own database.
    # db_url="postgresql://user:password@localhost:5432/my_db",
    
    # Async database connection.
    # async_db_url="postgresql://user:password@localhost:5432/my_db",
    
    # Redis database connection.
    # redis_url="redis://localhost:6379",
    
    # Change the frontend path.
    # frontend_path="/",
    
    # Deploy to the cloud.
    # deploy_url="https://poligraph.reflex.dev",
    
    # Change the frontend port.
    # frontend_port=3001,
    
    # Set log level to debug
    # log_level="debug",
)