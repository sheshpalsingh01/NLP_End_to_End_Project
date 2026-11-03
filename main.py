from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.textSummarizer.pipeline.model_trainer_pipeline import ModelTrainerPipeline 
from src.textSummarizer.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline



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

STAGE_NAME ="Model Trainer stage"

try:
    logger.info("Starting model trainer ........")
    obj = ModelTrainerPipeline()
    obj.initiate_model_trainer()
    logger.info("Model Trainer completed .........")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME ="Model Evaluation stage"

try:
    logger.info("Starting model evaluation ........")
    obj = ModelEvaluationPipeline()
    obj.initiate_model_evaluation()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    logger.info("Model Evaluation completed .........")
except Exception as e:
    logger.exception(e)
    raise e                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

