from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user, records, dashboard
# create tables
Base.metadata.create_all(bind=engine)

# create FastAPI app
app = FastAPI(
    title="Finance Dashboard Backend",
    description="Role-based financial management system",
    version="1.0.0"
)

# include routers
app.include_router(user.router)
app.include_router(records.router)
app.include_router(dashboard.router)