from flask import Flask
from flask_restful import Resource, reqparse, Api
from gensim.summarization import summarize



app = Flask(__name__)
api = Api(app)

class Summary(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('Text', type=str, required=True, help='Conversation text')
	parser.add_argument('Ratio', type=float, required=False, help='Summary ratio')

	def get(self):
		args = Summary.parser.parse_args()
		text =  args['Text']
		ratio = 0.7
		if args['Ratio']:
			ratio = args['Ratio']
		summarized_text = summarize(text, ratio)
		return {'Topic': summarized_text.split(".")[0], 'Summary': summarized_text.replace('\n',' ')}

api.add_resource(Summary, '/summary')

if __name__=='__main__':
    app.run(debug=True)