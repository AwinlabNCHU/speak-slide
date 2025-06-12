from app.database import Base, engine, SessionLocal
from app.models.user import User
import logging
import time
import os
from sqlalchemy import text, inspect

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def wait_for_db_connection(max_retries=3, retry_delay=1):
    """Wait for database connection to be available."""
    for attempt in range(max_retries):
        try:
            # Try to connect to the database
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
                conn.commit()
            return True
        except Exception as e:
            if attempt < max_retries - 1:
                logger.warning(f"Database connection attempt {attempt + 1} failed: {str(e)}")
                time.sleep(retry_delay)
            else:
                logger.error(f"Could not connect to database after {max_retries} attempts")
                return False
    return False

def drop_all_tables():
    """Drop all tables from the database."""
    try:
        # Get all table names
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        
        if not table_names:
            logger.info("No tables found to drop")
            return True
            
        # Drop each table
        with engine.connect() as conn:
            for table in table_names:
                logger.info(f"Dropping table: {table}")
                conn.execute(text(f"DROP TABLE IF EXISTS {table}"))
            conn.commit()
            
        logger.info("All tables dropped successfully")
        return True
    except Exception as e:
        logger.error(f"Error dropping tables: {str(e)}")
        return False

def recreate_tables():
    """Recreate database tables with proper error handling."""
    try:
        # Wait for database connection
        if not wait_for_db_connection():
            return False

        # Drop all tables
        if not drop_all_tables():
            return False
        
        # Create all tables
        logger.info("Creating all tables...")
        Base.metadata.create_all(bind=engine)
        
        # Verify tables were created
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        if not table_names:
            logger.error("No tables were created")
            return False
            
        logger.info(f"Database tables recreated successfully: {table_names}")
        return True
    except Exception as e:
        logger.error(f"Error recreating tables: {str(e)}")
        return False

if __name__ == "__main__":
    # Delete existing database files
    db_files = ["vute.db", "sql_app.db"]
    for db_file in db_files:
        if os.path.exists(db_file):
            try:
                os.remove(db_file)
                logger.info(f"Deleted existing database file: {db_file}")
            except Exception as e:
                logger.error(f"Error deleting database file {db_file}: {str(e)}")
    
    # Recreate tables
    if not recreate_tables():
        exit(1) 