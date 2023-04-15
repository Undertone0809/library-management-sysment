# -*- coding: utf-8 -*-
# @Time    : 2023/4/15 14:48
# @Author  : Zeeland
# @File    : book_service.py
# @Software: PyCharm

import logging
from model.base_model import BaseModel
from model.book import Book
from service import cache_service
from typing import Optional, List, Union

__all__ = ['show_all_books', 'query_book']


def show_all_books() -> Optional[List[dict]]:
    return cache_service.get_all_model_data(Book)


def add_book(book: Book) -> Optional[List[dict]]:
    return cache_service.append_model_data(book)


def query_book(book: Book) -> Optional[List[dict]]:
    return cache_service.query_model_data(book)


def query_book(keyword: str) -> Optional[Book]:
    pass