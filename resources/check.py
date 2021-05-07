from flask_restful import Resource

class CheckResource(Resource):
    def get(self):
        return {
                "success": True
                }
