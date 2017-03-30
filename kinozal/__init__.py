# -*- coding: utf8 -*-

from kinozal.main import kinozal


def autoload():
    return kinozal()


config = [{
    'name': 'kinozal',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'Кинозал.ТВ',
            'description': 'Торрент трекер <a href="http://kinozal.tv/">Кинозал.ТВ</a>',
            'wizard': True,
            'icon': 'AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAQAQAAAAAAAAAAAAAAAAAAAAAAACARztMgEc7/4BHO/+ARztMAAAAAIBHO0yhd2n/gEc7/6F3af+ARztMAAAAAIBHO0yARzv/gEc7/4BHO0wAAAAAgEc7/7iYiv/O4+r/pH5x/4FIPP+kfnH/zsrE/87j6v/OycL/pYB1/4BHO/+jfHD/ztbV/7+yrP+ARzv/AAAAAIBHO//O4+r/zu/9/87v/f/O7/3/zu/9/87v/f/O7/3/zu/9/87v/f/O7/3/zu/9/87v/f/O1dT/gEc7/wAAAACARztMpYB1/87v/f8IC5X/CAuV/wgLlf8IC5X/zu/9/77h+v9vgcv/SFSy/wAAif97j87/oXdp/4BHO0wAAAAAAAAAAIBHO//O7/3/gabq/w4Tnv8OE57/gabq/87v/f96muj/DBCd/wAAif83SMf/zu/9/4BHO/8AAAAAAAAAAIBHO0ynhXv/zu/9/87v/f8OE57/CAuV/87v/f+63vn/Hyqx/wAAif9KXMX/zO38/87v/f+mhHn/gEc7TAAAAAChd2n/1eHk/87v/f/O7/3/DhOe/wgLlf9nhuT/MEPF/wAAif82ScT/utjy/87v/f/O7/3/zsrD/6F3af8AAAAAgEc7/9Pk6v/O7/3/zu/9/xQcqP8IC5X/FBqo/xUYlf9of9v/zu/9/87v/f/O7/3/zu/9/87d4f+ARzv/AAAAAIBHO//Y19X/zu/9/87v/f8RGaT/CAuV/wAAif90h8v/zu/9/87v/f/O7/3/zu/9/87v/f/OycL/gEc7/wAAAAChd2n/up6S/87v/f/O7/3/ERmk/wgLlf9DXdj/CQ6Z/zdAqf/O7/3/zu/9/87v/f/O7/3/upyQ/6F3af8AAAAAgEc7TIJLQP/P7/3/zu/9/xQcqP8IC5X/zu/9/46l2f8jNMD/gJXS/87v/f/O7/3/zu/9/45kXf+ARztMAAAAAAAAAACARzv/0e35/5Go2/8UHKj/CAuV/5Go2//O7/3/XHDY/w4Tn/8YHJf/QEms/9Dr9v+ARzv/AAAAAAAAAACARztMu6KY/9Hu+v8IC5X/CAuV/wgLlf8IC5X/zu/9/87v/f9OZtz/FB2q/y08wv/Q6/b/oXdp/4BHO0wAAAAAgEc7/9/s8P/R7fn/0e77/9Hu+//O7/3/zu/9/87v/f/O7/3/z+/9/9Dt+P/Q7Pf/3u3t/87n8P+ARzv/AAAAAIBHO//Sz8j/3+zw/7qhlf+IWE//o31w/9jZ2P/a7fH/2NfV/7ylm/+GVEr/qYyD/87o8f/R2dj/gEc7/wAAAACARztMgEc7/4BHO/+ARztMAAAAAIBHO0yARzv/gEc7/4BHO/+ARztMAAAAAIBHO0yARzv/gEc7/4BHO0wAAAAACCEAAAABAAAAAQAAAAEAAIADAAAAAQAAAAEAAAABAAAAAQAAAAEAAAABAACAAwAAAAEAAAABAAAAAQAACCEAAA==',
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 48,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 0,
                    'description': 'Starting score for each release found via this provider.',
                },
                {
                    'name': 'auto-update',
                    'advanced': True,
                    'label': 'Automatic Update',
                    'type': 'bool',
                    'default': 1,
                    'description': 'Automatic update at startup.',
                }
            ],
        },
    ],
}]
