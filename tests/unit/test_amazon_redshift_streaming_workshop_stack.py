import aws_cdk as core
import aws_cdk.assertions as assertions

from amazon_redshift_streaming_workshop.amazon_redshift_streaming_workshop_stack import AmazonRedshiftStreamingWorkshopStack

# example tests. To run these tests, uncomment this file along with the example
# resource in amazon_redshift_streaming_workshop/amazon_redshift_streaming_workshop_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AmazonRedshiftStreamingWorkshopStack(app, "amazon-redshift-streaming-workshop")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
