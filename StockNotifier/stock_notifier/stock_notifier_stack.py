from aws_cdk import (
    Stack,
    aws_ssm as ssm,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_events as events,
    Duration
)
from constructs import Construct
from aws_cdk.aws_ecr_assets import DockerImageAsset
import os

class StockNotifierStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # ParameterStore details for Discord webhook URL
        discord_webhook_url = ssm.StringParameter(
            self,
            "DiscordWebhookUrl",
            parameter_name="DISCORD_WEBHOOK_URL",
            string_value=os.getenv("DISCORD_WEBHOOK_URL"),
            description="Discord Web Server",
            tier=ssm.ParameterTier.STANDARD
        )
        
        
        # Create a ECR repository for our docker image
        stock_notifier_docker_image = DockerImageAsset(
            self,
            "StockNotifierImage",
            directory="./lambda",
            file="Dockerfile"
        )
        
        # Lambda Function
        stock_notifier_lambda = _lambda.DockerImageFunction(
            self,
            "StockNotifierLambda",
            function_name="StockNotifierLambda",
            memory_size=2048,
            timeout=Duration.seconds(600),
            environment={"DISCORD_WEBHOOK_URL_ARN": discord_webhook_url.parameter_arn},
            code=_lambda.DockerImageCode.from_ecr(
                repository=stock_notifier_docker_image.repository,
                tag_or_digest=stock_notifier_docker_image.image_tag
            )
        )
        
        # Stock Dynamo DB Table
        stock_dynamo_table = dynamodb.Table(
            self,
            "StockTable",
            partition_key=dynamodb.Attribute(
                name="PartId",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="StoreId",
                type=dynamodb.AttributeType.STRING
            ),
            table_name="Stock_Table",
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )
        
        # Cloudwatch event (once per minute)
        one_minte_event_rule = events.Rule(
            self,
            "MinuteRule",
            rule_name="MinuteRule",
            schedule=events.Schedule.cron(
                # TODO, change to one minute
                hour="0",
                minute="0"
            )
        )
        
        
        
        
        
        
        
        
