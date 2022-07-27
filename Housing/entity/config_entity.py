from collections import namedtuple


DataIngestionConfig = namedtuple("DataIngestionConfig",
                    ["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])



DataTranformationConfig = namedtuple("DataTranformationConfig",
                    ["add_bedroom_per_room",
                    "transformed_train_dir",
                    "transorm_test_dir",
                    "preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig",
                        ['trained_model_file_path',
                        "base_accuracy",
                        ])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",
                        ["timestamp"])

ModelPushConfig = namedtuple("ModelPushConfig",["export_dir_path"])
