from chans import CHANS

PREFIX = "/video/turkishchannels"
NAME = "Turkish Channels"
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


@route(PREFIX + '/watch')
def CreateVideoStream(url, title, thumb):
    v_content = VideoClipObject(
        key=Callback(CreateVideoStream, url=url, title=title, thumb=thumb),
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
