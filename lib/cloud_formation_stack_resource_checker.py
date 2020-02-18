import boto3


class CloudFormationStackResourceChecker:

    def __init__(self):
        self.cloudformation = boto3.client('cloudformation')

    def get_stack_and_resource_count(self):
        stacks = self._get_stack_list()
    
        stack_and_resource_counts = []
        for stack in stacks:
            stack_name = stack['StackName']
            resources = self._get_stack_resources(stack_name)
            stack_and_resource_counts.append({
                'StackName': stack_name,
                'ResourceCount': len(resources)
            })

        return stack_and_resource_counts

    def _get_stack_list(self, token=None):
        option = {
            'StackStatusFilter': ['CREATE_COMPLETE']
        }
    
        if token is not None:
            option['NextToken'] = token
    
        res = self.cloudformation.list_stacks(**option)
        stacks = res.get('StackSummaries', [])
    
        if 'NextToken' in res:
            stacks += self._get_stack_list(res['NextToken'])
    
        return stacks

    def _get_stack_resources(self, stack_name, token=None):
        option = {
            'StackName': stack_name
        }
    
        if token is not None:
            option['NextToken'] = token
    
        res = self.cloudformation.list_stack_resources(**option)
        resources = res.get('StackResourceSummaries', [])
    
        if 'NextToken' in res:
            resources += self._get_stack_resources(res['NextToken'])
        return resources
    
