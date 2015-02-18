PREFIX = "/video/turkishchannels"

NAME = "turkish channels"

SHOWTV_STREAM_URL = "http://live-ciner.mncdn.net/showtv/showtv2/radyodelisi.m3u8"
SHOWTV_TITLE = "show tv"

TV8_STREAM_URL = "http://origin.live.web.tv.streamprovider.net/streams/7ea4b11a8660697ab54a3e7d03bdfef7_live_0_0/index.m3u8"
TV8_TITLE = "tv 8"

KANALD_STREAM_URL = "http://media.netd.com.tr/S1/HLS_LIVE/kanald/1500/prog_index.m3u8"
KANALD_TITLE = "kanal d"

STARTV_STREAM_URL = "http://origin.live.web.tv.streamprovider.net/streams/7acfc999bbde179fc45f18506125345f_live_0_0/index.m3u8"
STARTV_TITLE = "star"

CHANS = {
    SHOWTV_TITLE: [SHOWTV_STREAM_URL, R('show-tv.png')],
    TV8_TITLE: [TV8_STREAM_URL, R('tv8.png')],
    KANALD_TITLE: [KANALD_STREAM_URL, R('kanald.png')],
    STARTV_TITLE: [STARTV_STREAM_URL, R('startv.png')]
    }

DEFAULT_THUMB = R('icon-default.png')


def Start():
    ObjectContainer.title1 = NAME


@handler(PREFIX, NAME)
def MainMenu():
    oc = ObjectContainer()
    for k, v in CHANS.iteritems():
        oc.add(CreateVideoStream(url=v[0],
                                 title=k,
                                 thumb=v[1]))
    return oc


@route(PREFIX + '/showtv')
def CreateVideoStream(url, title, thumb, container=False):
    v_content = VideoClipObject(
        key=Callback(CreateVideoStream, url=url, title=title, thumb=thumb, container=True),
        url=url,
        title=title,
        thumb=thumb,
        items=[
            MediaObject(
                parts=[
                    PartObject(
                        key=HTTPLiveStreamURL(url=url)
                    )
                ],
                optimized_for_streaming=True
            )
        ]
    )
    return v_content
