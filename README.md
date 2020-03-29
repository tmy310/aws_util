# aws_util
aws python libraries.

# libraries
## prerequisites
aws-cli

## cloud_formation_stack_resource_checker.py
### purpose
cloudformation has stack limits.
this is to check stack.
### usage
```
cloud_formation_stack_resource_checker = CloudFormationStackResourceChecker()
cloud_formation_stack_resource_checker.get_stack_and_resource_count()
```
### sample
```
python sample.py
[{'StackName': 'hogehoge', 'ResourceCount': 100}, {'StackName': 'hogehoge2', 'ResourceCount': 1}
```
