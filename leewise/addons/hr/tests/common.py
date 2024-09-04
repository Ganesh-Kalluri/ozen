# -*- coding: utf-8 -*-
# Part of Leewise. See LICENSE file for full copyright and licensing details.

from leewise.addons.mail.tests.common import mail_new_test_user
from leewise.tests import common


class TestHrCommon(common.TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestHrCommon, cls).setUpClass()

        cls.res_users_hr_officer = mail_new_test_user(cls.env, login='hro', groups='base.group_user,hr.group_hr_user', name='HR Officer', email='hro@example.com')
