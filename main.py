def find_removed_word(sentence: str, new_size_diff: int = 16) -> str:
    words = ["Ложка", "лес", "комбайн", "льдина", "обезьяна", "микроволновка", "видеокарта"]
    for word in words:
        # Убираем слово, запятые и пробелы, которые могут стать лишними
        modified_sentence = sentence.replace(f"{word}, ", "").replace(f", {word}", "").replace(f" – {word}", "").replace(f" {word}", "")
        
        # Проверяем размер предложения в байтах
        original_size = len(sentence.encode('utf-16le'))
        new_size = len(modified_sentence.encode('utf-16le'))
        
        # Если разница равна 16 байтам, мы нашли слово
        if original_size - new_size == new_size_diff:
            return word

    return "Не удалось найти слово"
    
# Исходное предложение
sentence = "Ложка, лес, комбайн, льдина, обезьяна, микроволновка, видеокарта – это слова"

# Находим удалённое слово
removed_word = find_removed_word(sentence)
print(f"Удалённое слово: {removed_word}")
