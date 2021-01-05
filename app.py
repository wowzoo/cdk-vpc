#!/usr/bin/env python3

from aws_cdk import core
from networks.networks_stack import VPCStack


app = core.App()
VPCStack(app, "WorkshopVPC")

core.Tags.of(app).add("Owner", "wowzoo")

app.synth()
