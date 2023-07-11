from rest_framework import pagination

class BookingPagination(pagination.PageNumberPagination):
    page_size=3
    page_size_query_param='perpage'
    max_page_size=10
    page_query_param='page'

class MenuPagination(pagination.PageNumberPagination):
    page_size=2
    page_size_query_param='perpage'
    max_page_size=5
    page_query_param='page'