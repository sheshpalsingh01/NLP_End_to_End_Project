from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_data_ingestion_pipeline import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info("Starting data ingestion")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info("Data ingestion completed")
    logger.info(f"Stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.exception(e)

# if __name__ == "__main__":
#     try:
#         logger.info("Starting data ingestion")
#         obj = DataIngestionPipeline()
#         obj.initiate_data_ingestion()
#         logger.info("Data ingestion completed")
#     except Exception as e:
#         logger.exception(e)