#!/usr/bin/env python3

from aws_cdk import core

from networks.networks_stack import NetworksStack


app = core.App()
NetworksStack(app, "networks")

app.synth()
