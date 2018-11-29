"""Views for the Products Resource"""

from flask_restful import Resource, reqparse,Api
from flask import request
from app.v1.models import Redflags


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('title', help="You must supply thetitle", required='True')
parser.add_argument('nature', help="You must supply the nature", required='True')
parser.add_argument('comment', help="You must supply the comment", required='True')


class NewRedflags(Resource):

    """
        Class to handle adding and fetching all redflags
    """
    def post(self):

        """Route to handle creating redflags"""

        args = parser.parse_args()
        return Redflags().add_redflag(
            args['title'],
            args['nature'],
            args['comment']
			)
    

class GetRedflags(Resource):
    
    def get(self):

        """Route to fetch all redflags"""

        return Redflags().get_all_redflags()

class GetRedflag(Resource):

    def get(self, redflag_id):

        """Route to fetch a specific redflag"""

        return Redflags().get_one_redflag(redflag_id)


