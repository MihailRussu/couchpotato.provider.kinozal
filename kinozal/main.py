# -*- coding: utf8 -*-

import traceback

from couchpotato.core.helpers.variable import tryInt
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrent.base import TorrentProvider
from couchpotato.core.media.movie.providers.base import MovieProvider
from bs4 import BeautifulSoup
from datetime import datetime

log = CPLog(__name__)


class kinozal(TorrentProvider, MovieProvider):
    baseurl = 'http://kinozal.tv'
    urls = {
        'test': baseurl,
        'login': "{}/takelogin.php".format(baseurl),
        'login_check': "{}/my.php".format(baseurl),
        'detail': '{}/details.php?id=%s'.format(baseurl),
        'search': '{}/browse.php?s=%s&c=1200'.format(baseurl),
        'download': '{}/download.php?id=%s'.format(baseurl),
    }

    size_gb = [u'гб']
    size_mb = [u'мб']
    size_kb = [u'кб']

    http_time_between_calls = 3  # seconds

    cat_ids = [
        ([1], ['brrip', 'dvdrip']),
        ([2], ['dvdr']),
        ([3], ['720p', '1080p']),
        ([4], ['bd50']),
        ([5], ['cam', 'ts', 'tc', 'r5', 'scr']),
        ([6], ['3d']),
    ]

    def getLoginParams(self):
        log.debug('Getting login params for kinozal')
        return {
            'username': self.conf('username'),
            'password': self.conf('password'),
            'returnto': ''
        }

    def loginSuccess(self, output):
        isLoginSuccessful = '/logout.php?hash4u=' in output
        log.debug('Checking login success for kinozal: %s' % isLoginSuccessful)
        return isLoginSuccessful

    loginCheckSuccess = loginSuccess

    def _searchOnTitle(self, title, movie, quality, results):

        if not title or len(title) < 3:
            return log.debug("No title passed or it is too short, skipping...")

        title = title.encode('utf-8')
        movie_year = int(movie['info']['year'])
        log.debug('Searching kinozal for {} ({})'.format(title, movie_year))

        kinozal_categories = self.getCatId(quality) or [0]

        initial_url = self.urls['search'] % title.replace(':', ' ')

        for kinozal_category in kinozal_categories:

            url = initial_url + '&v=' + str(kinozal_category)
            log.debug('Fetching {}'.format(url))

            data = self.getHTMLData(url).decode('cp1251')

            if not data:
                self.debug('Could not get search results form kinozal...')
                continue

            html = BeautifulSoup(data)
            try:
                result_table = html.find('table', attrs={'class': 't_peer'})
                if not result_table:
                    log.debug('No table results from kinozal')
                    return

                torrents = result_table.find_all('tr', attrs={'class': 'bg'})
                log.debug('Found {} potential torrents...'.format(len(torrents)))

                for idx, torrent in enumerate(torrents):
                    result = {}
                    log.debug('Working on #{} - {}'.format(idx + 1, torrent))

                    # lookup torrent's full name & ID
                    info_cell = torrent.find('td', attrs={'class': 'nam'})
                    result['id'] = info_cell.find('a')['href'].split('=')[1]
                    result['name'] = info_cell.getText()

                    # is the year in torrent's name? i.e. is it worth further analysis?
                    if not any([str(year) in result['name'] for year in [movie_year - 1, movie_year, movie_year + 1]]):
                        log.debug("Neither {} nor it's neighbors were found in {}".format(movie_year, result['name']))
                        continue

                    # lookup torrent's size
                    size_cell = torrent.find_all('td', attrs={'class': 's'})[1]
                    result['size'] = self.parseSize(size_cell.getText())

                    # lookup torrent's seeders
                    seeders_cell = torrent.find('td', attrs={'class': 'sl_s'})
                    result['seeders'] = tryInt(seeders_cell.getText())
                    # result['leechers'] = 0

                    # lookup & calculate torrent's age
                    torrent_uploaded = torrent.find_all('td', attrs={'class': 's'})[2].getText()[:-8].strip()
                    result['age'] = (datetime.today() - datetime.strptime(torrent_uploaded, '%d.%m.%Y')).days

                    # fill the rest of the data
                    result['url'] = self.urls['download'] % result['id']
                    result['detail_url'] = self.urls['detail'] % result['id']

                    log.debug(u'result = {}'.format(result))
                    results.append(result)

            except:
                log.error('Failed to parse kinozal: %s' % (traceback.format_exc()))
