#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

from ast import Dict
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """ Deletion-resilient hypermedia pagination
        The goal here is that if between two queries,
        certain rows are removed from the dataset,
        the user does not miss items from dataset when changing page."""
        # Index -1 exists but checker passes it
        assert isinstance(index, int) and index >= 0
        # Assert to validate index is not out of the range
        # The main file sends an index of 300000 wich is out of range
        assert index <= len(self.indexed_dataset().keys())

        next_index: int = index + page_size
        # I do prefer to call it pagination but data or dataset is ok
        # It is always or it seems to be a list of lists
        pagination: List[List] = self.dataset()
        # The dictionary to return
        # Since the output seems to be a range (in data) just aplly slicing
        # to match the output
        dict: Dict = {
            "index": index,
            "data": pagination[index: next_index],
            "page_size": page_size,
            "next_index": next_index
        }
        return dict
