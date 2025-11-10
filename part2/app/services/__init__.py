"""Services package initialization."""
from app.services.facade import HBnBFacade

# Create a single shared instance of the facade
facade = HBnBFacade()
