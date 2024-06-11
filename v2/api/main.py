from flask import Flask, request
from flask_restful import Resource, Api
from v2.spiders.music import QQMusic
import asyncio

app = Flask(__name__)
api = Api(app)


class Index(Resource):
    def get(self):
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop = asyncio.get_event_loop()
        music = QQMusic()
        type = request.args.get('type')
        ip_address = request.remote_addr

        if 'links' in type:
            links = loop.run_until_complete(music.index_links())
            return {'ip': ip_address, 'infos': links}
        elif 'hots' in type:
            hots = loop.run_until_complete(music.index_hots())
            loop.close()
            return {'ip': ip_address, 'infos': hots}
        elif 'new' in type:
            new = loop.run_until_complete(music.index_new_songs())
            return {'ip': ip_address, 'infos': new}
        elif 'wonder' in type:
            wonder = loop.run_until_complete(music.index_wonder())
            return {'ip': ip_address, 'infos': wonder}
        elif 'albums' in type:
            albums = loop.run_until_complete(music.index_albums())
            return {'ip': ip_address, 'infos': albums}
        elif 'ranks' in type:
            ranks = loop.run_until_complete(music.index_ranks())
            return {'ip': ip_address, 'infos': ranks}
        elif 'mv' in type:
            mv = loop.run_until_complete(music.index_mv())
            return {'ip': ip_address, 'infos': mv}
        elif 'srank' in type:
            srank = loop.run_until_complete(music.index_search_ranks())
            return {'ip': ip_address, 'infos': srank}
        else:
            return {'ip': ip_address, 'infos': '接口不存在'}


class Search(Resource):
    def get(self):
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop = asyncio.get_event_loop()
        music = QQMusic()
        type = request.args.get('type')

        ip_address = request.remote_addr

        if 'song' in type:
            song = request.args.get('song')
            mode = request.args.get('mode')
            song = loop.run_until_complete(music.index_search_song(song, mode))
            return {'ip': ip_address, 'infos': song}

        elif 'singer' in type:
            singer = request.args.get('singer')
            mode = request.args.get('mode')
            singer = loop.run_until_complete(music.index_search_singer(singer, mode))
            return {'ip': ip_address, 'infos': singer}
        elif 'detail' in type:
            song = request.args.get('song')
            detail = loop.run_until_complete(music.song_detail(song))
            return {'ip': ip_address, 'infos': detail}
        elif 'comment' in type:
            song = request.args.get('song')
            mode = request.args.get('mode')
            song = loop.run_until_complete(music.song_comment(song, mode))
            return {'ip': ip_address, 'infos': song}
        else:
            return {'ip': ip_address, 'infos': '接口不存在'}


class LoginSearch(Resource):
    def get(self):
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop = asyncio.get_event_loop()
        music = QQMusic()
        type = request.args.get('type')

        ip_address = request.remote_addr

        if 'song' in type:
            song = request.args.get('song')
            song = loop.run_until_complete(music.handle_login_search_info(song))
            return {'ip': ip_address, 'infos': song}

        elif 'singer' in type:
            singer = request.args.get('singer')
            singer = loop.run_until_complete(music.handle_login_search_info(singer))
            return {'ip': ip_address, 'infos': singer}

        elif 'detail' in type:
            song = request.args.get('song')
            detail = loop.run_until_complete(music.handle_login_song_detail(song))
            return {'ip': ip_address, 'infos': detail}
        elif 'comment' in type:
            song = request.args.get('song')
            song = loop.run_until_complete(music.song_comment(song, 'lg'))
            return {'ip': ip_address, 'infos': song}
        elif 'mv' in type:
            song = request.args.get('song')
            detail = loop.run_until_complete(music.handle_login_search_mv(song))
            return {'ip': ip_address, 'infos': detail}
        else:
            return {'ip': ip_address, 'infos': '接口不存在'}


class Singer(Resource):
    def get(self):
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop = asyncio.get_event_loop()
        music = QQMusic()
        type = request.args.get('type')
        category = request.args.get('category')
        page = request.args.get('page')

        ip_address = request.remote_addr
        infos = loop.run_until_complete(music.handle_singer_categpory(type, category, page))
        if infos:
            return {'ip': ip_address, 'infos': infos}
        else:
            return {'ip': ip_address, 'infos': '接口不存在'}


class Ranks(Resource):
    def get(self):
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop = asyncio.get_event_loop()
        music = QQMusic()
        keyword = request.args.get('keyword')
        ip_address = request.remote_addr
        infos = loop.run_until_complete(music.handle_ranks(keyword))
        if infos:
            return {'ip': ip_address, 'infos': infos}
        else:
            return {'ip': ip_address, 'infos': '接口不存在'}


class Songs(Resource):
    def get(self):
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        loop = asyncio.get_event_loop()
        music = QQMusic()
        keyword = request.args.get('keyword')
        ip_address = request.remote_addr
        infos = loop.run_until_complete(music.handle_song(keyword))
        if infos:
            return {'ip': ip_address, 'infos': infos}
        else:
            return {'ip': ip_address, 'infos': '接口不存在'}


api.add_resource(Index, '/index')
api.add_resource(Search, '/search')
api.add_resource(LoginSearch, '/ls')
api.add_resource(Singer, '/singer')
api.add_resource(Ranks, '/ranks')
api.add_resource(Songs, '/song')

if __name__ == '__main__':
    app.run(debug=True)
