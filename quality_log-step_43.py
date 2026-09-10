# === Stage 43: Добавь пагинацию длинных списков ===
# Project: QualityLog
def paginate_table(table, page_size=10):
    """Returns a generator yielding (page_index, page_records) tuples."""
    for i in range(0, len(table), page_size):
        yield i // page_size, table[i:i + page_size]
