from io import BytesIO

# ⚠️ Заглушка: не вызывает rembg, чтобы не крашить Render Free
def remove_background(image_file):
    """
    Временная функция-заглушка для деплоя на Render Free.
    Просто возвращает оригинальное изображение без удаления фона.
    """
    try:
        data = image_file.read()
        result = BytesIO(data)
        result.seek(0)
        return result
    except Exception as e:
        print(f"[❌ background removal error]: {e}")
        image_file.seek(0)
        return image_file
