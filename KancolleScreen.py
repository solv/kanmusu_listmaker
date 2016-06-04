#!/usr/bin/python
# -*- coding: utf-8 -*-

from logging import getLogger,StreamHandler,DEBUG

# ログ設定
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
