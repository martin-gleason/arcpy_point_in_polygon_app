from flask_restful import reqparse


class GetAddress:
    parser = reqparse.RequestParser()
    parser.add_argument(
        "address",
        type=str,
        required=True,
        help="This field cannot be left blank",
    )
