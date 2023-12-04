from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info("...........stage{STAGE_NAME} started .........")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("...........stage{STAGE_NAME} completed.........")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data validation Stage"

try:
    logger.info("...........stage{STAGE_NAME} started .........")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info("...........stage{STAGE_NAME} completed.........")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info("...........stage{STAGE_NAME} started .........")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info("...........stage{STAGE_NAME} completed.........")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer Stage"

try:
    logger.info("...........stage{STAGE_NAME} started .........")
    data_trainer = ModelTrainerTrainingPipeline()
    data_trainer.main()
    logger.info("...........stage{STAGE_NAME} completed.........")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info("...........stage{STAGE_NAME} started .........")
    data_trainer = ModelEvaluationTrainingPipeline()
    data_trainer.main()
    logger.info("...........stage{STAGE_NAME} completed.........")
except Exception as e:
    logger.exception(e)
    raise e
