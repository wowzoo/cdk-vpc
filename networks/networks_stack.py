from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_ssm as ssm,
)


class VPCStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        workshop_vpc = ec2.Vpc(
            self,
            "VPC",
            max_azs=2,
            cidr="10.10.0.0/16",
            # Create 2 groups in 2 AZs
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE,
                    name="Private",
                    cidr_mask=24
                )
            ],
            nat_gateways=2,
        )

        ssm.StringParameter(
            self,
            "VPCIDStringParameter",
            parameter_name="vpc-id",
            string_value=workshop_vpc.vpc_id
        )

        workshop_security_group = ec2.SecurityGroup(
            self,
            "WorkshopSecurityGroup",
            vpc=workshop_vpc,
            description="Security Group for workshop",
            security_group_name="WorkshopSecurityGroup"
        )

        ssm.StringParameter(
            self,
            "SecurityGroupStringParameter",
            parameter_name="security-group-id",
            string_value=workshop_security_group.security_group_id
        )

        core.CfnOutput(
            self,
            "VPC ID",
            value=workshop_vpc.vpc_id
        )

        core.CfnOutput(
            self,
            "Security Group ID",
            value=workshop_security_group.security_group_id
        )
