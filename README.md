# aws_util
aws python libraries.

# libraries
## cloud_formation_stack_resource_checker.py
### purpose
cloudformation has stack limits.
this is to check stack.
### usage
```
cloud_formation_stack_resource_checker = CloudFormationStackResourceChecker()
cloud_formation_stack_resource_checker.get_stack_and_resource_count()
```
