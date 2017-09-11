#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Creation:    06.06.2017
# Last Update: 21.07.2017
#
# <https://codewerft.net>
#
# Copyright (c) 2017 Codewerft UG (haftungsbeschränkt)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from seastar.model.platform_anatomy import Platform as PlatformModel
from seastar.model.platform_anatomy import ComputeNode as ComputeNodeModel
from seastar.model.platform_anatomy import Processor as ProcessorModel
from seastar.model.platform_anatomy import ProcessorCore as ProcessorCoreModel


class Platform(SQLAlchemyObjectType):

    class Meta:
        model = PlatformModel
        interfaces = (relay.Node, )

class ComputeNode(SQLAlchemyObjectType):

    class Meta:
        model = ComputeNodeModel
        interfaces = (relay.Node, )

class Processor(SQLAlchemyObjectType):

    class Meta:
        model = ProcessorModel
        interfaces = (relay.Node, )

class ProcessorCore(SQLAlchemyObjectType):

    class Meta:
        model = ProcessorCoreModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_Platforms = SQLAlchemyConnectionField(Platform)
    all_Nodes = SQLAlchemyConnectionField(ComputeNode)
    all_Processors = SQLAlchemyConnectionField(Processor)
    all_ProcessorCores = SQLAlchemyConnectionField(ProcessorCore)


    # role = graphene.Field(Role)


schema = graphene.Schema(query=Query, types=[Platform, ComputeNode, Processor, ProcessorCore])
