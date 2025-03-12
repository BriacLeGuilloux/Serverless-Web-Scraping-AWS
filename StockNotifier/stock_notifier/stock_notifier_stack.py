from aws_cdk import (
    Stack,
    aws_ssm as ssm
)
from constructs import Construct
from aws_cdk.aws_ecr_assets import DockerImageAsset
import os

class StockNotifierStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # ParameterStore 
        
        
        # Create a ECR repository for our docker image
        stock_notifier_docker_image = DockerImageAsset(
            self,
            "StockNotifierImage",
            directory="./lambda",
            file="Dockerfile"
        )
