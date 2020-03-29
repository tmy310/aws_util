# -*- coding: utf-8 -*-

from libs.cloud_formation_stack_resource_checker  import CloudFormationStackResourceChecker

cloud_formation_stack_resource_checker = CloudFormationStackResourceChecker()
print(cloud_formation_stack_resource_checker.get_stack_and_resource_count())

