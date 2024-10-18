DISK_SIZE_MB = 1.44
DISK_SIZE_BYTES = DISK_SIZE_MB * 1024 * 1024
PAGES_PER_BOOK = 100
LINES_PER_PAGE = 50
CHARS_PER_LINE = 25
BYTES_PER_CHAR = 4

book_size_bytes = PAGES_PER_BOOK * LINES_PER_PAGE * CHARS_PER_LINE * BYTES_PER_CHAR

books_on_disk = DISK_SIZE_BYTES // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(books_on_disk))
