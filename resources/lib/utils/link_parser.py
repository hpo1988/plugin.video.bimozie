# -*- coding: utf-8 -*-
import re
import xbmcaddon
import utils.xbmc_helper as helper
from urllib import urlencode
from .hosts import fshare, \
    imacdn, \
    phimmoi, \
    gpt2_phimmoi, \
    pzc_phimmoi, \
    hydrax, \
    fptplay, \
    ok, \
    vtv16, \
    hls_hydrax, \
    dongphim, \
    fembed, \
    hdclub, \
    animehay, \
    vuviphim, \
    rapidvid, \
    onlystream, \
    movie3s, \
    smamuhh1metro, \
    toolpg, \
    vtvhub, \
    phut90, \
    hphim, \
    cors, \
    streamlink, \
    mixdrop, \
    manga123, \
    googlevideo, \
    iframeembed, \
    fantvh, \
    vanlongstreaming, \
    feurl, \
    hls_parser, \
    streamtape, \
    vproxy, \
    header_location, \
    verystream


class LinkParser:
    def __init__(self, media):
        self.media = media
        self.url = media['link']

    def get_link(self):
        print("LinkParser:: Find link source of %s" % self.url)
        if re.search('ok.ru', self.url):
            # return self.get_link_resolveurl()
            return ok.get_link(self.url)

        if re.search('drive.google.com', self.url):
            return self.get_link_resolveurl()

        if re.search('feurl.com', self.url):
            return feurl.get_link(self.url, self.media)

        if re.search('streamtape.com', self.url):
            return streamtape.get_link(self.url, self.media)

        elif 'vhstream.xyz' in self.url \
                or 'vkooltv.com' in self.url \
                or '3s.live' in self.url \
                or 'vn.phimmoicdn.net' in self.url \
                or 'loadblancer.xemphimmedia.com' in self.url \
                :
            return cors.get_link(self.url, self.media)

        # elif 'cdnplay.xyz' in self.url \
        #         :
        #     return hls_parser.get_link(self.url, self.media)

        elif 'phimnhe.net/player/yotube.php' in self.url \
                or 'aio.vtvhub.com' in self.url \
                or 'xomphimhay.com/proxy/loadstream.php' in self.url \
                or 'xem-phim.tv/proxy' in self.url \
                or 'xemphimso.org/proxy' in self.url \
                or 'phimgi.tv/player/yotube.php' in self.url:
            return iframeembed.get_link(self.url, self.media)

        elif 'fimfast.com' in self.url \
                or 'cdnplay.xyz' in self.url \
                or 'vdicdn.com' in self.url \
                or 'phimngay.com' in self.url \
                or 'animehay.tv' in self.url \
                or 'beverly-downing' in self.url \
                or 'play.xomphimhay.com/load-stream' in self.url \
                or 'play.xemphimso.info/load-stream' in self.url \
                or 'proxymedia.site' in self.url \
                or 'goostreams.online' in self.url \
                or 'goolink.site' in self.url \
                or 'vtv16.site' in self.url \
                or 'fbcdn.net' in self.url \
                or 'googleapicdn.com' in self.url:
            return cors.get_link(self.url, self.media, including_agent=False)

        elif 'googlevideo.com' in self.url:
            return googlevideo.get_link(self.url, self.media)

        elif 'fantvh.net' in self.url:
            return fantvh.get_link(self.url, self.media)

        elif re.search('manga123.net', self.url):
            return manga123.get_link(self.url, self.media)

        # elif re.search('mixdrop.co', self.url):
        #     return self.get_link_resolveurl()

        elif re.search('mixdrop.co', self.url):
            return mixdrop.get_link(self.url, self.media), 'mixdrop.co'

        elif 'wowza' in self.url \
                :
            # or 'apihls.vproxy.online' in self.url:
            return streamlink.get_link(self.url, self.media)

        elif 'plb.animehay.tv' in self.url:
            return self.input_stream()

        elif '90p.tv' in self.url:
            return phut90.get_link(self.url, self.media), '90p.tv'

        elif 'lb.animehay.tv' in self.url:
            return animehay.get_link(self.url), 'animehay.tv'

        elif re.search('toolsp2p', self.url) \
                or re.search('player.toolpg.com', self.url) \
                or re.search('hls.hphim.org', self.url):
            return toolpg.get_link(self.url, self.media)

        elif re.search('hphim.org', self.url) \
                or re.search('facebookstream.cloud', self.url):
            return vanlongstreaming.get_link(self.url, self.media)

        elif re.search('openload.co', self.url):
            return self.get_link_openload()

        elif re.search('movie3s.net', self.url):
            return movie3s.get_link(self.url, self.media)

        elif 'apihls.vproxy.online' in self.url:
            return self.url, 'inputstream'

        elif 'phim7z.vproxy.online' in self.url:
            return vproxy.get_link(self.url, self.media)

        elif re.search('vtvhub.com', self.url) \
                or 'phim7z.vproxy.online' in self.url:
            return vtvhub.get_link(self.url, self.media)

        elif re.search('smamuhh1metro.com', self.url):
            return smamuhh1metro.get_link(self.url, self.media)

        elif re.search('stream.kiwi', self.url):
            return header_location.get_link(self.url, self.media)

        elif re.search('fshare.vn', self.url):
            return self.get_link_fshare()

        elif re.search('dailymotion.com', self.url):
            return self.get_link_resolveurl()

        elif re.search('streamango.com', self.url):
            return self.get_link_resolveurl()

        elif re.search('rapidvid.to', self.url):
            return rapidvid.get_link(self.url)

        elif re.search('verystream.com', self.url):
            return verystream.get_link(self.url)

        elif re.search('onlystream.tv', self.url):
            return onlystream.get_link(self.url)

        elif re.search('rapidvideo.com', self.url):
            return self.get_link_resolveurl()

        elif re.search('fembed.com', self.url):
            return fembed.get_link(self.url)

        elif re.search('24hd.club', self.url):
            return hdclub.get_link(self.url)

        elif re.search('vuviphim.xyz', self.url) \
                or re.search('vuviphimmoi.com', self.url) \
                or re.search('vuviphimz.com', self.url) \
                or re.search('thoctv.com', self.url):
            return vuviphim.get_link(self.url)

        elif re.search('fptplay.net', self.url):
            helper.message('FPTPlay hls link parsing', 'Get Link')
            return fptplay.get_link(self.url)

        elif re.search('sstreamgg.xyz', self.url) \
                or re.search('ggstream.me', self.url) \
                or re.search('hhstream.xyz', self.url) \
                or re.search('116.203.139.97', self.url) \
                or re.search('tstream.xyz', self.url):
            return self.get_referer_link()

        elif 'pzc.phimmoi' in self.url:
            return pzc_phimmoi.get_link(self.url, self.media)

        elif 'gpt.phimmoi' in self.url:
            helper.message('Phimmoi gpt.phimmoi.net link parsing', 'Get Link')
            return pzc_phimmoi.get_link(self.url, self.media)

        # elif 'gpt2.phimmoi.net' in self.url:
        elif re.search(r'gpt\d.phimmoi', self.url):
            return gpt2_phimmoi.get_link(self.url, self.media)

        elif re.search('hls.phimmoi', self.url):
            helper.message('Phimmoi hls link parsing', 'Get Link')
            return phimmoi.get_link(self.url, self.media['originUrl'])

        elif re.search('hydrax.html', self.url):
            helper.message('hydrax link parsing', 'Get Link')
            return hydrax.get_vip_hydrax(self.url, self.media)
        elif re.search('hydrax.net/watch', self.url):
            helper.message('hydrax link parsing', 'Get Link')
            return hydrax.get_guest_hydrax(self.url, self.media)

        # elif re.search('youtube.com', self.url):
        #     return self.get_youtube()

        elif re.search('imacdn.com', self.url):
            helper.message('imacdn HFF', 'Movie Found')
            return imacdn.get_link(self.url, self.media), 'imacdn'

        elif re.search('vtv16.com', self.url):
            return vtv16.get_link(self.url)

        elif re.search('hls.hydrax.net', self.url):
            return hls_hydrax.get_link(self.url, self.media), 'hls5'

        elif re.search('dgo.dongphim.net', self.url) \
                or re.search('dgo.dongphim.tv', self.url) \
                or re.search('dgo.dongphim.biz', self.url):
            return cors.get_link(self.url, self.media)

        elif '.xyz' in self.url:
            return cors.get_link(self.url, self.media, including_agent=False)

        elif self.url.endswith('m3u8'):
            return self.get_m3u8()

        return self.url, 'unknow'

    def get_youtube(self):
        self.url = self.url.replace(re.search('^http.*(\?.*)', self.url).group(1), '')
        try:
            import urlresolver
            re.sub('(^http.*)\?', '\1', self.url)
            stream_url = urlresolver.resolve(self.url)
            return stream_url, '720'
        except:
            return None

    def get_link_openload(self):
        try:
            import urlresolver
            stream_url = urlresolver.resolve(self.url)
            return stream_url, 'openload.co'
        except:
            return None, None

    def get_link_resolveurl(self):
        try:
            import urlresolver
            stream_url = urlresolver.resolve(self.url)
            return stream_url, 'URLResolver'
        except:
            return None, None

    def get_link_fshare(self):

        if not helper.getSetting('fshare.username'):
            helper.message('Required username/password to get fshare.vn link, open addon settings', 'Login Required')
            xbmcaddon.Addon().openSettings()
            return None, None

        if helper.getSetting('fshare.enable'):
            return fshare.FShareVN(
                self.url,
                helper.getSetting('fshare.username'),
                helper.getSetting('fshare.password')
            ).get_link(), 'Fshare'
        else:
            return fshare.FShareVN(self.url).get_link(), 'Fshare'

    def get_m3u8(self):
        # support to run with inputstream.adaptive
        if re.search('51.15.90.176', self.url):  # skip this for phimbathu & bilutv
            return self.url, 'hls5'

        # hls-streaming.phimgi.net
        if re.search('hls-streaming.phimgi.net', self.url):  # skip this for phimbathu & bilutv
            url = self.url + "|%s" % urlencode({
                'Origin': 'https://phimgi.net',
                'Referer': self.media['originUrl']
            })
            return url, 'hls5'

        return self.url, 'hls3'

    def get_referer_link(self):
        url = self.url + "|Referer=https://vuviphim.com/"
        return url, 'Referer'

    def input_stream(self):
        return self.url, 'hls'
