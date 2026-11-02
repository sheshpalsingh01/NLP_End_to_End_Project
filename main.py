from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info("Starting data ingestion")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info("Data ingestion completed")
    logger.info(f"Stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)

STAGE_NAME ="Data Transformation stage"

try:
    logger.info("Starting data transformation ........")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info("Data Transformation complate .........")
except Exception as e:
    logger.exception(e)
    raise e