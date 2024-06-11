from flask import Flask, request
from flask_restful import Resource, Api
from QQSpider.v1.spiders.index import IndexInfo
from QQSpider.v1.spiders.singer import singer as Singer
from QQSpider.v1.spiders.search_song import search as SearchSong
from QQSpider.v1.spiders.search_singer import search as SearchSinger
from QQSpider.v1.spiders.signer_detail import main

app = Flask(__name__)
api = Api(app)


class Index(Resource):
    def get(self):
        index = IndexInfo()
        index.main()
        return {'infos': index.infos}


class Singers(Resource):
    def get(self):
        page = request.args.get('page')
        singer = Singer(page)
        return {'info': singer}


class SearchSongs(Resource):
    def get(self):
        song = request.args.get('song')
        info = SearchSong(song)
        return {'info': info}


class SearchSingers(Resource):
    def get(self):
        singer = request.args.get('singer')
        info = SearchSinger(singer)
        return {'info': info}


class SingerDetail(Resource):
    def get(self):
        info = main()
        return {'message': "测试数据", 'info': info}


api.add_resource(Index, '/')
api.add_resource(Singers, '/singerlist')
api.add_resource(SearchSongs, '/searchsong')
api.add_resource(SearchSingers, '/searchsinger')
api.add_resource(SingerDetail, '/singerdetail')

if __name__ == '__main__':
    app.run(debug=True)
