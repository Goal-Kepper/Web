from flask import Flask


def create_app():

	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'SECRET'

	from app.views.auth.auth import is_logged_in
	app.before_request(is_logged_in)

	from app.views.auth import auth_bp
	app.register_blueprint(auth_bp)

	from app.views.index import index_bp
	app.register_blueprint(index_bp)


	import json
	from flask import request
	clients = [
		{
			'id': 1,
			'login': 'markeeff',
			'password': '12345678',
			'email': 'super@mail.ru'

		},
		{
			'id': 2,
			'login': 'kozuhoff',
			'password': '87654321',
			'email': 'puper@mail.ru'
		}
	]

	news = [
		{
			'id': 1,
			'name': 'Grand Opening!',
			'text': 'Вчера наконец-то открылась новая кофейня!'
		},
		{
			'id': 2,
			'name': 'Бегом с семьей!',
			'text': 'Новые акции для заказа 3 и более стаканчиков кофе'
		},
		{
			'id': 3,
			'name': 'Новые вершины',
			'text': 'Сегодня бариста открыл новый вид кофе - ф-латте-р'
		}
	]

	@app.route('/reg', methods=['POST'])
	def add_client():
		if type(request.json) is dict:
			new_client = request.json
		else:
			new_client = json.loads(request.json)
		if len(new_client) != 3 or \
			'login' not in new_client or \
			'password' not in new_client or \
			'email' not in new_client:
			return {'message': 'Невалидные данные'}, 400
		new_client['id'] = len(clients) + 1
		clients.append(new_client)
		return '', 201


	@app.route('/log', methods=['POST'])
	def check_client():
		if type(request.json) is dict:
			client = request.json
		else:
			client = json.loads(request.json)
		if len(client) != 2 or \
				'login' not in client or \
				'password' not in client:
			return {'message': 'Невалидные данные'}, 400
		for cl in clients:
			if cl['login'] == client['login'] and cl['password'] == client['password']:
				return '', 201
		return '', 202

	@app.route('/news', methods=['GET'])
	def get_news():
		return json.dumps(news)

	@app.route('/news', methods=['POST'])
	def add_news():
		if type(request.json) is dict:
			new_news = request.json
		else:
			new_news = json.loads(request.json)
		if len(new_news) != 2 or \
			'name' not in new_news or \
			'text' not in new_news:
			return {'message': 'Невалидные данные'}, 400
		new_news['id'] = len(news) + 1
		news.append(new_news)
		print(news)
		return '', 200

	@app.route('/news/<int:news_id>', methods=['PUT'])
	def update_news(news_id):
		new = next((n for n in news if n['id'] == news_id), None)
		params = request.json
		print(params, new)
		print("PUT")
		if not new:
			return {'message': 'Ошибка при редактировании'}, 400
		new.update(params)
		print(news)
		return '', 200

	@app.route('/news/<int:news_id>', methods=['DELETE'])
	def delete_client(news_id):
		idx, cur_news = next((n for n in enumerate(news) if n[1]['id'] == news_id), (None, None))
		print(cur_news, "DELETE")
		news.remove(cur_news)
		print(news)
		return '', 200

	return app
