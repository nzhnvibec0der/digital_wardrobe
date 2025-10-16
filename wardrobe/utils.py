from rembg import remove, new_session
from io import BytesIO

# Явно создаём сессию с моделью u2net (универсальная)
session = new_session("u2net_cloth_seg")

def remove_background(image_file):
    """
    Удаляет фон с изображения, возвращает BytesIO без фона.
    """
    try:
        image_bytes = image_file.read()
        output = remove(image_bytes, session=session)

        if not output:
            raise ValueError("rembg вернул пустые данные")

        result = BytesIO(output)
        result.seek(0)

        with open("debug_removed.png", "wb") as f:
            f.write(result.getvalue())

    except Exception as e:
        print(f"[❌ rembg error]: {e}")
        image_file.seek(0)
        return image_file
