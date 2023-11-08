#!/usr/bin/env python3
"""Task 1 Simple pagination"""

from ast import Tuple
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method that returns a page
        Parameters:
            @page: int starting page
            @page_size: int size of page
        Return: A list of the pagination"""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        pagination: List[List] = self.dataset()

        range_idx: Tuple = self.index_range(page, page_size)

        if range_idx[0] >= len(pagination):
            return []

        return (pagination[range_idx[0]:range_idx[1]])

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Function that helps to get the range of indexes
        Parameters:
            @page: integer
            @page_size: integer
            Return: A tuple containing the range of indexes from
            start to end
        Note: In Pagination all the indexes starts at 1"""
        if page > 0 and page_size > 0:
            pass
        start = (page - 1) * page_size
        end = start + page_size
        return (start, end)
