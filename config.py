import os

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('admin')}:{os.getenv('ShubhDATA')}@{os.getenv('database-2.c984o0e84367.ap-south-1.rds.amazonaws.com')}/{os.getenv('database-2')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
