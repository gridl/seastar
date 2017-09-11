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


from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship

from seastar.database import Base

### PLATFORM COMPONENTS

class Platform(Base):
    """ [Platform Anatomy]
    """
    __tablename__ = 'pa_platform'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class ComputeNode(Base):
    """ [Platform Anatomy] ComputeNode represents a specific compute node of
        'platform'.
    """
    __tablename__ = 'pa_compute_node'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    platform_id = Column(Integer, ForeignKey('pa_platform.id'))

    platform = relationship(
        Platform,
        backref=backref('pa_compute_node',
                        uselist=True,
                        cascade='delete,all'))


class Processor(Base):
    """ [Platform Anatomy] Processor represents a specific processor of
        'node'.
    """
    __tablename__ = 'pa_processor'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    compute_node_id = Column(Integer, ForeignKey('pa_compute_node.id'))
    compute_node = relationship(
        ComputeNode,
        backref=backref('pa_Processor',
                        uselist=True,
                        cascade='delete,all'))


class ProcessorCore(Base):
    """ [Platform Anatomy] ProcessorCore represents a specific core of
        'processor'.
    """
    __tablename__ = 'pa_ProcessorCore'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    processor_id = Column(Integer, ForeignKey('pa_processor.id'))
    processor = relationship(
        Processor,
        backref=backref('pa_ProcessorCore',
                        uselist=True,
                        cascade='delete,all'))
