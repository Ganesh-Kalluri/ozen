# Part of Leewise. See LICENSE file for full copyright and licensing details.

from werkzeug.exceptions import NotFound

from leewise import http
from leewise.http import request
from leewise.addons.mail.models.discuss.mail_guest import add_guest_to_context


class WebclientController(http.Controller):
    @http.route("/mail/init_messaging", methods=["POST"], type="json", auth="public")
    @add_guest_to_context
    def mail_init_messaging(self):
        if not request.env.user._is_public():
            return request.env.user.sudo(False)._init_messaging()
        guest = request.env["mail.guest"]._get_guest_from_context()
        if guest:
            return guest._init_messaging()
        raise NotFound()

    @http.route("/mail/load_message_failures", methods=["POST"], type="json", auth="user")
    def mail_load_message_failures(self):
        # sudo as to not check ACL, which is far too costly
        # sudo: res.users - return only failures of current user as author
        return request.env.user.partner_id._message_fetch_failed()
