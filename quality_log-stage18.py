# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: QualityLog
class Tag:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color or '#6363ff'

    def to_dict(self):
        return {'name': self.name, 'color': self.color}

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d.get('color'))

class TagManager:
    _tags = {}

    @staticmethod
    def get_all():
        return list(TagManager._tags.values())

    @staticmethod
    def add(tag_name, color=None):
        if tag_name in TagManager._tags:
            print(f"Tag '{tag_name}' already exists.")
            return None
        tag = Tag(tag_name, color)
        TagManager._tags[tag.name] = tag
        return tag

    @staticmethod
    def remove(tag_name):
        if tag_name not in TagManager._tags:
            print(f"Tag '{tag_name}' does not exist.")
            return False
        del TagManager._tags[tag_name]
        return True

    @staticmethod
    def get_or_add(name, color=None):
        existing = TagManager._tags.get(name)
        if existing:
            return existing
        new_tag = TagManager.add(name, color)
        if new_tag is None:
            return None
        return new_tag

# Пример использования:
if __name__ == '__main__':
    t1 = TagManager.add('Critical', '#ff0000')
    print(f"Created tag: {t1}")

    t2 = TagManager.get_or_add('Bug', '#00ff00')
    print(f"Retrieved or created: {t2}")

    removed = TagManager.remove(t1.name)
    print(f"Removed tag '{t1.name}': {removed}")

    all_tags = TagManager.get_all()
    print(f"All tags: {[t.to_dict() for t in all_tags]}")
