from flask_restful import Resource

class CheckResource(Resource):
    def get():
        return {
                "success": True
                }
