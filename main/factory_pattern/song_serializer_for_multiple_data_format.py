
import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:

    def serialize(self, song, format):
        serializer_factory = SongSerializerFactory()
        serializer = serializer_factory._get_serializer(format)
        return serializer._serialize(song)


class SongSerializerFactory:
    def _get_serializer(self, format):
        if format == 'JSON':
            return JSONSerializer()
        elif format == 'XML':
            return XMLSerializer()
        else:
            raise ValueError(format)


class Serializer:
    def _serialize(self, song):
        pass


class JSONSerializer(Serializer):
    def _serialize(self, song):
        song_info = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(song_info)


class XMLSerializer(Serializer):
    def _serialize(self, song):
        song_info = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_info, 'title')
        title.text = song.title
        artist = et.SubElement(song_info, 'artist')
        artist.text = song.artist
        return et.tostring(song_info, encoding='unicode')


# main function in python
def main():
    # print('Hello World')
    song = Song('1', 'All the best!', 'Ram Leela Bansali.')
    print(song)
    serializer = SongSerializer()
    print(serializer)
    result = serializer.serialize(song, 'XML')
    print(result)
    result = serializer.serialize(song, 'JSON')
    print(result)


if __name__=="__main__":
    main()
