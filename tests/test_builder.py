# -*- coding: utf-8 -*-
"""\
Test against the buidler module.
"""
from __future__ import unicode_literals
from nose.tools import ok_, eq_, raises
from pyqrcode import builder


def test_illegal_mode():
    try:
        b = builder.QRCodeBuilder( version=1, error='M')
        b.add_data( 'test', 'murks' )
        raise Exception('Expected an error for illegal mode')
    except ValueError as ex:
        ok_('murks' in str(ex))


def test_illegal_error():
    try:
        b = builder.QRCodeBuilder( version=40, error='R')
        b.add_data( '123', 'numeric' )
        raise Exception('Expected an error for illegal mode')
    except ValueError as ex:
        ok_('R' in str(ex))


def test_illegal_version():
    try:
        b = builder.QRCodeBuilder( version=41, error='M')
        b.add_data( '123', 'numeric')
        raise Exception('Expected an error for illegal mode')
    except ValueError as ex:
        ok_('41' in str(ex))



if __name__ == '__main__':
    import nose
    nose.core.runmodule()
