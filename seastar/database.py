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

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    # from .models import Department, Employee, Role
    from seastar.model.platform_anatomy import Platform, ComputeNode, Processor, ProcessorCore

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # # Create the fixtures
    # engineering = Department(name='Engineering')
    # db_session.add(engineering)
    # hr = Department(name='Human Resources')
    # db_session.add(hr)
    #
    # manager = Role(name='manager')
    # db_session.add(manager)
    # engineer = Role(name='engineer')
    # db_session.add(engineer)
    #
    # peter = Employee(name='Peter', department=engineering, role=engineer)
    # db_session.add(peter)
    # roy = Employee(name='Roy', department=engineering, role=engineer)
    # db_session.add(roy)
    # tracy = Employee(name='Tracy', department=hr, role=manager)
    # db_session.add(tracy)
    # db_session.commit()

    cluster = Platform(name='cyrus')
    db_session.add(cluster)

    for n in range(0, 8):
        node = ComputeNode(name='node-'+str(n), platform=cluster)
        db_session.add(node)

        for p in range(0, 8):
            processor = Processor(name="processor-"+str(p), compute_node=node)
            db_session.add(processor)


            for c in range(0, 16):
                core = ProcessorCore(name="core-"+str(p), processor=processor)
                db_session.add(core)

    db_session.commit()
