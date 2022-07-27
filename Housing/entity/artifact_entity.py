from collections import namedtuple

from Housing.component.stage_01_data_ingestion import DataIngestion

DataIngestionArtifact = namedtuple("DataIngestionArtifact",
        ["train_file_path","test_file_path","is_ingested","message"])